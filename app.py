from flask import Flask, render_template
from flask_bootstrap import Bootstrap
import datetime

#create the object of Flask
app  = Flask(__name__)

bootstrap = Bootstrap(app)

def get_forms():
    forms = [
        {
            "name": "Vladyslav",
            "surname": "Diakun",
            "dateborn": datetime.datetime(2000, 12, 14, 0, 0).strftime('%d/%m/%Y'),
            "group": "IPZ-31",
            "email": "vlad5dyakun@gmail.com",
            "coorp_email": "vladyslav.diakun.19@pnu.edu.ua"
        },
        {
            "name": "Danilo",
            "surname": "Golub",
            "dateborn": datetime.datetime(2001, 8, 31, 0, 0).strftime('%d/%m/%Y'),
            "group": "IPZ-41",
            "email": "getreadytofly4l@gmail.com",
            "coorp_email": "danilo.golub.18@pnu.edu.ua"
        },
        {
            "name": "Yaroslav",
            "surname": "Osadchiy",
            "dateborn": datetime.datetime(2000, 4, 11, 0, 0).strftime('%d/%m/%Y'),
            "group": "M-41",
            "email": "hatsunismov_forever@gmail.com",
            "coorp_email": "yaroslav.osadchiy.19@pnu.edu.ua"
        }
    ]
    return forms

def get_numbers():
    numbers = [9, -3, 12, -7, -2, -13, 27, 4, 0, 54]
    return numbers

#creating our routes
@app.route('/')
def index():
    data = "Main Page"
    title = "Опис навігаційного меню"
    return render_template('index.html', 
        data = data, 
        title = title
    )


@app.route('/task')
def task():
    data = "Tasks"
    title = "Завдання"
    return render_template('task.html', 
        data = data, 
        title = title
    )

@app.route('/if')
def if_statement():
    data = "If Statements"
    title = "Оператори If, elif, else"
    numbers = get_numbers()
    return render_template('if.html', 
        data = data,
        title = title, 
        numbers = numbers
    )

@app.route('/for')
def for_cycle():
    data = "For cycle"
    title = "Оператор циклу for"
    forms = get_forms()
    return render_template('for.html', 
        data = data,
        title = title, 
        forms = forms
    )

#run flask app
if __name__ == "__main__":
    app.run(debug=True)