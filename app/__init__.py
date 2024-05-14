from flask import Flask, Blueprint

home_bp = Blueprint('home', __name__, url_prefix='/')

def create_app():
    app = Flask(__name__)
    
    from .home.routes import home_bp
    app.register_blueprint(home_bp)

    return app