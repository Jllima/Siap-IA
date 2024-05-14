from flask import Flask, Blueprint
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

home_bp = Blueprint('home', __name__, url_prefix='/')
chat_bp = Blueprint('chat', __name__, url_prefix='/chats')

db = SQLAlchemy()
migrate = Migrate()

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    
    from .home.routes import home_bp
    app.register_blueprint(home_bp)

    from .chats.routes import chat_bp
    app.register_blueprint(chat_bp)

    return app