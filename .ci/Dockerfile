FROM python:3.11-slim-bookworm as base

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.6.1 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_IN_PROJECT=true \
    POETRY_NO_INTERACTION=1 \
    PYSETUP_PATH="/opt/pysetup" \
    VIRTUAL_ENV="/opt/pysetup/.venv" \
    STATIC_DIST_DIR="/app/static/dist" \
    STATIC_SRC_DIR="vite" \
    NODE_MAJOR=20

ENV PATH="$POETRY_HOME/bin:$VIRTUAL_ENV/bin:$PATH"



FROM base as builder

RUN apt-get update && \
    apt-get install -y ca-certificates curl gnupg build-essential curl && \
    mkdir -p /etc/apt/keyrings && \
    curl -fsSL https://deb.nodesource.com/gpgkey/nodesource-repo.gpg.key | gpg --dearmor -o /etc/apt/keyrings/nodesource.gpg && \
    echo "deb [signed-by=/etc/apt/keyrings/nodesource.gpg] https://deb.nodesource.com/node_$NODE_MAJOR.x nodistro main" | tee /etc/apt/sources.list.d/nodesource.list && \
    apt-get update && \
    apt-get install -y nodejs && \
    pip install poetry==$POETRY_VERSION

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

EXPOSE 8000



FROM prod-runtime as prod

COPY --chmod=777 .ci/prod/entrypoint.sh .
CMD ["./entrypoint.sh"]



FROM prod-runtime as test

COPY --chmod=777 .ci/test/entrypoint.sh .
CMD ["./entrypoint.sh"]
