# Authentication

Authentication use pyjwt `https://github.com/jpadilla/pyjwt`

## Use

- Add `@token_required` before each function required login

## How it work?
When use login, system use pyjwt to generate a token by exp (expired time),
user id, and SECRET_KEY with HS256 

When use send token in header, system decode and get the user id

Frontend:
- Add header: `Authorization Bearer TokenKey`