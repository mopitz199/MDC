FROM postgres:9.5

# RUN apt-get update
# RUN apt-get install gnome-schedule -y
# RUN apt-get install nano -y

ADD cron /etc/cron.d/cron
ADD backup.sh /var/backup.sh
ADD clean-backup.sh /var/clean-backup.sh

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cron
RUN chmod 760 /var/backup.sh
RUN chmod 760 /var/clean-backup.sh

RUN /etc/init.d/cron start
