from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'chave_secreta_para_flash_messages'  # Necessário para usar flash messages

@app.route('/nova-receita', methods=['GET', 'POST'])
def nova_receita():
    if request.method == 'POST':
        # Capturar dados do formulário
        nome = request.form.get('nome')
        ingredientes = request.form.get('ingredientes')
        modo_preparo = request.form.get('modo_preparo')
        
        # Validação dos campos
        if not nome or not ingredientes or not modo_preparo:
            flash('Erro: Todos os campos são obrigatórios!', 'error')
            return redirect(url_for('nova_receita'))
        
        # Redirecionar para a página de receita criada com os dados
        return redirect(url_for('receita_criada', 
                              nome=nome, 
                              ingredientes=ingredientes, 
                              modo_preparo=modo_preparo))
    
    return render_template('receita.html')

@app.route('/receita-criada')
def receita_criada():
    nome = request.args.get('nome')
    ingredientes = request.args.get('ingredientes')
    modo_preparo = request.args.get('modo_preparo')
    return render_template('receita_criada.html', 
                          nome=nome, 
                          ingredientes=ingredientes, 
                          modo_preparo=modo_preparo)

if __name__ == '__main__':
    app.run(debug=True)