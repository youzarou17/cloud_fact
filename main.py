from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])  # Ajout de la route et des méthodes HTTP
def hello_world():
    """Responds to any HTTP request."""
    request_json = request.get_json(silent=True)
    if request_json and 'name' in request_json:
        name = request_json['name']
    else:
        name = 'World'
    return f'Hello {name}!'

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)