from .models import Events, Sensors

SEED_LOCATIONS = [
    {
        "type": 1,
        "properties": {
            "name": "Saint Petersburg City Hall",
            "address": "175 5th St N, St. Petersburg, FL 33701",
        },
        "geometry": {"type": "Point", "coordinates": [27.773056, -82.64]},
    },
    {
        "type": 2,
        "properties": {
            "name": "Leslee Lake",
            "address": "Leslee Lake Dr N, St. Petersburg, FL 33713",
        },
        "geometry": {"type": "Point", "coordinates": [27.7963597, -82.6933985]},
    },
    {
        "type": 3,
        "properties": {
            "name": "Douglas L. Jamerson Elementary School",
            "address": "1200 37th St S, St. Petersburg, FL 33711",
        },
        "geometry": {"type": "Point", "coordinates": [27.758062, -82.682204]},
    },
]

START_SENSORS = [
    Sensors(location=SEED_LOCATIONS[0], model="A-test", radius=5),
    Sensors(location=SEED_LOCATIONS[1], model="B-Test", radius=6),
    Sensors(location=SEED_LOCATIONS[2], model="C-Test", radius=7),
]

START_EVENTS = [
    Events(event_type="Fire", sensor_id=1),
    Events(event_type="Police", sensor_id=2),
    Events(
        location={
            "type": 3,
            "properties": {
                "name": "Douglas L. Jamerson Elementary School",
                "address": "1200 37th St S, St. Petersburg, FL 33711",
            },
            "geometry": {"type": "Point", "coordinates": [27.758062, -82.682204]},
        },
        event_type="Test",
    ),
]
