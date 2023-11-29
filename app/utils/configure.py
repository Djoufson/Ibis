from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Configure SQLite database
def configure_database(app:Flask) -> tuple[Flask, SQLAlchemy]:
    db = SQLAlchemy(app)
    return db

def configure_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
    return app

app = configure_app()
db = configure_database(app)
