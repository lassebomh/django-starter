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
    STATIC_SRC_DIR="vite"

ENV PATH="$POETRY_HOME/bin:$VIRTUAL_ENV/bin:$PATH"



FROM base as builder

RUN apt update && apt install -y --no-install-recommends build-essential curl nodejs npm

RUN curl -sSL https://install.python-poetry.org | python -

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



FROM prod-runtime as prod

EXPOSE 8000

COPY --chmod=777 .ci/entrypoint.prod.sh .
CMD ["./entrypoint.prod.sh"]



FROM prod-runtime as test

COPY --chmod=777 .ci/entrypoint.test.sh .
CMD ["./entrypoint.test.sh"]
