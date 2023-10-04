from flask import Flask, jsonify, request
import random
import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Dados iniciais de consumo de energia
energia_atual = 1000  # Em watts
data_hora_inicial = datetime.datetime.now()

@app.route('/')
def index():
    return "API Simulador de Consumo de Energia"

@app.route('/consumo', methods=['GET', 'POST'])
def consumo():
    global energia_atual
    global data_hora_inicial

    if request.method == 'POST':
        dados = request.get_json()
        consumo_atual = dados['consumo']
        energia_atual += consumo_atual

    data_hora_atual = datetime.datetime.now()
    tempo_decorrido = (data_hora_atual - data_hora_inicial).total_seconds() / 60  # Em minutos

    # Simula o consumo de energia a cada minuto
    consumo_por_minuto = random.randint(1, 10)  # Geração de consumo aleatório
    energia_atual += consumo_por_minuto

    resposta = {
        "energia_consumida": energia_atual,
        "tempo_decorrido": tempo_decorrido
    }

    return jsonify(resposta)

if __name__ == '__main__':
    app.run(debug=True)
