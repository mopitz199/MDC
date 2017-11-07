#!/bin/bash
now=$(date +"%s")
name="$now.dump"
dir="/var/pg/backups/$name"
pg_dump -U admin -Fc base_datos -f $dir
