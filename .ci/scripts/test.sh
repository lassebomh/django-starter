#!/bin/bash

cd .ci/staging

echo "::group::Stopping services"
docker compose down -v
echo "::endgroup::"

echo "::group::Pulling images"
docker compose pull
echo "::endgroup::"

echo "::group::Building images"
docker compose build
echo "::endgroup::"

echo "::group::Running tests"
docker compose run django ./entrypoint.test.sh
echo "::endgroup::"

echo "::group::Stopping services"
docker compose down -v
echo "::endgroup::"
