#FROM nginx
#
#MAINTAINER Anthony Abeo <anthonyabeo@gmail.com>
#
##COPY nginx.conf /etc/nginx/nginx.conf
#RUN mkdir /docker_nginx
#
#WORKDIR /docker_nginx
#
#COPY . /docker_nginx
#
#COPY nginx.conf /etc/nginx/sites-available/
#
#EXPOSE 80
#
#RUN mkdir /etc/nginx/sites-enabled
#
#RUN ["ln", "-s", "/etc/nginx/sites-available/nginx.conf", "/etc/nginx/sites-enabled"]
#
#RUN nginx -t

############################################################
# Dockerfile to build Nginx Installed Containers
# Based on Ubuntu
############################################################

# Set the base image to Ubuntu
FROM ubuntu:16.04

# File Author / Maintainer
MAINTAINER Maintaner Name

# Update the repository
RUN apt-get update

# Install necessary tools
RUN apt-get install -y nano wget dialog net-tools

# Download and Install Nginx
RUN apt-get install -y nginx

# Remove the default Nginx configuration file
RUN rm -v /etc/nginx/nginx.conf

# Copy a configuration file from the current directory
ADD nginx.conf /etc/nginx/

# Append "daemon off;" to the beginning of the configuration
#RUN echo "daemon off;" >> /etc/nginx/nginx.conf

# Expose ports
EXPOSE 80

RUN nginx -t

# Set the default command to execute
# when creating a new container
CMD service nginx start