"""
API REST simples para consulta de dados climáticos.

Este script utiliza o Flask para criar um servidor web com um endpoint
que busca informações de clima em tempo real da API OpenWeatherMap.
"""

# --- Importação das Bibliotecas ---
import os
from flask import Flask, jsonify
import requests
from dotenv import load_dotenv

# --- Inicialização e Configuração ---
load_dotenv()

app = Flask(__name__)

# Pega a chave da API do ambiente pelo NOME da variável
API_KEY = '99ddf84a7d0a549eca0e62bd35caf314'
BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# --- Definição do Endpoint da API ---
@app.route('/weather/<string:city>', methods=['GET'])
def get_weather(city):
    # CORREÇÃO: A docstring fica DENTRO da função
    """
    Endpoint que retorna os dados do clima para uma cidade específica.

    :param city: O nome da cidade a ser consultada.
    :return: Um objeto JSON com os dados do clima ou uma mensagem de erro.
    """
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',
        'lang': 'pt_br'
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        weather_info = {
            "cidade": data['name'],
            "temperatura_celsius": data['main']['temp'],
            "condicao": data['weather'][0]['description'],
            "umidade_percentual": data['main']['humidity'],
            "velocidade_vento_kmh": round(data['wind']['speed'] * 3.6, 2)
        }
        
        return jsonify(weather_info)

    except requests.exceptions.HTTPError:
        if response.status_code == 404:
            return jsonify({"erro": "Cidade não encontrada"}), 404
        return jsonify({"erro": "Erro ao contatar a API de clima. Verifique a cidade ou sua chave de API."}), response.status_code
    
    except requests.exceptions.RequestException as e:
        return jsonify({"erro": f"Erro de conexão com o serviço externo: {e}"}), 503

# --- Bloco de Execução Principal ---
if __name__ == '__main__':
    app.run(debug=True)