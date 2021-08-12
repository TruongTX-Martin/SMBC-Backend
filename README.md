# Flask App Base

Python Code to quickly bootstrap Nexus Projects using the Flask framework.

Flask is a lightweight WSGI web application framework. It is designed to make getting started quick and easy, with the ability to scale up to complex applications.

A minimal Flask Application looks something like this:

``` Python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello, World!"
```

For more information about Flask, please check the [Flask Documentation](https://flask.palletsprojects.com/en/2.0.x/)

This project is written in Python 3.8, Flask 1.1.4

This project uses `pyproject.toml` proposed on [PEP-0518](https://www.python.org/dev/peps/pep-0518/#specification) instead of `requirements.txt`. [Poetry](https://python-poetry.org/) is used for dependency management.

## Deployment

There are two ways to deploy Flask App Base on your environment for local development. Either by pyenv or by docker-compose (recommended!).

**Note:** You will need to provide a `.env` file in the working directory to provide environment configurations.

### 1. Set up local Python 3.8.x environment with `pyenv` and install Poetry

- Install [pyenv](https://github.com/pyenv/pyenv)
- Install latest version of python 3.8.x and use it.

``` bash
pyenv install 3.8.0
pyenv local 3.8.0
```

- Install [Poetry](https://python-poetry.org/)

``` bash
pip3 install poetry
```

- Install dependency

``` bash
poetry install
```

- Run http server

``` bash
poetry run python manage.py run
```

### 2. Deploy project with Docker compose (Recommended!)

#### What is Docker?

Docker provides the ability to package and run an application in a loosely isolated environment called a container. Containers are lightweight and contain everything needed to run the application, so you do not need to rely on what is currently installed on the host. You can easily share containers while you work, and be sure that everyone you share with gets the same container that works in the same way.

For more information about Docker, please check the [Docker Documentation](https://docs.docker.com/get-started/overview/)

Please have a current version of Docker installed on your machine. [Docker Desktop](https://www.docker.com/products/docker-desktop) provides you with the Docker CLI as well as a dashboard to easily view your containers.

#### What is Docker-Compose?

Compose is a tool for defining and running multi-container Docker applications. With Compose, you use a YAML file to configure your application’s services. Then, with a single command, you create and start all the services from your configuration. Compose is included in the Docker CLI, so no additional installation is required.

For more information about Docker-Compose, please check the [Docker-Compose Documentation](https://docs.docker.com/compose/)

#### Get Started

This project has 2 containers for local development. A container for the flask app and postgres database each. Please check detail configuration in `docker-compose.yml`

- db: Postgres database with initiate database script in `docker/init.sql`
- app: Python Flask Application

``` bash
cd flask-app-base
docker compose up
```

Alternatively, you can run `make test` in the terminal.

### How to execute commands inside a Docker-Compose container

Use the `docker compose exec <DOCKER_CONTAINER> <COMMAND>` command in your terminal.

For example, if you wanted to run `poetry run python manage.py database upgrade` command:

``` bash
docker-compose exec app poetry run python manage.py database upgrade
```

**Note:** that you need to have the container running first before you execute these commands. Use `docker container ls` to see the running containers.

### Migrate Database

After running the project on your machine, you will still need to migrate the database for the application to work properly.

#### Migrate Database on local Python environment

- Update database

``` bash
poetry run python manage.py database upgrade
```

- Generate the migration files

``` bash
poetry run python manage.py database migrate
```

#### Migrate Database on Docker Compose environment

``` bash
docker compose exec app poetry run python manage.py database upgrade
docker compose exec app poetry run python manage.py database migrate
```

### Seed Database

At this point, the application should run perfectly. However, to generate mock data and give a realistic look of the application, run the following command to seed the database. Of course, the seed data first has to be present in the `app/seed/` directory.

For Local Python Environment

``` bash
poetry run python manage.py seed
```

For Docker Compose Environment

``` bash
docker compose exec app poetry run python manage.py seed
```

Congratulations! Your application has been deployed successfully and is now ready for active development. Please see the additional documentation below for more information on the specific components and good development practices.

For more information about deploying project to Local Environment, please see [Running Project In My Local Environment Documentation](./documents/how-to-run-local.md)

## FAQ

- **Where can I get the .env file?**
    Check with your project owner. The .env file contains all environment configurations including server access keys. Ensure that it is in your `.gitignore` and is not pushed to Github!

    See `.env.example` for a sample .env file.

    ``` bash
    cp .env.example .env
    ```

    Please update the database information with DB_ENVIRONMENT variables in .env file

- **Who supports this project?**
    If you are having any issues, please check with Mike.

## All Documentation

- [Structuring Your Flask App](./documents/flask-app-structure.md)
- [Conventions and Practices](./documents/conventions.md)
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

**Next:** [Structuring Your Flask App](./documents/flask-app-structure.md)