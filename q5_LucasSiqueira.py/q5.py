#Implementação da aplicação de ajustar os valores RGB
from flask import Flask, request, jsonify
import random

app = Flask(__name__)

generate_random_rgb = lambda: (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

get_rgb_str = lambda rgb: f"RGB atual: {rgb}"

validate_and_adjust = lambda r, g, b: jsonify({
    'message': get_rgb_str((r, g, b)),
    'rgb': (r, g, b),
}) if all(isinstance(x, int) and 0 <= x <= 255 for x in [r, g, b]) else jsonify({'error': 'Invalid RGB values provided'}), 400

app.add_url_rule('/', 'index', lambda: jsonify({
    'message': get_rgb_str(generate_random_rgb()),
    'prompt': 'Você gostaria de ajustar os valores RGB? (Use /adjust endpoint)'
}), methods=['GET'])

app.add_url_rule('/adjust', 'adjust', lambda: validate_and_adjust(
    request.json.get('red', 0),
    request.json.get('green', 0),
    request.json.get('blue', 0)
), methods=['POST'])

app_run_lambda = lambda: app.run(debug=True)
app_run_lambda()
