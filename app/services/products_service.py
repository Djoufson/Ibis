from app.models.weather_type import WeatherType
from app.models.product import Product
from app.utils.configure import db

def add_product(data) -> tuple[dict[str, str], int]:
    product_name = data.get('name')
    weather_type_id = data.get('weather_type_id')

    if not product_name or not weather_type_id:
        return {'error': 'Invalid input'}, 400

    weather_type = WeatherType.query.get(weather_type_id)

    if not weather_type:
        return {'error': 'Invalid Weather Type ID'}, 400

    new_product = Product(name=product_name, weather_type_id=weather_type_id)
    db.session.add(new_product)
    db.session.commit()

    return {'message': 'Product added successfully!'}, 201
