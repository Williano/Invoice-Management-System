############################################################
# Dockerfile to build Django uWSGI Container
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu:16.04

# File Author / Maintainer
MAINTAINER Maintaner mpedigree tech team

# Update the repository and install some needed libraries
RUN apt-get update
RUN apt-get install python-pip -y \
                    libmysqlclient-dev -y \
                    python-dev -y \
                    supervisor -y \
                    uwsgi -y \
                    uwsgi-plugin-python -y \
                    build-essential -y \
                    && \
                    apt-get clean && \
                    rm -rf /var/lib/apt/lists/*

# Upgrade pip
RUN pip install --upgrade pip

## The enviroment variable ensures that the python output is set straight
## to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# Environment Variables
ENV SECRET_KEY %d#l!8i_*!qb!bd9i)^ie86a5x^4z6e!mu-03l%ujt54g72p&m
ENV NAME invoice
ENV USER mpedigree
ENV PASSWORD mpedigreepass
ENV HOST 192.168.33.10
ENV PORT 3306
ENV DEBUG False

# Create directory to house uwsgi logs
RUN mkdir -p /var/log/uwsgi
RUN chown -R root:root /var/log/uwsgi

RUN mkdir /Invoice_Management_System
WORKDIR /Invoice_Management_System
COPY . /Invoice_Management_System

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Exposed Ports
EXPOSE 8000
EXPOSE 9001

# Copy project supervisor configuration file to default location
COPY deploy/supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf

CMD ["/usr/bin/supervisord"]