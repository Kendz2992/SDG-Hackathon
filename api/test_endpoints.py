from datetime import datetime
from flask import Blueprint, jsonify, request

from . import db
from .models import Events, Sensors

test = Blueprint("test", __name__)


@test.route("/", methods=["GET"])
@test.route("/home", methods=["GET"])
@test.route("/index", methods=["GET"])
def home():
    time = datetime.now()
    sensors = Sensors.query.count()
    events = Events.query.count()
    return f"Welcome to SDG Hackathon @ {time}, there are {sensors} sensors and {events} events registered"


@test.route("/testg", methods=["GET"])
def test_get():
    return "Test GET endpoint, 200", 200


@test.route("/testp", methods=["POST"])
def test_post():
    return "Test POST endpoint, 201", 201
