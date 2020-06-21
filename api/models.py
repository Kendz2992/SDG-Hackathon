from dataclasses import dataclass
from datetime import datetime

from . import db


class Sensors(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(250), nullable=False)
    model = db.Column(db.String(250))
    radius = db.Column(db.Integer)

    def __repr__(self):
        return f"<Sensor {self.id}-{self.location}>"


@dataclass
class Events(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String(250), nullable=False)
    event_type = db.Column(db.String(250), nullable=False)
    sensor_id = db.Column(db.Integer)

    def __repr__(self):
        return f"<Event {self.id}-{self.event_type}-{self.location}>"
