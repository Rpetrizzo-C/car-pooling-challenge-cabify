FROM python:3.8

# This Dockerfile is optimized for go binaries, change it as much as necessary
# for your language of choice.
EXPOSE 9091

COPY client/. car-pooling-challenge/

COPY requirements.txt car-pooling-challenge/

WORKDIR /car-pooling-challenge

RUN ls

RUN pip3 install -r requirements.txt

RUN python manage.py makemigrations

RUN python manage.py migrate

RUN chmod +x entrypoint.sh
 
ENTRYPOINT ["./entrypoint.sh"]
