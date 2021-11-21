from olddb import db
from olddb import User
from olddb import Assignment
from olddb import Course
from flask import Flask
import json
from flask import request

app = Flask(__name__)
db_filename = "cms.db"

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

# generalized response formats
def success_response(data, code=200):
    return json.dumps(data), code


def failure_response(message, code=404):
    return json.dumps({"error": message}), code

# Team related routes
@app.route("/api/teams/", methods=["GET"])
def get_teams():
    '''Get all teams.'''
    pass

@app.route("/api/teams/", methods=["POST"])
def create_team():
    '''Create new team with given name and password.'''
    pass

@app.route("/api/teams/<int:team_id>/", methods=["GET"])
def get_team(team_id):
    '''Get info about team with team_id.'''
    pass

@app.route("/api/teams/<int:team_id>/", methods=["DELETE"])
def delete_team(team_id):
    '''Delete team with team_id.'''
    pass


# Event related routes
@app.route("/api/events/", methods=["GET"])
def get_events():
    '''Get all events.'''
    pass

@app.route("/api/events/<int:team_id>/<int:event_id>", methods=["GET"])
def get_event(team_id, event_id):
    '''Get event with event_id from team_id team.'''
    pass

@app.route("/api/events/<int:team_id>/", methods=["POST"])
def post_event(team_id):
    '''Post new event to team_id team.'''
    pass

@app.route("/api/events/<int:team_id>/<int:event_id>", methods=["DELETE"])
def delete_event(team_id, event_id):
    '''Delete event with team_id.'''
    pass

@app.route("/api/events/<int:user_id>/", methods=["GET"])
def get_fav_events(user_id):
    '''Get all events associated with user with user_id.'''
    pass


# User related routes
@app.route("/api/users/<int:user_id>/", methods=["GET"])
def get_user(user_id):
    '''Get user with user_id.'''
    pass

@app.route("/api/users/", methods=["POST"])
def create_user():
    '''Create user with provided information.'''
    pass

@app.route("/api/users/<int:user_id>/favorites/", methods=["GET"])
def get_fav_teams(user_id):
    '''Get all favorite teams of user with user_id.'''

@app.route("/api/users/<int:user_id>/favorites/<int:team_id>/", methods=["POST"])
def add_fav_team(user_id, team_id):
    '''Add team with team_id to users favorite teams.'''

@app.route("/api/users/<int:user_id>/favorites/<int:team_id>/", methods=["DELETE"])
def remove_fav_team(user_id, team_id):
    '''Remove team with team_id from users favorite teams.'''

@app.route("/reset/")
def reset():
    db.drop_all()
    db.create_all()
    return success_response("yes")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
