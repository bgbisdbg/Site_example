FROM python:3.11
WORKDIR /site
COPY . /site
RUN apt-get -y update \
    &&apt-get -y upgrade \
    &&apt-get -y install python3-pip\
    &&pip install -r requirements.txt
WORKDIR /site/my_store

