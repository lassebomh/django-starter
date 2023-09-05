FROM python:3.11-slim as base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VIRTUAL_ENV="/opt/pysetup/.venv" \
    STATIC_DIST_DIR="/app/static/dist" \
    STATIC_SRC_DIR="static_vite" \
    NODE_MAJOR=20

ENV PATH="$POETRY_HOME/bin:$VIRTUAL_ENV/bin:$PATH"



FROM base as builder

RUN apt-get update && \
    apt-get install -y --no-install-recommends nodejs npm
    
COPY .ci/install-poetry.py .
RUN python install-poetry.py

WORKDIR $PYSETUP_PATH
COPY ./poetry.lock ./pyproject.toml ./
RUN poetry install --without dev

WORKDIR /app/$STATIC_SRC_DIR
COPY ./$STATIC_SRC_DIR/package*.json .
RUN npm ci



FROM builder as dev

WORKDIR $PYSETUP_PATH
RUN poetry install

WORKDIR /app/$STATIC_SRC_DIR
RUN npm install

WORKDIR /app

COPY . .

EXPOSE 8000

CMD bash



FROM builder as prod-builder

WORKDIR /app/

COPY . .

WORKDIR /app/$STATIC_SRC_DIR
RUN npm run build

WORKDIR /



FROM base as prod-runtime

COPY --from=prod-builder $POETRY_HOME $POETRY_HOME
COPY --from=prod-builder $PYSETUP_PATH $PYSETUP_PATH
COPY --from=prod-builder $STATIC_DIST_DIR $STATIC_DIST_DIR

WORKDIR /app

COPY . .

COPY --chmod=777 .ci/entrypoint*.sh .



FROM prod-runtime as prod

EXPOSE 8000

RUN python manage.py collectstatic --no-input

CMD ["./entrypoint.prod.sh"]



FROM prod-runtime as worker

CMD ["./entrypoint.worker.sh"]