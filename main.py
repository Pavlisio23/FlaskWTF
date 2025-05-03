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

if __name__ == '__main__':
    app.run(debug=True)