from datetime import datetime
from flask import Blueprint, jsonify, request

from __init__ import db
from models import Event, Sensor

event = Blueprint("event", __name__)


@event.route("/events", methods=["GET"])
def get_events():
    events = Event.query.all()
    events_dict = [event.__dict__ for event in events]

    return jsonify({"events": events_dict}), 200


@event.route("/events/latest", methods=["GET"])
def get_recent_events():
    time = datetime.estnow()

    events = Event.query.all()
    events_dict = [event.__dict__ for event in events]

    return jsonify({"events": events_dict}), 200


@event.route("/events", methods=["POST"])
def post_events():
    event = request.get_json()
    new_event = Event(**event)

    db.session.add(new_event)
    db.session.commit()

    return jsonify({"added": event}), 201
