from flask import Flask, render_template, request

app = Flask(__name__)

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

if __name__ == '__main__':
    app.run(debug=True)