## What is request validation?

**request_validator** is a middleware to validate the body of request using request Schema class to sure them are met expectations, and prevent invalid data befor continue to process.

## How to use?

#### In controller file 
```
...
from app.middlewares.request_validator import validate_request_body
from ..schemas import (SigninSchema)
...


@app.route("/signin", methods=["POST"])
@validate_request_body(SigninSchema)
@inject
def signin(user_service: UserService, *params):
    request_data = request.get_json()

    input_data = {
        'email': request_data['email'],
        'password': request_data['password']
    }

    user = user_service.login(**input_data)
    return Token(user).response()
```
