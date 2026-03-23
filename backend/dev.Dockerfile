# FROM python:3.13.5-bullseye
FROM python:3.14.3-alpine3.23

WORKDIR /container
EXPOSE 8000

RUN apk update 
RUN pip install pdm
RUN apk add gcc musl-dev linux-headers
COPY ./container/pyproject.toml .
COPY ./container/pdm.lock .
COPY ./container/README.md .
RUN pdm install -G dev

COPY ./container .



ENV TZ=Asia/Bangkok
ENV APPLICATION_MODE=DEV

# CMD tail -f /dev/null
CMD ["pdm", "run", "fastapi", "dev", "./src/codekids_crm_backend/main.py", "--host", "0.0.0.0"]