#!/bin/sh -x

#// START OMIT
docker run --rm -d --name primer2 --net radionica -p 8000:8000 janos/radionica-primer2
#// END OMIT