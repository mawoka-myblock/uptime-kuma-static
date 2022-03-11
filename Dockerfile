FROM python:3.9

RUN apt-get update && apt-get install -y cron
RUN crontab -l | { cat; echo "*/1 * * * *  sh -c cd /app python3 /app/main.py"; } | crontab -
RUN crontab -l | { cat; echo "@reboot cd /app && python3 /app/main.py"; } | crontab -
ENV RUNTIME=docker

# Create actual app
RUN mkdir /app
RUN mkdir /app/out
COPY main.py /app
COPY templates/ /app/templates
COPY requirements.txt /app
WORKDIR /app
RUN pip install -r requirements.txt
# CMD ["python3","main.py"]
# SHELL ["cd", "/app", "&&", "python3", "/app/main.py"]
CMD cd /app && python3 main.py
# CMD /usr/sbin/cron -f -l 8
#CMD ["/usr/sbin/cron", "-f"]
# CMD ["python3", "main.py"]