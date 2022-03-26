FROM python:3.7-slim

EXPOSE 5000
# set work dir
WORKDIR /app
COPY . /app

# install nginx
RUN apt-get clean \
    && apt-get -y update

RUN apt-get -y install nginx \
    && apt-get -y install python3-dev \
    && apt-get -y install build-essential

# install requirements
RUN pip install -r requirements.txt

CMD python wsgi.py
