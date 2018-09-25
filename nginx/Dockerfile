FROM ubuntu:16.04

MAINTAINER Anthony Abeo <anthonyabeo@gmail.com>

#COPY invoice.conf /etc/nginx/nginx.conf
RUN mkdir /docker_nginx

WORKDIR /docker_nginx

COPY . /docker_nginx

COPY invoice.conf /etc/nginx/sites-available/

EXPOSE 80

RUN mkdir /etc/nginx/sites-enabled

RUN ["ln", "-s", "/etc/nginx/sites-available/invoice.conf", "/etc/nginx/sites-enabled/"]

