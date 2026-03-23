#!/bin/bash
set -e

# Read username and password from Docker secrets
username=$(< /run/secrets/mongo_db_user.txt)
password=$(< /run/secrets/mongo_db_password.txt)

# Define hosts and replica set config
hosts=("coredb:27017")

config="{ _id: \"rs0\", members: ["
for i in "${!hosts[@]}"; do
  config+="{ _id: $i, host: \"${hosts[$i]}\" }"
  if [ "$i" -lt $(( ${#hosts[@]} - 1 )) ]; then
    config+=", "
  fi
done
config+="] }"

# Run rs.initiate via mongo shell
mongosh -u "$username" -p "$password" --eval "rs.initiate($config)"

for host in "${hosts[@]}"; do
  mongosh -u "$username" -p "$password" --eval "rs.add('$host')"
done
