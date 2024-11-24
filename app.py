from flask import Flask, render_template, request, redirect, url_for, flash
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta'  # Necessário para utilizar flash messages

# Dados simulados para o histórico de programações
programacoes = [
    {
        'data': datetime(2024, 11, 17),
        'titulo': 'Culto de Ação de Graças',
        'descricao': 'Culto especial para agradecer as bênçãos recebidas durante o ano.',
        'diretor': 'Pr. João Silva'
    },
    {
        'data': datetime(2024, 11, 10),
        'titulo': 'Culto de Louvor',
        'descricao': 'Uma noite dedicada ao louvor e adoração.',
        'diretor': 'Ministério de Música'
    },
    # Adicione mais programações conforme necessário
]

@app.route('/')
def index():
    return render_template('index.html', programacoes=programacoes)

@app.route('/agendar', methods=['GET', 'POST'])
def agendar():
    if request.method == 'POST':
        titulo = request.form['titulo']
        descricao = request.form['descricao']
        data_str = request.form['data']
        diretor = request.form['diretor']

        # Validação simples dos campos
        if not titulo or not descricao or not data_str or not diretor:
            flash('Todos os campos são obrigatórios.', 'error')
            return redirect(url_for('agendar'))

        try:
            data = datetime.strptime(data_str, '%Y-%m-%d')
        except ValueError:
            flash('Data inválida. Use o formato AAAA-MM-DD.', 'error')
            return redirect(url_for('agendar'))

        # Adiciona a nova programação à lista (simulação)
        nova_programacao = {
            'data': data,
            'titulo': titulo,
            'descricao': descricao,
            'diretor': diretor
        }
        programacoes.append(nova_programacao)
        flash('Programação agendada com sucesso!', 'success')
        return redirect(url_for('index'))

    return render_template('agendar.html')

if __name__ == '__main__':
    app.run(debug=True)
