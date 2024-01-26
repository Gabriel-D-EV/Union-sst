from flask import Flask, render_template, redirect, request, flash
from flask_mail import Mail, Message
from datetime import datetime
from config import email, senha

app = Flask(__name__)
app.secret_key = "gabrieldev"

mail_config = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": email,
    "MAIL_PASSWORD": senha,
}

app.config.update(mail_config)
mail = Mail(app)

class Contato:
    def __init__(self, nome, email, mensagem):
        self.nome = nome
        self.email = email
        self.mensagem = mensagem
        
    

hj = datetime.now()
ano = hj.year

@app.route('/')
def index():
    return render_template('index.html', ano=ano)

@app.route('/send', methods=['GET', 'POST'])
def send():
    if request.method == 'POST':
        formContato = Contato(
            request.form["nome"],
            request.form["email"],
            request.form["mensagem"]
        )
        
        msg = Message(
            subject= f'Cliente {formContato.nome} te enviou uma mensagem do Union.sst',
            sender=email,
            recipients= ['gabriel.silva_dev@outlook.com', 'Unionsst@gmail.com', 'pedroraphbass@gmail.com'],
            body= f'''
            
                Assunto: Solicitação do Cliente

                Olá, 

                Recebi uma mensagem de cliente. Aqui estão os detalhes:

                Nome: {formContato.nome}
                Email: {formContato.email}

                Mensagem:
                {formContato.mensagem}

                Atenciosamente,
                Admin
                '''
        )
        
        mail.send(msg)
        flash('Mensagem enviada com sucesso!')
    
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True)
