# Invoice Management System

## Table of contents
* [Getting Started](#getting-started)
* [Setup](#setup)
* [Features](#features)
* [Testing](#testing)
* [Contributing](#contributing)

## Getting Started
This section describes how to set up an environment to run and test the project.

## Setup


### Using Python virtualenv

#### Prerequisites
* You have a working installation of Python 2.7.*
* You can install software on your system.
* You can create and activate Python virtual environments.
Create a Python virtual environment somewhere on your system and activate it.
Your shell prompt should look something like this:
```shell
(env)[username@computer pwd]$
```

Clone this repository into the directory of your choice like so:
```shell
$ git clone https://github.com/Williano/Invoice-Management-System.git
```

`cd` into the project root directory and install the needed requirements.  
NB: Ensure that your virtual environment is activated.
```shell
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
```shell
$ python manage.py migrate
```


### Running
When all is okay, you can start the local development server.
```shell
$ python manage.py runserver
```

Visit `localhost:8000` in your browser.


### Using Docker
You can build and run the app using Docker containers. This requires minimal setup.

#### Prerequisites
Make sure you have Docker a Docker-compose installed. Follow the URLs
below to install for the appropriate system.

[Installing docker-compose]([GitHub](http://github.com))  
[Installing docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/#install-docker-ce-1)

After installation you can verify that it is installed by running
```shell
$ sudo docker version
```
It should display something like this if successful:
```
Client:
 Version:           18.06.1-ce
 API version:       1.38
 Go version:        go1.10.3
 Git commit:        e68fc7a
 Built:             Tue Aug 21 17:25:13 2018
 OS/Arch:           linux/amd64
 Experimental:      false

Server:
 Engine:
  Version:          18.06.1-ce
  API version:      1.38 (minimum version 1.12)
  Go version:       go1.10.3
  Git commit:       e68fc7a
  Built:            Tue Aug 21 17:27:37 2018
  OS/Arch:          linux/amd64
  Experimental:     false
```

Now clone the repository and `cd` into `deploy` directory inside the root of 
the project. 
```
$ cd Invoice-Management-System
```

Now run to build and start running the containers.
```
$ docker-compose build --no-cache
$ docker-compose up --no-start --force-recreate
$ docker-compose start
```
Then visit `127.0.0.1` in your browser.  
Supervisor will be running on `127.0.0.1:9001`. If prompted for username and password,
use the following:
```
username: mpedigree
password: mpedigree
``` 


## Features

## Testing
Run the commands below to test the project and view the coverage.
```shell
$ coverage run --source='.' manage.py test
$ coverage report -m
```
To exclude the virtualenv folder do the following:
```shell
$ coverage run --omit ve  --source="." manage.py  test
```
In the above example "ve" is the name of the virtualenv.


## Contributing

1. Fork it (<https://github.com/Williano/Invoice-Management-System.git>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request
