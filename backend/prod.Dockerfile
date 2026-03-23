FROM python:3.14.3-alpine3.23


WORKDIR /working/backend/container
EXPOSE 8000

RUN pip install pdm
COPY ./container/pyproject.toml .
COPY ./container/pdm.lock .
COPY ./container/README.md .
RUN pdm install --prod

COPY ./container .



ENV TZ=Asia/Bangkok
ENV APPLICATION_MODE=PROD

# CMD tail -f /dev/null
CMD ["pdm", "run", "fastapi", "run", "./src/usoul_backend/main.py", "--workers", "8"]