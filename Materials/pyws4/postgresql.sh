#!/bin/sh -x

#// START OMIT
docker run -d \
    --name radionica-postgres \
    --net radionica \
    --restart unless-stopped \
    -e POSTGRES_USER=radionica \
    -e POSTGRES_PASSWORD=P4ss \
    -v radionica-postgres-data:/var/lib/postgresql/data \
    -p 127.0.0.1:5432:5432 \
    postgres:9.6.2
#// END OMIT