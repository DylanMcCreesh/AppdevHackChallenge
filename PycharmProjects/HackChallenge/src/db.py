from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

# your classes here
association_table = db.Table(
    "Association",
    db.Model.metadata,
    db.Column("team_id", db.Integer, db.ForeignKey("team.id")),
    db.Column("fan_id", db.Integer, db.ForeignKey("fan.id")),
)

class Fan(db.Model):
    __tablename__ = "fan"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    favorite_teams = db.relationship(
        "Team", secondary=association_table, back_populates="fans"
    )

    def __init__(self, **kwargs):
        self.username = kwargs.get("username")
        self.password = kwargs.get("password")

    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "favorite_teams": [t.serialize() for t in self.favorite_teams]
        }

class Team(db.Model):
    __tablename__ = "team"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    gender = db.Column(db.String, nullable=True)
    sport = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable=False)
    events = db.relationship("Event", cascade="delete")
    fans = db.relationship(
        "Fan", secondary=association_table, back_populates="favorite_teams"
    )

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.password = kwargs.get("password")
        self.gender = kwargs.get("gender")
        self.sport = kwargs.get("sport")


    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "sport": self.sport,
            "events": sorted([e.sub_serialize() for e in self.events], key= lambda ev: ev["unixTime"])
        }

    def sub_serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "gender": self.gender,
            "sport": self.sport,
        }

class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    unixTime = db.Column(db.Integer, nullable=False)
    location = db.Column(db.String, nullable=False)
    opponent = db.Column(db.String, nullable=False)
    score = db.Column(db.String, nullable=True)
    win = db.Column(db.Integer, nullable=True)
    team_id = db.Column(db.Integer, db.ForeignKey("team.id"))

    def __init__(self, **kwargs):
        self.title = kwargs.get("title")
        self.unixTime = kwargs.get("unixTime")
        self.location = kwargs.get("location")
        self.description = kwargs.get("description")
        self.opponent = kwargs.get("opponent")
        self.win = kwargs.get("win")
        self.score = kwargs.get("score", "-")
        self.team_id = kwargs.get("team_id")

    def serialize(self):
        wonString = ""
        if self.win == 0:
            wonString = "W"
        if self.win == 1:
            wonString = "L"
        if self.win == 2:
            wonString = "T"
        team = Team.query.filter_by(id=self.team_id).first()
        return {
            "id": self.id,
            "title": self.title,
            "unixTime": self.unixTime,
            "location": self.location,
            "date": datetime.fromtimestamp(self.unixTime).date(),
            "time": datetime.fromtimestamp(self.unixTime).time(),
            "description": self.description,
            "opponent": self.opponent,
            "win": wonString,
            "gender": team.gender,
            "sport": team.sport,
            "team": team.sub_serialize(),
        }

    def sub_serialize(self):
        wonString = ""
        if self.win == 0:
            wonString = "W"
        if self.win == 1:
            wonString = "L"
        if self.win == 2:
            wonString = "T"
        return {
            "id": self.id,
            "title": self.title,
            "unixTime": self.unixTime,
            "location": self.location,
            "date": datetime.fromtimestamp(self.unixTime).date(),
            "time": datetime.fromtimestamp(self.unixTime).time(),
            "opponent": self.opponent,
            "win": wonString,
            "gender": team.gender,
            "sport": team.sport,
        }