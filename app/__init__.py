# from flask import Flask
# from config import Config

# app = Flask(__name__)
# app.config.from_object(Config)

from flask import Flask
from app.routes import register_routes  # Adjusted import

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')

    register_routes(app)  # Register routes

    return app


