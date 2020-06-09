# Authentication
Let’s say you have a Flask application that allows user to add tweets.
Each tweet belongs to a user and only logged in user can add tweet. 
Therefore you want to limit some routes to only logged in users and if user is not logged in, 
they will be redirected to the login page

Adding the login check for every route is quite cumbersome and violates the DRY principle.
It would be very handy if we can just decorate such routes with @login_required and all the login checks will be done automatically


Authentication use pyjwt `https://github.com/jpadilla/pyjwt`

The authentication we are using decorator.

Check http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
to see detail about decorator


## Use

- Add `@token_required` before each function required login
```python
@app.route("/add_tweet")
@login_required
def add_tweet():
```

## How it work?

Currently we created function `token_required` in `app/middlewares/authenticate.py`

1. First Check the Authorization in header request:
 `auth_header = request.headers.get('Authorization')`

2. Second Get the token: ` _, token = auth_header.split()`

3. Third decode the token, we get the user id `decoded = jwt.decode(token, Config.SECRET_KEY, algorithms='HS256')`

4. Four get user and set user by user service
`user_service.load_logged_in_user_to_request(decoded['id'])`

When use login, system use pyjwt to generate a token by exp (expired time),
user id, and SECRET_KEY with HS256 

When use send token in header, system decode and get the user id

Frontend:
- Add header: `Authorization Bearer TokenKey`

![Accesstoken](images/access-token-in-header.png)