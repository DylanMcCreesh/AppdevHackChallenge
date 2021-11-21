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

# your routes here
@app.route("/api/courses/")
def get_courses():
    return success_response(
        {"courses": [c.serialize() for c in Course.query.all()]}
    )

@app.route("/api/courses/", methods=["POST"])
def create_course():
    body = json.loads(request.data)
    if not body.get("name") or not body.get("code"):
        return failure_response("not all fields were provided!", 400)
    new_course = Course(code=body.get("code"), name=body.get("name"))
    db.session.add(new_course)
    db.session.commit()
    return success_response(new_course.serialize(), 201)


@app.route("/api/courses/<int:course_id>/")
def get_course(course_id):
    course = Course.query.filter_by(id=course_id).first()
    if course is None:
        return failure_response("Course not found!")
    return success_response(course.serialize())

@app.route("/api/courses/<int:course_id>/", methods=["DELETE"])
def delete_course(course_id):
    course = Course.query.filter_by(id=course_id).first()
    if course is None:
        return failure_response("Course not found!")
    db.session.delete(course)
    db.session.commit()
    return success_response(course.serialize())

@app.route("/api/users/", methods=["POST"])
def create_user():
    body = json.loads(request.data)
    if not body.get("name") or not body.get("netid"):
        return failure_response("not all fields were provided!", 400)
    new_user = User(name=body.get("name"), netid=body.get("netid"))
    db.session.add(new_user)
    db.session.commit()
    return success_response(new_user.serialize(), 201)

@app.route("/api/users/<int:user_id>/")
def get_user(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return failure_response("User not found!")
    return success_response(user.serialize())

@app.route("/api/courses/<int:course_id>/add/", methods=["POST"])
def add_user(course_id):
    body = json.loads(request.data)
    course = Course.query.filter_by(id=course_id).first()
    if course is None:
        return failure_response("Course not found!")
    if not body.get("user_id"):
        return failure_response("user not provided!", 400)
    if body.get("type") != "student" and body.get("type") != "instructor":
        return failure_response("invalid user type", 400)
    user = User.query.filter_by(id=body.get("user_id")).first()
    if user is None:
        return failure_response("User not found!")
    for person in course.students:
        if person.id == user.id:
            return failure_response("already in the class!", 400)
    for person in course.instructors:
        if person.id == user.id:
            return failure_response("already in the class!", 400)
    if body.get("type") == "student":
        course.students.append(user)
    if body.get("type") == "instructor":
        course.instructors.append(user)
    db.session.commit()
    course = Course.query.filter_by(id=course_id).first()
    return success_response(course.serialize())

@app.route("/api/courses/<int:course_id>/assignment/", methods=["POST"])
def add_assignment(course_id):
    body = json.loads(request.data)
    course = Course.query.filter_by(id=course_id).first()
    if course is None:
        return failure_response("Course not found!")
    if not body.get("title") or not body.get("due_date"):
        return failure_response("not all fields filled", 400)
    assignment = Assignment(title=body.get("title"), due_date=body.get("due_date"), course_id=course_id)
    course = Course.query.filter_by(id=course_id).first()
    course.assignments.append(assignment)
    db.session.add(assignment)
    db.session.commit()
    return success_response(assignment.serialize(), 201)

@app.route("/reset/")
def reset():
    db.drop_all()
    db.create_all()
    return success_response("yes")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
