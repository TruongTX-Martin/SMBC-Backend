# How to setup project

This project uses `pyproject.toml` proposed on [PEP-0518](https://www.python.org/dev/peps/pep-0518/#specification) instead of `requirements.txt`. And you can use [Poetry](https://python-poetry.org/).

## 1. Setup python 3.8.x environment with `pyenv` and install Poetry

- Install [pyenv](https://github.com/pyenv/pyenv)
- Install latest version of python 3.8.x and use it.

```
pyenv install 3.8.0
pyenv local 3.8.0
```

- Install [Poetry](https://python-poetry.org/)

```
pip3 install poetry
```

- Install dependency

```
poetry install
```

- Run http server

```
poetry run python manage.py run
```


## How to run with Docker compose

We have 2 container for local development. Please check detail configuration in `docker-compose.yml`

- db: Postgres database with initiate database process in `docker/init.sql`
- app: oppi application

```
cd oppi_mvp
docker-compose up
```

#### How to execute a poetry command in side docker-compose container
For example with `poetry run python manage.py database upgrade` command you can run through `docker-compose exec`

```bash
docker-compose exec app poetry run python manage.py database upgrade

```

## How to update database

### 1. Update models files
Please update your model files by adding new fields or add new model

### 2. Update database

```bash
poetry run python manage.py database upgrade
```

### 3. Generate migration files
```bash
poetry run python manage.py database migrate
```

### 4. Code format

Please execute isort and yapf before committing

```bash

poetry run isort -rc -y app tests

poetry run yapf -ir -vv app tests
```

For Docker compose environment

```bash

docker-compose exec app poetry run isort -rc -y app tests

docker-compose exec app poetry run yapf -ir -vv  app tests

```

Add pre_commit to .git hooks for auto format code.


```bash
cp  .git-hooks/pre-commit .git/hooks


chmod +x .git/hooks/pre-commit

```

* Note, this git hook uses poetry mode by default. For `pip`, `pipenv` environment please remove comment out from .git/hooks/pre-commit


### 5. Run unittest

Command:
poetry run python manage.py test

Option `-p` for path of test file, directory

#### Local machine

```bash
poetry run python manage.py test -p tests

```

#### Docker compose environment
Start test Docker environment

```bash
make test

```

Run test case in Docker compose environment
```.env
docker-compose exec app poetry run python manage.py test -p tests

# or
make run-test
```

Other documents
- [API design (Swagger)](./documents/api.yaml)
- [Database ERD design](./documents/db/schema.plantuml)
- [Authentication Flow](./documents/authentication.md)
- [How to create a middleware](./documents/how-to-create-middleware.md)
- [How to migrate database](./documents/how-to-migrate-database.md)
- [How to validate a request](./documents/how-to-validate-request-params.md)
- [How to write an unittest](./documents/unittest.md)
- [How to create a soft delete model](./documents/how-to-create-soft-delete-model.md)
- [How to use sql transaction](./documents/how-to-use-a-sql-transaction.md)
- [How to use cache](./documents/how-to-use-a-cache.md)
