FROM python:2.7

MAINTAINER mpedigree tech team

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

RUN mkdir -p /var/log/uwsgi
RUN chown -R root:root /var/log/uwsgi

RUN mkdir /Invoice_Management_System
WORKDIR /Invoice_Management_System
COPY .. /Invoice_Management_System

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

RUN pip install uwsgi

EXPOSE 8000

CMD ["uwsgi", "--ini", "deploy/invoice.ini"]