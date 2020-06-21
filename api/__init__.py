from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import Config

db = SQLAlchemy()

# App config and connecting
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    from .models import Events, Sensors

    db.init_app(app)

    from .endpoints import event
    from .test_endpoints import test

    app.register_blueprint(event)
    app.register_blueprint(test)

    return app


def setup_db(db):

    # Setup db with base sensors and events
    from .config_db import START_EVENTS, START_SENSORS

    db.session.add_all(START_SENSORS)
    db.session.commit()
    db.session.add_all(START_EVENTS)
    db.session.commit()
