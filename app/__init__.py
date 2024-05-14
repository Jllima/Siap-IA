from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy
from config import Config

home_bp = Blueprint('home', __name__, url_prefix='/')
db = SQLAlchemy()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    
    from .home.routes import home_bp
    app.register_blueprint(home_bp)

    return app