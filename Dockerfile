FROM python:3.9.7-alpine3.14


RUN apk add --no-cache build-base
RUN crontab -l | { cat; echo "*/1 * * * *  cd /app && python3 main.py"; } | crontab -
RUN crontab -l | { cat; echo "@reboot  cd /app && python3 main.py"; } | crontab -
ENV RUNTIME=docker

# Create actual app
RUN mkdir /app
RUN mkdir /app/out
COPY main.py /app
COPY templates/ /app/templates
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN apk del build-base
CMD ["crond", "&&", "tail", "-f", "/var/log/cron.log"]
