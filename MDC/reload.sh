#!/bin/bash
docker-compose exec web kill -HUP `cat /tmp/gunicorn.pid`
