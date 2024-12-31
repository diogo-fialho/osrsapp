#!/bin/bash
TIMESTAMP=$(date +"%F_%T")
BACKUP_DIR="$1"
DAYS_OLD=$3
mkdir -p "$BACKUP_DIR"

echo "creating backup"
mongodump --host=$2 --out="$BACKUP_DIR/$TIMESTAMP"

echo "cleaning up older files"
find $BACKUP_DIR -mindepth 1 -maxdepth 1 -type d -mtime +$DAYS_OLD -exec sh -c 'echo Removing: {}; rm -rf {}' \;