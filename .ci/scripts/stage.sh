#!/bin/bash

cd .ci/staging

docker compose build
docker compose up
docker compose down -v