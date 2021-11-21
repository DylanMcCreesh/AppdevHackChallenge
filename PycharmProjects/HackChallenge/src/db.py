from flask_sqlalchemy import SQLAlchemy

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
    password = db.Column(db.String, nullable=False)
    events = db.relationship("Team", cascade="delete")
    fans = db.relationship(
        "Fan", secondary=association_table, back_populates="favorite_teams"
    )

    def __init__(self, **kwargs):
        self.name = kwargs.get("name")
        self.password = kwargs.get("password")

    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "event": [e.serialize() for e in self.events]
        }

class Event(db.Model):
    __tablename__ = "event"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    time = db.Column(db.String, nullable=False)
    location = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey("team.id"))

    def __init__(self, **kwargs):
        self.title = kwargs.get("title")
        self.due_date = kwargs.get("due_date")
        self.course_id = kwargs.get("course_id")

    def serialize(self):
        return {
            "id": self.id,
            "title": self.title,
            "time": self.time,
            "location": self.location,
            "description": self.description,
            "team": Course.query.filter_by(id=self.team_id).first().serialize(),
        }