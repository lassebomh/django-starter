
# Test

```bash
docker compose -f .ci/docker-compose.test.yml up --build && docker compose -f .ci/docker-compose.test.yml down -v
```

# Production


```bash
docker compose -f .ci/docker-compose.prod.yml up --build
```

