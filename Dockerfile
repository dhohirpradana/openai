# syntax=docker/dockerfile:1

FROM python:3.8-slim-buster

WORKDIR /openai-question

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

RUN pip3 install -U flask-cors

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]