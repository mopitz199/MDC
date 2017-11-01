FROM postgres:9.5

ADD cron /etc/cron.d/cron
ADD backup.sh /var/backup.sh
ADD clean-backup.sh /var/clean-backup.sh
ADD postgresql.conf /etc/postgresql.conf

RUN mkdir /var/pg_log

# Give execution rights on the cron job
RUN chmod 0644 /etc/cron.d/cron
RUN chmod 760 /var/backup.sh
RUN chmod 760 /var/clean-backup.sh
RUN chmod 777 /var/clean-backup.sh
RUN chown -R postgres:postgres /var/pg_log

RUN /etc/init.d/cron start

CMD ["postgres", "-c", "config_file=/etc/postgresql.conf"]
