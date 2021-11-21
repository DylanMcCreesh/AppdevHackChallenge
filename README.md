# AppdevHackChallenge


## API Specification:

## Team related routes - These first four routes are the ones implemented so far
### Get all teams
`"/api/teams/", methods=["GET"]`
```
Response:
<HTTP STATUS CODE 200>
{
    "teams": [
        {
            "id": 1,
            "name": "Cornell Women's Soccer",
            "events": [ <SERIALIZED EVENT WITHOUT TEAM FIELD>, ... ]
        },
        {
            "id": 2,
            "name": "Cornell Men's Soccer",
            "events": [ <SERIALIZED EVENT WITHOUT TEAM FIELD>, ... ]
        }
        ...
    ]
}
```

### Create a team
`"/api/teams/", methods=["POST"]`
```
Request:
{
    "name": "Cornell Women's Soccer",
    "password": "password1"
}
```
```
Response:
<HTTP STATUS CODE 201>
{
    "id": 1,
    "name": "Cornell Women's Soccer",
    "events": [ <SERIALIZED EVENT WITHOUT TEAM FIELD>, ... ]
}
```

### Get a specific team
`"/api/teams/<int:team_id>/", methods=["GET"]`
```
Response:
<HTTP STATUS CODE 200>
{
    "id": 1,
    "name": "Cornell Women's Soccer",
    "events": [ <SERIALIZED EVENT WITHOUT TEAM FIELD>, ... ]
}
```

### Delete a team
`"/api/teams/<int:team_id>/", methods=["DELETE"]`
```
Request:
{
    "name": "Cornell Women's Soccer",
    "password": "password1"
}
```
```
Response:
<HTTP STATUS CODE 200>
{
    "id": 1,
    "name": "Cornell Women's Soccer",
    "events": [ <SERIALIZED EVENT WITHOUT TEAM FIELD>, ... ]
}
```


## Event related routes - Not yet Implemented
### Get all events
`"/api/events/", methods=["GET"]`
```
Response:
<HTTP STATUS CODE 200>
{
    "events": [
        {
            "id": 1,
            "title": "Cornell Women's Soccer vs. UVA",
            "time": 1553354209, // Event beginning in unix time
            "location": "Charles F. Berman Field",
            "description": "Enjoy pizza and root for our undefeated soccer team.",
            "team": <SERIALIZED TEAM WITHOUT EVENT FIELD>
        },
        {
            "id": 2,
            "title": "Princeton Hockey vs. Cornell Lacrosse",
            "time": 1553364809, // Event beginning in unix time
            "location": "Lynah Rink",
            "description": "Don't miss the game of the century!",
            "team": <SERIALIZED TEAM WITHOUT EVENT FIELD>
        }
        ...
    ]
}
```

### Get a specific event
`"/api/events/<int:team_id>/<int:event_id>", methods=["GET"]`
```
Response:
<HTTP STATUS CODE 200>
{
    "id": 1,
    "title": "Cornell Women's Soccer vs. UVA",
    "time": 1553354209, // Event beginning in unix time
    "location": "Charles F. Berman Field",
    "description": "Enjoy pizza and root for our undefeated soccer team.",
    "team": <SERIALIZED TEAM WITHOUT EVENT FIELD>
}
```

### Create a new event
`"/api/events/<int:team_id>/", methods=["POST"]`
```
Request:
{
    "name": "Cornell Women's Soccer", // Team name
    "password": "password1",
    "title": "Cornell Women's Soccer vs. UVA",
    "time": 1553354209, // Event beginning in unix time
    "location": "Charles F. Berman Field",
    "description": "Enjoy pizza and root for our undefeated soccer team."
}
```
```
Response:
<HTTP STATUS CODE 201>
{
    "id": 1,
    "title": "Cornell Women's Soccer vs. UVA",
    "time": 1553354209, // Event beginning in unix time
    "location": "Charles F. Berman Field",
    "description": "Enjoy pizza and root for our undefeated soccer team.",
    "team": <SERIALIZED TEAM WITHOUT EVENT FIELD>
}
```

### Delete an event
`"/api/events/<int:team_id>/<int:event_id>", methods=["DELETE"]`


### Get all events from user's favorite teams
`"/api/events/<int:user_id>/", methods=["GET"]`



## User related routes - Not yet implemented
### Get user
`"/api/users/<int:user_id>/", methods=["GET"]`


### Create user
`"/api/users/", methods=["POST"]`


### Get user's favorite teams
`"/api/users/<int:user_id>/favorites/", methods=["GET"]`

### Add team to favorites
`"/api/users/<int:user_id>/favorites/<int:team_id>/", methods=["POST"]`

### Remove team from favorites
`"/api/users/<int:user_id>/favorites/<int:team_id>/", methods=["DELETE"]`
