# Conventions and Recommended Practices

Please refer to this document for the conventions and the recommended practices used in this project.

## Git Workflow

We use git and Github for version control.

### Git Branch Naming Conventions

Name format `<type>/<name>_<issue_no>`

See [Innovatube Development-Rules: Git](https://github.com/Innovatube/development-rules/blob/master/common/git.md) for more details.

## Documenting APIs

It is important to update the Swagger documentation at `app/documents/api.yaml` every time a change is made to the API. This is to help the Front-End and Back-End teams to work together and communicate on requirements.

### About Swagger

The Swagger Editor is an open source editor to design, define and document RESTful APIs in the Swagger Specification. The Swagger plugin can be installed on your local IDE, and used to render the YAML file at `app/documents/api.yaml` into the Swagger UI.

For guidelines on how to write API documentation in the Swagger Specification, please check [Open API Specification Docs](https://swagger.io/specification/)

## Documenting ERD

It is important to update the Entity-Relationship Diagram at `app/documents/db/schema.plantuml` every time a change is made to the Database Design. This is to help Back-End team to coordinate changes. 

ERD Documentation: [/documents/db/schema.plantuml](./db/schema.plantuml)

We are using PlantUML to manage ERD. Please install plantUML extension to your IDE to view the file.

Please run this command to auto generate and update the ERD, every time you update the Models.

``` bash
poetry run manage.py generate_erd
```

## Code Formatting

In this project we use isort and yapf to maintain code. Please execute isort and yapf before committing

```bash
poetry run isort -rc -y .
poetry run yapf -ir -vv .
```

For Docker-Compose run:

``` bash
docker-compose exec app poetry run isort -rc -y app tests migrations seeds
docker-compose exec app poetry run yapf -ir -vv  app tests migrations seeds
```

You can also add pre_commit to .git hooks for auto format code.

``` bash
cp  .git-hooks/pre-commit .git/hooks
chmod +x .git/hooks/pre-commit
```

* Note, this git hook uses poetry mode by default. For `pip`, `pipenv` environment please remove comment out from .git/hooks/pre-commit

**Next**: [Writing Unit Tests](../documents/unittest.md)
