# AppdevHackChallenge


## API Specification:

#### "/api/teams/", methods=["GET"]
    Get all teams.


#### "/api/teams/", methods=["POST"]
    Create new team with given name and password.


#### "/api/teams/<int:team_id>/", methods=["GET"]
    Get info about team with team_id.


#### "/api/teams/<int:team_id>/", methods=["DELETE"]
    Delete team with team_id.



# Event related routes
#### "/api/events/", methods=["GET"]
    Get all events.


#### "/api/events/<int:team_id>/<int:event_id>", methods=["GET"]
    Get event with event_id from team_id team.


#### "/api/events/<int:team_id>/", methods=["POST"]
    Post new event to team_id team.


#### "/api/events/<int:team_id>/<int:event_id>", methods=["DELETE"]
    Delete event with team_id.


#### "/api/events/<int:user_id>/", methods=["GET"]
    Get all events associated with user with user_id.



# User related routes
#### "/api/users/<int:user_id>/", methods=["GET"]
    Get user with user_id.


#### "/api/users/", methods=["POST"]
    Create user with provided information.


#### "/api/users/<int:user_id>/favorites/", methods=["GET"]
    Get all favorite teams of user with user_id.

#### "/api/users/<int:user_id>/favorites/<int:team_id>/", methods=["POST"]
    Add team with team_id to users favorite teams.

#### "/api/users/<int:user_id>/favorites/<int:team_id>/", methods=["DELETE"]
    Remove team with team_id from users favorite teams.
