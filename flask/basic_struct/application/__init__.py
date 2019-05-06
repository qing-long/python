from flask import Flask
from config import config


def create_app(config=config['dev']):
    app = Flask(__name__)
    app.config.from_object(config)
    return app
