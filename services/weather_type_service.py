from models.weather_type import WeatherType
from utils.configure import db

def add_weather(data) -> tuple[dict[str, str], int]:
    weather_type_name = data.get('name')

    if not weather_type_name:
        return {'error': 'Invalid input'}, 400

    new_weather_type = WeatherType(type_name=weather_type_name)
    db.session.add(new_weather_type)
    db.session.commit()

    return {'message': 'Weather Type added successfully!'}, 201
