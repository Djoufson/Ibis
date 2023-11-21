from flask import jsonify
from utils.configure import app
from services.openai_service import generate_openai_advertisement

@app.route('/advertisements/<int:weather_id>/<int:max_tokens>', methods=['GET'])
def get_advertisement(weather_id, max_tokens):
    product, advertisement_text = generate_openai_advertisement(weather_id, max_tokens)
    return jsonify({'product': product, 'advertisement_text': advertisement_text})
