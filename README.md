# Invoice Management System

## Getting Started
This section describes how to set up an environment to run and test the project.

### Prerequisites
* You have a working installation of Python 2.7.*
* You can install software on your system.
* You can create and activate Python virtual environments.

### Setup
Create a Python virtual environment somewhere on your system and activate it.
Your shell prompt should look something like this:
```
(env)[username@computer pwd]$
```

Clone this repository into the directory of your choice like so:
```
$ git clone https://github.com/Williano/Invoice-Management-System.git
```

`cd` into the project root directory and install the needed requirements.  
NB: Ensure that your virtual environment is activated.
```
$ cd Invoice-Management-System/
$ pip install -r requirements.txt
```

You will need to set the following environment variables. 
Open your .bashrc file
```shell
$ vim ~/.bashrc
```

and add the following 
```shell
export SECRET_KEY='{secure secret key}'
export NAME='{database name}'
export USER='{user}'
export PASSWORD='{user password}'
export HOST='{database host ip}'
export PORT='{database port}'

```

Setup the database by running the following.
```
$ python manage.py makemigrations
$ python manage.py migrate
```

### Running
When all is okay, you can start the local development server.
```
$ python manage.py runserver
```

Visit `localhost:8000` in your browser.

## Testing
Run the commands below to test the project and view the coverage.
```
$ coverage run --source='.' manage.py test
$ coverage report -m
```