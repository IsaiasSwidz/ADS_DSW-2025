from flask import Flask, render_template, flash, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo

app = Flask(__name__)

app.config['SECRET_KEY'] = 'uma_chave_de_segurança_muito_dificil'

class MeuFormulario(FlaskForm):
    nome = StringField('Nome completo', validators=[DataRequired(message='Campo obrigatório, man')])
    email = StringField('E-Mail', validators=[
        DataRequired(message='Campo Obrigatória, garai.'),
        Email(message='Coloca logo um E-Mail válido, truta.')
    ])
    submit = SubmitField("Enviar")

class RegistroForm(FlaskForm):
    nome = StringField('Nome completo', validators=[DataRequired(message='Campo obrigatório, man')])
    email = StringField('E-Mail', validators=[
        DataRequired(message='Campo Obrigatória, garai.'),
        Email(message='Coloca logo um E-Mail válido, truta.')
    ])
    senha = PasswordField('Senha', validators=[
        DataRequired(message='Campo obrigatório'),
        Length(min=8, message='A senha deve ter pelo menos 8 caracteres'),
    ])
    confirmar_senha = PasswordField('Confirmar Senha', validators=[
        DataRequired(message='Campo obrigatório'),
        EqualTo('senha', message='As senhas devem ser idênticas'),
    ])
    biografia = TextAreaField('Biografia (opcional)')
    aceitar_termos = BooleanField('Aceito os termos de serviço', validators=[
        DataRequired(message='Você deve aceitar os termos para continuar')
    ])
    submit = SubmitField('Registrar')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/formulario', methods=['POST', 'GET'])
def formulario():
    form = MeuFormulario()
    if form.validate_on_submit():
        nome_usuario = form.nome.data
        email_usuario = form.email.data
        flash(f'Cadastro Recebido para {nome_usuario} e {email_usuario}')
        return redirect(url_for('formulario'))
    return render_template('formulario.html', form=form)

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    form = RegistroForm()
    if form.validate_on_submit():
        # Aqui você faria o persist (db) ou outra lógica de negócio
        flash(f'Registro concluído para {form.nome.data} ({form.email.data})!')
        return redirect(url_for('registro'))
    return render_template('registro.html', form=form)


if __name__ == '__main__':
    app.run(debug=True)