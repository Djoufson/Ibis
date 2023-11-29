from flask import jsonify
from app.utils.configure import app
from app.services.advertisement_service import generate_advertisement

@app.route('/advertisements/<int:weather_id>/<int:max_tokens>', methods=['GET'])
def get_advertisement(weather_id, max_tokens):
    product, advertisement_text = generate_advertisement(weather_id, max_tokens)
    return jsonify({'product': product, 'advertisement_text': advertisement_text})
