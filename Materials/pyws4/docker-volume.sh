#!/bin/sh -x

#// START OMIT
echo "print('lokacija skripte', __file__)" > /tmp/script.py

docker run --rm -v /tmp:/app python:3 python /app/script.py
#// END OMIT