#!/bin/sh -x

#// START OMIT
docker run -t --rm --net radionica debian ping -c 3 radionica-postgres
#// END OMIT