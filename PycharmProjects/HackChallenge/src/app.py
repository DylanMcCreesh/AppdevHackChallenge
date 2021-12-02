from db import db
from db import Fan
from db import Team
from db import Event
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
    return success_response(
        {"teams": [t.serialize() for t in Team.query.all()]}
    )

@app.route("/api/teams/", methods=["POST"])
def create_team():
    '''Create new team with given name and password.'''
    body = json.loads(request.data)
    if not body.get("name") or not body.get("password"):
        return failure_response("not all fields were provided!", 400)
    new_team = Team(name=body.get("name"), password=body.get("password"))
    db.session.add(new_team)
    db.session.commit()
    return success_response(new_team.serialize(), 201)

@app.route("/api/teams/<int:team_id>/", methods=["GET"])
def get_team(team_id):
    '''Get info about team with team_id.'''
    team = Team.query.filter_by(id=team_id).first()
    if team is None:
        return failure_response("Team not found!")
    return success_response(team.serialize())


@app.route("/api/teams/<int:team_id>/", methods=["DELETE"])
def delete_team(team_id):
    '''Delete team with team_id.'''
    team = Team.query.filter_by(id=team_id).first()
    if team is None:
        return failure_response("Course not found!")
    body = json.loads(request.data)
    if not body.get("name") or not body.get("password"):
        return failure_response("please provide both team name and password!", 400)
    if body.get("name") != team.name or  body.get("password") != team.password:
        return failure_response("incorrect team name or password!", 400)
    db.session.delete(team)
    db.session.commit()
    return success_response(team.serialize())


# Event related routes
@app.route("/api/events/", methods=["GET"])
def get_events():
    '''Get all events.'''
    return success_response(
        {"events": [e.sub_serialize() for e in Event.query.all()]}
    )

@app.route("/api/events/<int:team_id>/<int:event_id>", methods=["GET"])
def get_event(team_id, event_id):
    '''Get event with event_id from team_id team.'''
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return failure_response("Event not found!")
    if event.team_id != team_id:
        return failure_response("Event not for this team!")
    return success_response(event.sub_serialize())

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
    pass

@app.route("/api/users/<int:user_id>/favorites/<int:team_id>/", methods=["POST"])
def add_fav_team(user_id, team_id):
    '''Add team with team_id to users favorite teams.'''
    pass

@app.route("/api/users/<int:user_id>/favorites/<int:team_id>/", methods=["DELETE"])
def remove_fav_team(user_id, team_id):
    '''Remove team with team_id from users favorite teams.'''
    pass

@app.route("/reset/", methods=["POST"])
def reset():
    db.drop_all()
    db.create_all()
    return success_response("yes")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
