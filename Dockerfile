FROM python:3.12.0a1-alpine3.16

RUN apk update && apk upgrade

WORKDIR /app

ADD . /app

RUN pip3 install -r requirements.txt

CMD ["python3", "bloodhound_bot.py"]