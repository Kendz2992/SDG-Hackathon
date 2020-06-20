from datetime import datetime
from flask import Blueprint, jsonify, request

from __init__ import db

test = Blueprint("test", __name__)


@test.route("/", methods=["GET"])
@test.route("/home", methods=["GET"])
@test.route("/index", methods=["GET"])
def home():
    time = datetime.now()
    return f"Welcome to SDG Hackathon @ {time}"


@test.route("/testg", methods=["GET"])
def test_get():
    return "Test GET endpoint, 200", 200


@test.route("/testp", methods=["POST"])
def test_post():
    return "Test POST endpoint, 201", 201
