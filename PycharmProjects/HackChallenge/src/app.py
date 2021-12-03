from db import db
from db import Fan
from db import Team
from db import Event
import os
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
    if not body.get("name") or not body.get("password") or not body.get("sport") or not body.get("gender"):
        return failure_response("not all fields were provided!", 400)
    new_team = Team(name=body.get("name"), password=body.get("password"), sport = body.get("sport"), gender = body.get("gender"))
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
        return failure_response("Team not found!")
    body = json.loads(request.data)
    if not body.get("name") or not body.get("password"):
        return failure_response("please provide both team name and password!", 400)
    if body.get("name") != team.name or body.get("password") != team.password:
        return failure_response("incorrect team name or password!", 403)
    db.session.delete(team)
    db.session.commit()
    return success_response(team.serialize())


# Event related routes
@app.route("/api/events/", methods=["GET"])
def get_events():
    '''Get all events.'''
    return success_response(
        {"events": sorted([e.serialize() for e in Event.query.all()], key=lambda ev: ev["unixTime"])}
    )

@app.route("/api/events/<int:event_id>/", methods=["GET"])
def get_event(event_id):
    '''Get event with event_id from team_id team.'''
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return failure_response("Event not found!")
    return success_response(event.serialize())

@app.route("/api/events/", methods=["POST"])
def post_event():
    '''Post new event.'''
    body = json.loads(request.data)
    # if not body.get("name") or not body.get("password") or not body.get("description") or not body.get("opponent") or not body.get("unixTime") or not body.get("location") or not body.get("title") or not body.get("team_id"):
    #     return failure_response("not all fields were provided!", 400)
    team = Team.query.filter_by(id=body.get("team_id")).first()
    if not team:
        return failure_response("Team not found!")
    if body.get("name") != team.name or body.get("password") != team.password:
        return failure_response("incorrect team name or password!", 403)
    new_event = Event(title=body.get("title"), opponent=body.get("opponent"), location=body.get("location"), description=body.get("description"), unixTime=body.get("unixTime"), score=body.get("score", "-"), win=body.get("win", ""), team_id=body.get("team_id"))
    db.session.add(new_event)
    db.session.commit()
    return success_response(new_event.serialize(), 201)

@app.route("/api/events/<int:event_id>/", methods=["POST"])
def update_specific_event():
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return failure_response("Event not found!")
    team = Team.query.filter_by(id=event.team_id).first()
    if not body.get("name") or not body.get("password"):
        return failure_response("please provide both team name and password!", 400)
    if body.get("name") != team.name or body.get("password") != team.password:
        return failure_response("incorrect team name or password!", 403)
    event.score = body.get("score", event.score)
    event.won = body.get("won", event.won)
    event.title = body.get("title", event.title)
    event.description = body.get("description", event.description)
    event.opponent = body.get("opponent"), event.opponent
    event.unixTime = body.get("unixTime", event.unixTime)
    event.location = body.get("location", event.location)
    db.session.commit()
    return success_response(event.serialize())

@app.route("/api/events/<int:event_id>/", methods=["DELETE"])
def delete_event(event_id):
    '''Delete event with event_id.'''
    event = Event.query.filter_by(id=event_id).first()
    if event is None:
        return failure_response("Event not found!")
    team = Team.query.filter_by(id=event.team_id).first()
    body = json.loads(request.data)
    if not body.get("name") or not body.get("password"):
        return failure_response("please provide both team name and password!", 400)
    if body.get("name") != team.name or body.get("password") != team.password:
        return failure_response("incorrect team name or password!", 403)
    db.session.delete(event)
    db.session.commit()
    return success_response(event.serialize())

@app.route("/api/events/users/<int:user_id>/", methods=["GET"])
def get_fav_events(user_id):
    '''Get all events associated with user_id.'''
    body = json.loads(request.data)
    if not body.get("username") or not body.get("password"):
        return failure_response("not all fields were provided!", 400)
    user = Fan.query.filter_by(id=user_id).first()
    if user is None:
        return failure_response("User not found!")
    if body.get("username") != user.username or body.get("password") != user.password:
        return failure_response("incorrect team name or password!", 403)
    teams = set([team["id"] for team in user.serialize()["favorite_teams"]])
    fav_events = list(filter(lambda event: event["team"]["id"] in teams, [e.serialize() for e in Event.query.all()]))
    return success_response({"events": sorted(fav_events, key=lambda ev: ev["unixTime"])})

# User related routes
@app.route("/api/users/<int:user_id>/", methods=["GET"])
def get_user(user_id):
    '''Get user with user_id.'''
    user = Fan.query.filter_by(id=user_id).first()
    if user is None:
        return failure_response("User not found!")
    return success_response(user.serialize())

@app.route("/api/users/", methods=["POST"])
def create_user():
    '''Create user with provided information.'''
    body = json.loads(request.data)
    if not body.get("username") or not body.get("password"):
        return failure_response("not all fields were provided!", 400)
    new_user = Fan(username=body.get("username"), password=body.get("password"))
    db.session.add(new_user)
    db.session.commit()
    return success_response(new_user.serialize(), 201)

@app.route("/api/users/<int:user_id>/favorites/<int:team_id>/", methods=["POST"])
def add_fav_team(user_id, team_id):
    '''Add team with team_id to users favorite teams.'''
    fan = Fan.query.filter_by(id=user_id).first()
    team = Team.query.filter_by(id=team_id).first()
    body = json.loads(request.data)
    if not fan:
        return failure_response("Fan not found!")
    if not team:
        return failure_response("Team not found!")
    if body.get("username") != fan.username or body.get("password") != fan.password:
        return failure_response("incorrect fan username or password!", 403)
    for t in fan.favorite_teams:
        if t.id == team.id:
            return failure_response("Team already in Favorites!", 403)
    fan.favorite_teams.append(team)
    db.session.commit()
    return success_response(team.serialize(), 201)

@app.route("/api/users/<int:user_id>/remove/<int:team_id>/", methods=["POST"])
def remove_fav_team(user_id, team_id):
    '''Remove team with team_id from users favorite teams.'''
    fan = Fan.query.filter_by(id=user_id).first()
    team = Team.query.filter_by(id=team_id).first()
    body = json.loads(request.data)
    if not fan:
        return failure_response("Fan not found!")
    if not team:
        return failure_response("Team not found!")
    if body.get("username") != fan.username or body.get("password") != fan.password:
        return failure_response("incorrect fan username or password!", 403)
    for t in fan.favorite_teams:
        if t.id == team.id:
            fan.favorite_teams.remove(team)
            db.session.commit()
            return success_response(team.serialize(), 201)
    return failure_response("Team already non-favorite!", 403)

@app.route("/reset/", methods=["POST"])
def reset():
    db.drop_all()
    db.create_all()
    return success_response("yes")

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
