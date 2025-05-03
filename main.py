from flask import Flask, render_template, request, redirect, url_for
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/images/gallery'
app.config['ALLOWED_EXTENSIONS'] = {'png', 'jpg', 'jpeg', 'gif'}

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']


@app.route('/')
@app.route('/index')
def index():
    title = request.args.get('title', 'Марсианская миссия')
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html',
                         prof=prof,
                         title="Тренировки")

@app.route('/list_prof/<list_type>')
def list_prof(list_type):
    professions = [
        "Инженер-конструктор",
        "Пилот",
        "Строитель",
        "Врач",
        "Биолог",
        "Геолог",
        "Метеоролог",
        "Астробиолог",
        "Программист",
        "Электротехник"
    ]
    return render_template('list_prof.html',
                         list_type=list_type,
                         professions=professions,
                         title="Список профессий")

@app.route('/answer')
@app.route('/auto_answer')
def answer():
    user_data = {
        'title': 'Анкета участника миссии',
        'surname': 'Watny',
        'name': 'Mark',
        'education': 'выше среднего',
        'profession': 'штурман марсохода',
        'sex': 'male',
        'motivation': 'Всегда мечтал застрять на Марсе!',
        'ready': 'True'
    }
    return render_template('auto_answer.html', **user_data)

@app.route('/departments')
def departments():
    departments_list = [
        {'id': 1, 'title': 'Инженерный департамент', 'chief': 1, 'members': '1, 2, 3', 'email': 'eng@mars.org'},
        {'id': 2, 'title': 'Научный департамент', 'chief': 4, 'members': '4, 5, 6', 'email': 'science@mars.org'}
    ]
    return render_template('departments.html',
                         departments=departments_list,
                         title="Департаменты")


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        astronaut_id = request.form.get('astronaut_id')
        astronaut_pass = request.form.get('astronaut_pass')
        captain_id = request.form.get('captain_id')
        captain_token = request.form.get('captain_token')


        return render_template('success.html',
                               title="Доступ разрешен",
                               message="Системы корабля разблокированы")

    return render_template('login.html', title="Авторизация")

@app.route('/distribution')
def distribution():
    astronauts = [
        "Ридли Скотт",
        "Энди Уир",
        "Марк Уотни",
        "Венката Капур",
        "Тедди Сандерс",
        "Шон Бин"
    ]
    return render_template('distribution.html',
                         astronauts=astronauts,
                         title="Размещение по каютам")


@app.route('/table')
def table():
    sex = request.args.get('sex', 'male').lower()
    age = int(request.args.get('age', 25))

    if sex == 'female':
        wall_color = '#ffb6c1'
    else:
        wall_color = '#87cefa'

    if age < 21:
        image = 'МаленькийМарсианин.jpg'
    else:
        image = 'БольшойМарсианин.jpg'

    return render_template('table.html',
                           title="Оформление каюты",
                           wall_color=wall_color,
                           image=image,
                           sex=sex.capitalize(),
                           age=age)


@app.route('/gallery', methods=['GET', 'POST'])
def gallery():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)

        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('gallery'))

    # Получаем список изображений из папки
    images = []
    for f in os.listdir(app.config['UPLOAD_FOLDER']):
        if f.rsplit('.', 1)[1].lower() in app.config['ALLOWED_EXTENSIONS']:
            images.append(f)

    return render_template('gallery.html', images=images)


if __name__ == '__main__':
    app.run(debug=True)