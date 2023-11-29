from app.utils.configure import db

class WeatherType(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    type_name = db.Column(db.String(20), nullable=False)
