FROM python:3.10-slim

EXPOSE 8000

RUN apt-get update
RUN apt-get install -y --no-install-recommends python3-dev libpq-dev gcc nodejs npm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SHELL=/bin/bash

ENV POETRY_VERSION=1.6.1
ENV POETRY_NO_INTERACTION=1
ENV POETRY_VIRTUALENVS_CREATE=false
# ENV POETRY_HOME='/usr/local'

COPY poetry.lock pyproject.toml ./
RUN python -m pip install "poetry==${POETRY_VERSION}"
RUN python -m poetry install

# COPY requirements.txt .
# RUN python -m pip install -r requirements.txt

WORKDIR /app

COPY package*.json ./
RUN npm install

RUN chmod -R 777 node_modules/

COPY . .

RUN adduser -u 5678 --disabled-password --gecos "" appuser
RUN chown -R appuser /app

USER appuser

# During debugging, this entry point will be overridden.
CMD [\
    "python", "manage.py", "migrate", "&&", \
    "npm", "run", "build", "&&", \
    "python", "manage.py", "collectstatic", "&&", \
    "gunicorn", "--bind", "0.0.0.0:8000", "mysite.wsgi" \
    ]