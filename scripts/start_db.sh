#!/bin/bash

# this script starts Postgres DB in a Docker file
# db_name = 'online_store', username/password = 'postgres', port = '5432'
# don't forget to install `pip install "psycopg[binary]"` in your virtual env
# make the script executable chmod +x `start_db.sh`


docker run --name online_store -e POSTGRES_PASSWORD=postgres -d -p 5432:5432 postgres

# to start PgAdmin, you can comment out if not needed
# change the email & password, if you want
docker run --name test-pgadmin -p 15432:80 -e "PGADMIN_DEFAULT_EMAIL=oruns@duck.com" \
  -e "PGADMIN_DEFAULT_PASSWORD=postgres" -d dpage/pgadmin4:8.4


# other hints
# if a port is already in use, `sudo lsof -i :[PORT_NUMBER]` to find the PID
# then use 'sudo kill [PID]'
# hostname/address for connecting PGadmin to postgres docker server  `host.docker.internal`