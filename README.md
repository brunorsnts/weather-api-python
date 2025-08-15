# Weather API com Flask

![Linguagem](https://img.shields.io/badge/Python-3.12-blue?style=for-the-badge&logo=python)
![Framework](https://img.shields.io/badge/Flask-3.0-black?style=for-the-badge&logo=flask)
![Licença](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)

## 📄 Descrição

**Weather API** é uma API REST simples, desenvolvida em Python com o micro-framework Flask. Seu objetivo é fornecer informações climáticas em tempo real para qualquer cidade do mundo. A API atua como um wrapper, consumindo os dados do serviço externo [OpenWeatherMap](https://openweathermap.org/api) e os reformatando em uma resposta JSON limpa e concisa.

Este projeto foi criado como um exercício prático para demonstrar habilidades fundamentais em desenvolvimento de backend, incluindo criação de APIs REST, consumo de serviços de terceiros, gerenciamento de dependências e segurança de chaves de API.

## ✨ Funcionalidades

- **Endpoint único** para consulta de dados climáticos por nome da cidade.
- **Resposta em formato JSON** contendo informações essenciais: cidade, temperatura, condição, umidade e velocidade do vento.
- **Segurança:** As chaves de API são gerenciadas de forma segura através de variáveis de ambiente com o uso de um arquivo `.env`.
- **Tratamento de Erros:** Respostas claras para erros comuns, como cidades não encontradas (404).

## 🛠️ Tecnologias Utilizadas

- **Python 3.12**
- **Flask** (para a criação do servidor e da API)
- **Requests** (para fazer as chamadas HTTP à API externa)
- **python-dotenv** (para gerenciamento de variáveis de ambiente)
- **OpenWeatherMap API** (como fonte dos dados climáticos)
- **Ambiente Virtual (`venv`)** (para isolamento de dependências)

## ⚙️ Configuração e Instalação

Siga os passos abaixo para executar o projeto localmente.

### Pré-requisitos

- **Python 3.10+**
- **Git**

### Passos

1.  **Clone o repositório:**
    ```bash
    git clone https://github.com/brunorsnts/weather-api-python.git
    cd python-flask-weather-api
    ```

2.  **Crie e ative o ambiente virtual:**
    *Primeiro, crie o ambiente. No Windows, você pode precisar usar `python` ou `py` em vez de `python3`.*
    ```bash
    python3 -m venv venv
    ```
    *Agora, ative o ambiente:*
    ```bash
    # No Linux ou macOS
    source venv/bin/activate

    # No Windows (CMD ou PowerShell)
    .\venv\Scripts\activate
    ```

3.  **Instale as dependências:**
    O arquivo `requirements.txt` contém todas as bibliotecas necessárias.
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure a Chave de API:**
    - Crie um arquivo chamado `.env` na raiz do projeto.
    - Dentro dele, adicione sua chave da OpenWeatherMap no seguinte formato:
      ```
      OPENWEATHER_API_KEY=sua_chave_secreta_aqui
      ```

## 🚀 Como Executar

Com o ambiente virtual ativado e o arquivo `.env` configurado, inicie o servidor Flask com o seguinte comando:

```bash
# No Windows, use 'python' se 'python3' não for encontrado
python3 app.py

O servidor estará disponível em http://127.0.0.1:5000.

📡 Documentação da API

GET /weather/<cidade>

Retorna os dados climáticos atuais para a cidade especificada.

    Parâmetro de URL:

        cidade (string, obrigatório): O nome da cidade para a consulta.

Exemplo de Requisição de Sucesso

Requisição:
GET http://127.0.0.1:5000/weather/london

Resposta (200 OK):
JSON

{
  "cidade": "London",
  "temperatura_celsius": 15.1,
  "condicao": "nuvens dispersas",
  "umidade_percentual": 77,
  "velocidade_vento_kmh": 5.54
}


📜 Licença

Este projeto está sob a licença MIT.

👨‍💻 Autor

Feito por Bruno Rodrigues

    GitHub: @brunorsnts