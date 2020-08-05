## Run App
poetry run uvicorn main:app --reload

## Start postgres as a docker container

```bash
docker run \
  --rm \
  --name postgres \
  -p 5432:5432 \
  -e POSTGRES_USER=user \
  -e POSTGRES_PASSWORD=mysecretpassword \
  postgres
```