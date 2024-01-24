from flask import Flask, render_template, redirect
from flask_mail import Mail, Message
from datetime import datetime


app = Flask(__name__)

hj = datetime.now()
ano = hj.year

@app.route('/')
def index():
    return render_template('index.html', ano=ano)




if __name__ == '__main__':
    app.run(debug=True)
