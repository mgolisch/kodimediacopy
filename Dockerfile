
FROM python:2.7.12-wheezy
MAINTAINER mgolisch
LABEL Name=kodimediacopy Version=0.0.1 
RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD python run.py
