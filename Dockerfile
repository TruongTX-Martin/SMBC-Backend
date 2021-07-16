FROM python:3.8

RUN pip install poetry

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /var/www
WORKDIR /var/www

COPY pyproject.toml poetry.lock ./
RUN poetry config virtualenvs.create false && poetry install --no-root && rm -rf /var/cache/pypoetry

COPY . /var/www/app

WORKDIR /var/www/app

RUN cp /var/www/app/documents/api.yaml /var/www/app/app/static/documents/

CMD ["poetry", "run", "python", "manage.py", "run"]
