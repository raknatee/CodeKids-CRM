FROM mongo:8.2.6-noble


# RUN apt-get install python3 -y

COPY ./mongodb-keyfile /run/secrets/mongodb-keyfile

RUN chown 999:999 /run/secrets/mongodb-keyfile
RUN chmod 600 /run/secrets/mongodb-keyfile

COPY ./setmongo.sh .

COPY ./mongod.conf /etc/mongod.conf

CMD ["mongod", "--replSet", "rs0", "--bind_ip_all", "--keyFile", "/run/secrets/mongodb-keyfile", "--config", "/etc/mongod.conf"]