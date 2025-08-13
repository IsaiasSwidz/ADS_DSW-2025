from flask import Flask, render_template, request

app = Flask(__name__)

tarefas = []

@app.route('/', methods= ['GET', 'POST'])
def index():
    if request.method == 'POST':
        tarefa = request.form.get('tarefa')
        datalimite = request.form.get('datalimite')

        tarefas.append({
            'tarefa': tarefa,
            'datalimite': datalimite
        })

        return render_template('sucesso.html', tarefa=tarefa, datalimite=datalimite)

    return render_template('index.html', tarefas=tarefas)


if __name__ == '__main__':
    app.run(debug=True)