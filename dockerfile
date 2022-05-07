# pull the official docker image
FROM ubuntu:latest
FROM python:3.10.4-buster

# set work directory
WORKDIR /app

# set env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY requirements.txt .
COPY requirements_dev.txt .
COPY requirements_test.txt .
RUN apt-get -y update && apt-get -y upgrade
#RUN apt-get install -y cron vim
RUN apt-get install gcc libc-dev g++ libffi-dev libxml2 libffi-dev unixodbc-dev -y
RUN pip install -r requirements.txt
RUN pip install -r requirements_test.txt
RUN pip install -r requirements_dev.txt