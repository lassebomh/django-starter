FROM python:3.10-slim

EXPOSE 8000

RUN apt-get update
RUN apt-get install -y --no-install-recommends python3-dev libpq-dev gcc nodejs npm

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV SHELL=/bin/bash

COPY requirements.txt .
RUN python -m pip install -r requirements.txt

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