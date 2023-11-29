from app.utils.configure import app, db
from app.controllers.products_controller import *
from app.controllers.weather_type_controller import *
from app.controllers.advertisements_controller import *

if __name__ == '__main__':
    with app.app_context():
        db.create_all()

    app.run(debug=True)
