# Class holds all necessary configs for Flask app


class Config(object):

    # Flask
    FLASK_APP = "__init__.py"
    FLASK_DEBUG = 1

    # SQL DB
    SQLALCHEMY_DATABASE_URI = "sqlite:///api.db"
    SQLALCHEMY_ECHO = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
