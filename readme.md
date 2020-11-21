
[![Open in Gitpod](https://gitpod.io/button/open-in-gitpod.svg)](https://gitpod.io/#env=staging/https://github.com/uwidcit/pharm-backend)

# Pharm Backend
Backend application for pharmacy application

# Dependencies
* Python3/pip3
* Packages listed in requirements.txt

# Installing

```
$ pip3 install -r requirements.txt
```

# Connected Services

# Credentials

# Running the Project
Ensure the environment varable ENV is either set to 'staging' or 'production' then execute the following command
```
$ python3 -m App.main
```

# Deploying
App is configured to auto deploy master branch to heroku at [https://uwipharm.herokuapp.com](https://uwipharm.herokuapp.com)

# Intializing the Database
When connecting the project to a fresh empty database ensure the appropriate database credentials are set in environment.staging.json file then run the following command.
```
$ python3 manage.py initdb
```

# Database Migrations
If changes to the models are made, the database must be'migrated' so that it can be synced with the new models.
Then execute following commands using manage.py. More info [here](https://flask-migrate.readthedocs.io/en/latest/)

```
$ python3 manage.py db init
$ python3 manage.py db migrate
$ python3 manage.py db upgrade
$ python3 manage.py db --help
```