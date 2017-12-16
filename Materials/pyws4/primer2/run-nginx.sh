#!/bin/sh -x

#// START OMIT
docker run -d --rm \
    --name primer2-nginx \
    --net radionica \
    -v $(pwd)/primer2/primer2.conf:/etc/nginx/conf.d/default.conf \
    -p 9000:80 \
    nginx
#// END OMIT
