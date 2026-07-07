FROM node:24-alpine3.21

WORKDIR /container

RUN npm install -g pnpm@11.10.0

COPY ./container/package.json .
COPY ./container/pnpm-lock.yaml .
RUN pnpm config set store-dir .pnpm-store
RUN pnpm install

COPY ./container .

EXPOSE 80
# CMD tail -f /dev/null
CMD ["pnpm", "dev", "--host", "0.0.0.0", "--port", "80"]