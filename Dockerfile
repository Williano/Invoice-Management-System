FROM python:2

MAINTAINER Anthony A. Abeo <anthonyabeo@gmail.com>

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONUNBUFFERED 1

# create root directory for our project in the container
RUN mkdir /Invoice_Management_System

# Set the working directory to /Invoice_Management_System
WORKDIR /Invoice_Management_System

# Copy the current directory contents into the container at /Invoice_Management_System
COPY . /Invoice_Management_System/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Environment Variables
ENV SECRET_KEY %d#l!8i_*!qb!bd9i)^ie86a5x^4z6e!mu-03l%ujt54g72p&m
ENV NAME invoice
ENV USER mpedigree
ENV PASSWORD mpedigreepass
ENV HOST 192.168.33.10
ENV PORT 3306
ENV DEBUG True

# EXPOSE port 8000 to allow communication to/from server
# EXPOSE port 3306 to allow communication to/from MySQL
EXPOSE 8000
EXPOSE 3306

#CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
#ENTRYPOINT ["/usr/local/bin/uwsgi"]
RUN ["pip", "install", "uwsgi"]
CMD ["uwsgi", "--http", ":8000", "--chdir", "/Invoice_Management_System", "-w", "invoicemanager.wsgi", "--master", "--processes", "5"]
#CMD ["uwsgi", "--ini", "invoice.ini"]