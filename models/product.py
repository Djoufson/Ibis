from utils.configure import db

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    weather_type_id = db.Column(db.Integer, db.ForeignKey('weather_type.id'), nullable=False)
    weather_type = db.relationship('WeatherType', backref=db.backref('products', lazy=True))
