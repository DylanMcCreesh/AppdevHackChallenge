# AppdevHackChallenge

1. App Name: Our app's name is "score!".
2. App Tagline: All things Cornell Sports!
3. The ios team members' repository can be found here: https://github.com/erin-xu/sports-tracker
4. The screenshots below demonstrate the functionality and show the user interface of the app.

<img height="700" alt="ss1" src="https://user-images.githubusercontent.com/82056699/144698115-671e0685-0843-4fe3-8849-38aedd04fa91.png"> <img height="700" alt="ss2" src="https://user-images.githubusercontent.com/82056699/144698093-1b4e7336-fac8-4921-a512-03071f4d1b7d.png"> 

When the app is launched, the home screen is shown. On this screen, the next sports event is displayed at the top, along with the team, opponent, date, time, and location. More upcoming events are displayed below in a horizontally-scrollable collection view, including the date, team, opponent, and location. The “see all” button can be clicked to open the upcoming events page.  

<img height="700" alt="ss3" src="https://user-images.githubusercontent.com/82056699/144698280-29c826a7-c969-4f5c-b470-4d0940c2a75e.png"> <img height="700" alt="ss5" src="https://user-images.githubusercontent.com/82056699/144698338-1e72c89f-60d3-4344-9b96-3af9586c8ff2.png">

On this page, all upcoming events can be viewed and searched through using gender and sport filters. The team, location, time, date, and opponent is displayed for each upcoming event.

<img height="700" alt="ss6" src="https://user-images.githubusercontent.com/82056699/144698430-80770225-5800-4782-831f-82212aadf557.png"> <img height="700" alt="ss7" src="https://user-images.githubusercontent.com/82056699/144698519-7ad8f779-c423-425b-96cc-1174993c5d4f.png">

Sports events can also be browsed by team. When clicking on a sports team on the home page, a new page opens with a complete schedule of past and future games. The date, opponent, and location is displayed for each of these events. If the event has already occurred, the result is displayed as well.


5. App Description: An app designed for all Cornell Sports enthusiasts, score! helps its users keep track of Cornell Sporting events. The purpose of score! to make tracking and keeping up with Cornell sports easier for Cornell's incredibly busy students. It is an app which, on its backend, maintains an API of Cornell sporting events, Cornell teams, and users. A team can host many events, and each event is owned by exactly one Cornell team. The backend provides an API which holds all the events that teams have posted, serialized into accessible and readable data about the event for the frontend. On the frontend, data is retrieved from the provided API, and organized so users can filter, sort, and view both completed and upcoming Cornell sporting events. Users are able to filter upcoming events by both type of sport and the team's gender (i.e. Men's Soccer vs. Women's Soccer). Users are also able to access a list of a specific team's upcoming and completed events. When viewing an event, users see the time, date, and location of the event (and if the event has been completed, the score and whether Cornell won or not). 
6. iOS Requirements:        Utilizes NSLayoutConstraint.  Implements UICollectionView. Uses UINavigationController to navigate between screens. Integrates the API provided by the backend for data retrieval regarding the information for the sport evnets.  
   
   Backend Requirements:    The backend provided an API which both met and passed the outlined requirements. Our API implements 14 routes (including GET, POST, and DELETE methods), where 4 are required (note: the frontend does not yet utilize all provided routes, but does use more than 4 of the required routes). Our database houses three tables (Fan, Team, and Event Tables) and an association table between the Fan and Team tables, as well as relational keys between the Event and Team tables. Finally, an API specification is provided below for all 14 of the routes (both those utilized and not yet utilized by the frontend).
   
7. Other Notes: The backend implemented routes that haven't yet been implemented by the frontend. We believe in the future these routes could be used to enhance the features and functionality of the app. For example, the capcity for user's to create password-protected accounts and to select favorite teams already exists within the backend.

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
    "win": 0
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
    "win": 0
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
