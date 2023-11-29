from app.utils.configure import app
from app.services.weather_type_service import add_weather
from flask import request, jsonify

@app.route('/weather_types', methods=['POST'])
def add_weather_type():
    data = request.get_json()
    result = add_weather(data)
    return jsonify(result)
