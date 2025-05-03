from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    title = "Марсианская миссия"
    return render_template('base.html', title=title)

@app.route('/training/<prof>')
def training(prof):
    return render_template('training.html', prof=prof, title="Тренировки")

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
    return render_template('list_prof.html', list_type=list_type, professions=professions)


if __name__ == '__main__':
    app.run(debug=True)