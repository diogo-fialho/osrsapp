#!/bin/bash
TIMESTAMP=$(date +"%F_%T")
BACKUP_DIR="/backup"
mkdir -p "$BACKUP_DIR"
mongodump --host=mongodb --out="$BACKUP_DIR/$TIMESTAMP" -d osrs_api
