#!/bin/bash
lastMonth=$(($(date +"%s")-2592000))
for entry in "/var/pg/backups"/*
do
  filename=$(basename $entry)
  filename_no_extension="${filename%.*}"
  if [ $filename_no_extension -lt $lastMonth ]
  then
    rm $entry
  fi
done
