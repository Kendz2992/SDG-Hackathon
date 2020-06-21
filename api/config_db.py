from .models import Events, Sensors

START_SENSORS = [
    Sensors(location="over there", model="A-test", radius=5),
    Sensors(location="near here", model="B-Test", radius=6)
]

START_EVENTS = [
    Events(location="over there somewhere", event_type="Fire", sensor_id=1),
    Events(location="near here too", event_type="Police", sensor_id=2),
    Events(location="timbuktu", event_type="Test")
]