from flask import Flask
from dotenv import load_dotenv

load_dotenv()

def create_app():
    from .routes import api
    app = Flask(__name__)
    app.register_blueprint(api)
    return app