# Structuring Your Flask App

This documents contains the structure of the Flask App Base and some of the key principles used in software design.

## Flask App Base Structure

``` bash
flask-app-base
├── Dockerfile # Dockerfile for flask app Container
├── Makefile   # Makefile to run commands 
├── README.md 
├── app
│   ├── __init__.py
│   ├── bootstrap
│   │   └── __init__.py # Initialise flask app here
│   ├── cache
│   │   # Flask app caching
│   ├── config
│   │   # Set app configuration
│   ├── contexts
│   │   # Handles Application Context and Request Context
│   ├── database
│   │   # Initialise database using ORM 
│   ├── exceptions
│   │   # Declare custom exceptions here
│   ├── helpers
│   │   # Define helpers for some tasks
│   ├── middlewares
│   │   # Middleware layer, contains authentication processes
│   ├── models
│   │   # Define object models here
│   ├── repositories
│   │   # Repositories layer for data persistence
│   ├── response_error_handler.py # Handle errors and exceptions
│   ├── services
│   │   # Service layer for business logic
│   ├── session.py
│   └── views
│       ├── api
│       │   ├── controllers
│       │   │   # Controller layer for API
│       │   ├── responses
│       │   │   # Responses for API controllers
│       │   ├── routes.py # Build API routes here
│       │   └── schemas
│       │       # Field validation of request parameters
│       └── frontend
│           # Front end optimisations for deployment
├── docker 
│   │   # Configurations for docker containers here
│   ├── db
│   │   └── init.sql # Initialise database
│   └── nginx 
│       ├── Dockerfile 
│       └── nginx.conf
├── docker-compose.test.yml # Docker Compose for local testing
├── docker-compose.yml # Docker Compose for production
├── documents
│   │   # Place all documentation here
│   ├── api.yaml # Swagger Documentation for APIs
│   └── db 
│       # Plant UML ER-Diagram Documentation
├── manage.py # Handles sub
├── migrations
│   # Database Migrations
├── poetry.lock # Poetry manages dependencies
├── pyproject.toml
├── seeds
│   # Seed data
├── server.py
├── templates
│   # Static templates for rendering
└── tests # Test module
    ├── __init__.py
    ├── test_flask_base.py
    └── unit
        ├── __init__.py
        ├── app
        │   ├── __init__.py
        │   ├── services
        │   │   # Service Tests
        │   └── view
        │       └── api
        │           # API Tests
        ├── factories
        │   # factory boy implementation to generate fake data in the database
        └── mocks
            ├── repositories
            │   # Mock repositories
            └── test_data
```

### MVC Framework

The Model-View-Controller (MVC) framework is an architectural pattern that separates an application into three main logical components Model, View, and Controller. Each architecture component is built to handle specific development aspect of an application. MVC separates the business logic and presentation layer from each other.

In Flask App Base, the user will interact with a Front-End JavaScript framework like ReactJS (This is the **View Layer**). The Front-End makes API requests to our Back-End API Controller.

The **Controller Layer** handles these requests and coordinates the response.

Data is passed down to the **Model Layer** business logic is applied through the Services. Finally, for data persistence, the Repositories store data in the database using an ORM.

### SOLID Principles of Object Oriented Programming

In Flask App Base, we make use of multiple class definitions - be it for defining Services, Repositories or Model objects.

SOLID is an acronym for the first five object-oriented design (OOD) principles by Robert C. Martin. These principles establish practices that lend to developing software with considerations for maintaining and extending as the project grows. Adopting these practices can also contribute to avoiding code smells, refactoring code, and Agile or Adaptive software development.

- **Single Responsibility Principle**

    A class should only one job. Store a single class in a single file. If a class gets too big or has multiple functions, you might want to consider splitting it up into multiple classes.

- **Open-Closed Principle**

    A class should be extendable, without modifying the class itself. You should not need to modify the code you have already written to accommodate new functionality, but simply add what you now need.

- **Liskov Substitution Principle**

    Derived classes must be substitutable for their base classes. If you are using a function and your colleague changes the base class, you should not notice any difference in the function that you are using.

- **Interface Segregation Principle**

    A class should not inherit functions from a base class that it does not need.

- **Dependency Inversion Principle**

    Entities must depend on abstractions, not on concretions. It states that the high-level module must not depend on the low-level module, but they should depend on abstractions. For example, use an abstraction to decouple inputs to a function.

### Dependency Injection Pattern

In Flask App Base, dependency injection is applied in the Repository, Service and Controller layer. In dependency injection, objects do not create each other, but the `Dependency Injector` has the responsibility of assembling the dependencies. For example, one instance of the Repository class will exist, and it is 'injected' into the Service class, where its functions can be called.

Flask-Injector is used to bind the classes together. This is done in `/app/bootstrap/__init__.py`. For more information, please check the [Flask-Injector Documentation](https://github.com/alecthomas/flask_injector).

For more information about structuring good python code, please read [Cosmic Python: Simple Patterns For Building Complex Applications](https://www.cosmicpython.com/book/introduction.html)

**Next**: [Conventions And Recommended Practices](../documents/conventions.md)