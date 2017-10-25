FROM postgres:9.5

# RUN apt-get update
# RUN apt-get install gnome-schedule -y
# RUN apt-get install nano -y

ADD cron-backup /etc/cron.d/cron-backup

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cron-backup
