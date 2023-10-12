FROM python:3

RUN apt-get update && apt-get install -y default-libmysqlclient-dev

ENV PYTHONUNBUFFERED 1

WORKDIR /django

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:8000