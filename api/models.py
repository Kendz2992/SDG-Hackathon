from datetime import datetime

from __init__ import db


class Sensor(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250))
    radius = db.Column(db.Integer)


class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(250), nullable=False)
    event_type = db.Column(db.String(250), nullable=False)
    created = db.Column(db.DateTime, nullable=False, default=datetime.now())
