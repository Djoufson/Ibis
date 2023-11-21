from flask import request, jsonify
from utils.configure import app
from services.products_service import add_product

@app.route('/products', methods=['POST'])
def add_product_route():
    data = request.get_json()
    result = add_product(data)
    return jsonify(result)
