FROM mongo:latest

# Install cron
RUN apt-get update && apt-get install -y cron

# Copy the backup script
COPY backup.sh /usr/local/bin/backup.sh
RUN chmod +x /usr/local/bin/backup.sh

# Add cron job
RUN echo "0 23 * * * /usr/local/bin/backup.sh /backup mongodb 5 >> /var/log/backup.log 2>&1" > /etc/cron.d/mongo-backup \
    && chmod 0644 /etc/cron.d/mongo-backup \
    && crontab /etc/cron.d/mongo-backup

# Start cron in the foreground
CMD ["cron", "-f"]
