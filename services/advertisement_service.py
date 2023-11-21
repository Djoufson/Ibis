from models.weather_type import WeatherType
from models.product import Product
from openai_service import generate_openai_advertisement
import random

def generate_advertisement(weather_id:int) -> tuple[dict[str, str], int]:
    weather_type = WeatherType.query.get(weather_id)

    if not weather_type:
        return {'error': 'Invalid Weather Type ID'}, 400

    products = Product.query.filter_by(weather_type_id=weather_id).all()

    if not products:
        return {'error': 'No product found for this weather'}, 404

    chosen_product = random.choice(products)
    prompt = f'Introducing our {chosen_product.name} for {weather_type.type_name} weather!'
    advertisement_text = generate_openai_advertisement(prompt)

    return chosen_product.name, advertisement_text
