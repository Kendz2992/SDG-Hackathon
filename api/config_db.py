from .models import Events, Sensors

START_SENSORS = [
    Sensors(location="over there", model="A-test", radius=5),
    Sensors(location="near here", model="B-Test", radius=6),
]

START_EVENTS = [
    Events(location="over there somewhere", event_type="Fire", sensor_id=1),
    Events(location="near here too", event_type="Police", sensor_id=2),
    Events(location="timbuktu", event_type="Test"),
]

SEED_LOCATIONS = [
    {
        "type": 1,
        "properties": {"name": "Saint Petersburg City Hall", "address": "175 5th St N, St. Petersburg, FL 33701",},
        "geometry": {"type": "Point", "coordinates": [27.773056, -82.64]},
    },
    {
        "type": 2,
        "properties": {"name": "Leslee Lake", "address": "Leslee Lake Dr N, St. Petersburg, FL 33713",},
        "geometry": {"type": "Point", "coordinates": [27.7963597, -82.6933985]},
    },
    {
        "type": 3,
        "properties": {"name": "Douglas L. Jamerson Elementary School", "address": "1200 37th St S, St. Petersburg, FL 33711",},
        "geometry": {"type": "Point", "coordinates": [27.758062, -82.682204]},
    },
]
