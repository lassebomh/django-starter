ARG STATIC_DIST_DIR=/app/static/dist

FROM python:3.11 as base

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache \
    POETRY_VERSION=${POETRY_VERSION}

RUN apt update
RUN apt install -y --no-install-recommends nodejs npm

RUN pip install poetry==1.6.1

WORKDIR /app


FROM base as dev

ENV VIRTUAL_ENV=/app/.venv \
    PATH="/app/.venv/bin:$PATH" \
    STATIC_DIST_DIR=${STATIC_DIST_DIR} \
    POETRY_CACHE_DIR=/app/.venv/poetry_cache

RUN adduser -u 5678 --disabled-password --gecos "" appuser

COPY pyproject.toml poetry.lock ./
RUN poetry install --no-root

COPY package*.json .
RUN  npm install

COPY . .

RUN chmod 777 /app/node_modules
RUN chown -R appuser /app

EXPOSE 8000

USER appuser

CMD bash


FROM base as prod-builder

COPY pyproject.toml poetry.lock ./
RUN poetry install --without dev --no-root && rm -rf $POETRY_CACHE_DIR

COPY ./vite/package*.json ./vite/
RUN cd ./vite && npm ci

COPY ./vite ./vite
RUN cd ./vite && npm run build


FROM python:3.11-slim as prod-runtime

WORKDIR /app

COPY --from=prod-builder /app/.venv /app/.venv

RUN chmod +x /app/.venv/bin/python
RUN chmod +x /app/.venv/bin/pip

COPY --from=prod-builder ${STATIC_DIST_DIR} ${STATIC_DIST_DIR}

RUN adduser -u 5678 --disabled-password --gecos "" appuser
COPY --chown=appuser . .

USER appuser


FROM prod-runtime as prod

EXPOSE 8000

CMD [\
    "python", "manage.py", "migrate", "&&", \
    "python", "manage.py", "collectstatic", "&&", \
    "gunicorn", "--bind", "0.0.0.0:8000", "--worker-tmp-dir", "/dev/shm", "mysite.wsgi" \
]


FROM prod-runtime as test

ENV VIRTUAL_ENV="/app/.venv" \
    PATH="/app/.venv/bin:$PATH" \
    STATIC_DIST_DIR=${STATIC_DIST_DIR}

RUN echo which python
RUN echo whereis python


CMD [\
    "python", "manage.py", "migrate", "&&", \
    "python", "manage.py", "collectstatic", "&&", \
    "python", "manage.py", "test" \
]