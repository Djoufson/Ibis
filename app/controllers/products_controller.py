from flask import request, jsonify, render_template
from app.utils.configure import app
from app.services.products_service import add_product

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/products', methods=['POST'])
def add_product_route():
    data = request.get_json()
    result = add_product(data)
    return jsonify(result)
