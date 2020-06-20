from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

from config import Config

db = SQLAlchemy()

# App config and connecting
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    import models

    db.init_app(app)
    # db.create_all()

    from endpoints import event
    from test_endpoints import test

    app.register_blueprint(event)
    app.register_blueprint(test)

    return app


if __name__ == "__main__":
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get("PORT", 5000))
    app = create_app()
    app.run(host="0.0.0.0", port=port)
