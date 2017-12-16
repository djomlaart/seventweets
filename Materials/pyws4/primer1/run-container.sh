#!/bin/sh -x

#// START OMIT
docker run --rm -d --name primer1 --net radionica -p 5000:5000 janos/radionica-primer1
#// END OMIT