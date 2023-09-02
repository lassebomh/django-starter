
# Test

```bash
docker compose -f .ci/test/docker-compose.yml up --build && docker compose -f .ci/test/docker-compose.yml down -v
```

# Production


```bash
docker compose -f .ci/prod/docker-compose.yml up --build
```

