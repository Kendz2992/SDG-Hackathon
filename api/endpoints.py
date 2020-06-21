from datetime import datetime, timedelta
from flask import Blueprint, jsonify, request

from . import db
from .models import Events, Sensors

event = Blueprint("event", __name__)


@event.route("/events", methods=["GET"])
def get_events():
    event_query = Events.query.all()
    events = []

    for event in event_query:
        events.append(
            {
                "id": event.id,
                "location": event.location,
                "type": event.event_type,
                "sensor_id": event.sensor_id,
                "created": event.created,
            }
        )

    return jsonify({"events": events}), 200


@event.route("/events/latest", methods=["GET"])
def get_recent_events():
    time = datetime.now()

    event_query = Events.query[-5:]
    event_query = Events.query.filter(
        Events.created > (datetime.now() - timedelta(minutes=2))
    ).all()
    events = []

    for event in event_query:
        events.append(
            {
                "id": event.id,
                "location": event.location,
                "type": event.event_type,
                "sensor_id": event.sensor_id,
                "created": f"{time - event.created} ago",
            }
        )

    return jsonify({"events": events}), 200


@event.route("/events", methods=["POST"])
def post_events():
    event = request.get_json()

    if "sensor_id" in event:
        event["location"] = Sensors.query.get(event["sensor_id"]).location
    new_event = Events(**event)

    db.session.add(new_event)
    db.session.commit()

    return jsonify({"added": event}), 201


@event.route("/sensors", methods=["GET"])
def get_sensors():
    sensor_query = Sensors.query.all()
    sensors = []

    for sensor in sensor_query:
        sensors.append(
            {
                "id": sensor.id,
                "location": sensor.location,
                "model": sensor.model,
                "radius": sensor.radius,
            }
        )

    return jsonify({"sensors": sensors}), 200


@event.route("/sensors", methods=["POST"])
def post_sensors():
    sensor = request.get_json()
    new_sensor = Sensors(**sensor)

    db.session.add(new_sensor)
    db.session.commit()

    return jsonify({"added": sensor}), 201
