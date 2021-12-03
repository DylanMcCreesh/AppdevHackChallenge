# AppdevHackChallenge

The ios team members' repository can be found here: https://github.com/erin-xu/sports-tracker

## API Specification:

## Team related routes
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
            "gender": "Women's",
            "sport": "Soccer",
            "events": [<SERIALIZED EVENT WITHOUT TEAM FIELD>, ... ]
        },
        {
            "id": 2,
            "name": "Cornell Men's Soccer",
            "gender": "Men's",
            "sport": "Soccer",
            "events": [<SERIALIZED EVENT WITHOUT TEAM FIELD>, ... ]
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
    "password": "password1",
    "gender": "Women's",
    "sport": "Soccer",
}
```
```
Response:
<HTTP STATUS CODE 201>
{
    "id": 1,
    "name": "Cornell Women's Soccer",
    "gender": "Women's",
    "sport": "Soccer",
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
    "gender": "Women's",
    "sport": "Soccer",
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
    "gender": "Women's",
    "sport": "Soccer",
    "events": [ <SERIALIZED EVENT WITHOUT TEAM FIELD>, ... ]
}
```


## Event related routes
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
            "unixTime": 1638485544, // Event beginning in unix time
            "location": "Charles F. Berman Field",
            "date": "2021-08-02",
            "time": "06:43:43",
            "description": "Enjoy pizza and root for our undefeated soccer team.",
            "opponent": "UVA Women's Soccer",
            "score": "3-1",
            "win": "W",
            "team": <SERIALIZED TEAM WITHOUT EVENT FIELD>
        },
        {
            "id": 2,
            "title": "Princeton Hockey vs. Cornell Hockey",
            "unixTime": 1553364809, // Event beginning in unix time
            "location": "Lynah Rink",
            "date": "2021-08-02"
            "time": "06:43:43",
            "description": "Don't miss the game of the century!",
            "opponent": "Princeton Hockey"
            "score": "1-2",
            "win": "L",
            "team": <SERIALIZED TEAM WITHOUT EVENT FIELD>
        }
        ...
    ]
}
```

### Get a specific event
`"/api/events/<int:event_id>", methods=["GET"]`
```
Response:
<HTTP STATUS CODE 200>
{
    "id": 1,
    "title": "Cornell Women's Soccer vs. UVA",
    "unixTime": 1638485544, // Event beginning in unix time
    "location": "Charles F. Berman Field",
    "date": "2021-08-02",
    "time": "06:43:43",
    "description": "Enjoy pizza and root for our undefeated soccer team.",
    "opponent": "UVA Women's Soccer",
    "score": "3-1",
    "win": "W",
    "team": <SERIALIZED TEAM WITHOUT EVENT FIELD>
}
```

### Create a new event
`"/api/events/", methods=["POST"]`
```
Request:
{
    "team_id": 3,
    "name": "Cornell Women's Soccer",
    "password": "password1"
    "title": "Cornell Women's Soccer vs. UVA",
    "unixTime": 1638485544, // Event beginning in unix time
    "location": "Charles F. Berman Field",
    "description": "Enjoy pizza and root for our undefeated soccer team.",
    "opponent": "UVA Women's Soccer",
    "score": "3-1",
    "win": "W"
}
```
```
Response:
<HTTP STATUS CODE 201>
{
    "id": 1,
    "title": "Cornell Women's Soccer vs. UVA",
    "unixTime": 1638485544, // Event beginning in unix time
    "location": "Charles F. Berman Field",
    "date": "2021-08-02",
    "time": "06:43:43",
    "description": "Enjoy pizza and root for our undefeated soccer team.",
    "opponent": "UVA Women's Soccer",
    "score": "3-1",
    "win": "W",
    "team": <SERIALIZED TEAM WITHOUT EVENT FIELD>
}
```

### Update an event
`"/api/events/", methods=["POST"]`
```
Request:
{
    "name": "Cornell Women's Soccer",
    "password": "password1"
    "title": "Cornell Women's Soccer vs. UVA",
    "unixTime": 1638485544, // Event beginning in unix time
    "location": "Charles F. Berman Field",
    "description": "Enjoy pizza and root for our undefeated soccer team.",
    "opponent": "UVA Women's Soccer",
    "score": "3-1",
    "win": "W"
}
```
```
Response:
<HTTP STATUS CODE 201>
{
    "id": 1,
    "title": "Cornell Women's Soccer vs. UVA",
    "unixTime": 1638485544, // Event beginning in unix time
    "location": "Charles F. Berman Field",
    "date": "2021-08-02",
    "time": "06:43:43",
    "description": "Enjoy pizza and root for our undefeated soccer team.",
    "opponent": "UVA Women's Soccer",
    "score": "3-1",
    "win": "W",
    "team": <SERIALIZED TEAM WITHOUT EVENT FIELD>
}
```

### Delete an event
`"/api/events/<int:event_id>", methods=["DELETE"]`
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
    "title": "Cornell Women's Soccer vs. UVA",
    "unixTime": 1638485544, // Event beginning in unix time
    "location": "Charles F. Berman Field",
    "date": "2021-08-02",
    "time": "06:43:43",
    "description": "Enjoy pizza and root for our undefeated soccer team.",
    "opponent": "UVA Women's Soccer",
    "score": "3-1",
    "win": "W",
    "team": <SERIALIZED TEAM WITHOUT EVENT FIELD>
}
```

### Get all events from user's favorite teams
`"/api/events/users/<int:user_id>/", methods=["GET"]`
```
Request:
{
    "name": "John Smith",
    "password": "iluvmymommy"
}
```
```
Response:
<HTTP STATUS CODE 200>
{
    "events": [
        {
            "id": 3,
            "title": "Cornell Women's Soccer vs. UVA",
            "unixTime": 1638485544, // Event beginning in unix time
            "location": "Charles F. Berman Field",
            "date": "2021-08-02",
            "time": "06:43:43",
            "description": "Enjoy pizza and root for our undefeated soccer team.",
            "opponent": "UVA Women's Soccer",
            "score": "3-1",
            "win": "W",
            "team": <SERIALIZED TEAM WITHOUT EVENT FIELD>
        },
        {
            "id": 7,
            "title": "Princeton Hockey vs. Cornell Hockey",
            "unixTime": 1553364809, // Event beginning in unix time
            "location": "Lynah Rink",
            "date": "2021-08-02"
            "time": "06:43:43",
            "description": "Don't miss the game of the century!",
            "opponent": "Princeton Hockey"
            "score": "1-2",
            "win": "L",
            "team": <SERIALIZED TEAM WITHOUT EVENT FIELD>
        }
        ...
    ]
}
```

## User related routes
### Get user
`"/api/users/<int:user_id>/", methods=["GET"]`
```
Request:
{
    "name": "John Smith",
    "password": "iluvmymommy"
}
```
```
Response:
<HTTP STATUS CODE 200>
{
    "id": 41,
    "name": "John Smith",
    "teams": [<SERIALIZED TEAM>, ... ] // Favorite teams
}
```

### Create user
`"/api/users/", methods=["POST"]`
```
Request:
{
    "name": "Inle Bush",
    "password": "supersecretpassword"
}
```
```
Response:
<HTTP STATUS CODE 201>
{
    "id": 30,
    "name": "Inle Bush",
    "teams": []
}
```

### Add team to favorites
`"/api/users/<int:user_id>/favorites/<int:team_id>/", methods=["POST"]`
```
Request:
{
    "name": "John Smith",
    "password": "iluvmymommy"
}
```
```
Response:
<HTTP STATUS CODE 201>
{
    "id": 41,
    "name": "John Smith",
    "teams": [<SERIALIZED TEAM>, ... ] // Favorite teams with added team
}
```

### Remove team from favorites
`"/api/users/<int:user_id>/remove/<int:team_id>/", methods=["POST"]`
```
Request:
{
    "name": "John Smith",
    "password": "iluvmymommy"
}
```
```
Response:
<HTTP STATUS CODE 200>
{
    "id": 41,
    "name": "John Smith",
    "teams": [<SERIALIZED TEAM>, ... ] // Favorite teams without team
}
```
