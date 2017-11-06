#!/bin/bash
kill -HUP `cat /tmp/gunicorn.pid`
