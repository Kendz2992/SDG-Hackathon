# SDG-Hackathon
This is a Suncoast Developers Guild Hackathon project started 6/19/2020

To run this local out of the repo
- cd to top folder of repo
- Install pipenv via `brew install pipenv` or similar commands
- `pipenv shell`
- `export FLASK_APP=api`
- `export FLASK_DEBUG=True`
- Open up a python idle with `python`
- `from api.models import Events, Sensors`
- `from api import db, create_app, setup_db`
- `db.create_all(app=create_app())`
- Exit python idle with `exit()`
- Back in env shell, use `flask run`
- This should start a local version of the project
- Use Postman to add/POST new sensors and events

Some resources we used to create this project
- https://developer.okta.com/blog/2018/12/20/crud-app-with-python-flask-react
- https://blog.miguelgrinberg.com/post/how-to-create-a-react--flask-project
- https://www.youtube.com/watch?v=Urx8Kj00zsI part 1
- https://www.youtube.com/watch?v=06pWsB_hoD4 part 2
