FROM python:3.5

ENV PYTHONUNBUFFERED=1
ENV WEBAPP_DIR=/MDC

RUN mkdir -p /var/log/gunicorn

RUN mkdir $WEBAPP_DIR

WORKDIR $WEBAPP_DIR

ADD requirements.txt $WEBAPP_DIR/
RUN pip install -r requirements.txt

ADD . $WEBAPP_DIR/

RUN python manage.py collectstatic --no-input
