django-heroku-template
======================

A starting point for django environments on heroku. In order to get started do 3 things: 

Fork this repo and to a new repo called PROJECTNAME.

If you are me (the owner of this repo) you can't fork in github, so: 

* create a new repo 
* clone it locally

Then add this project as an upstream source and fetch / merge:

```sh
git remote add upstream https://github.com/far33d/django-heroku-template.git
git fetch upstream
git merge upstream/master
```

move the django\_heroku\_template directory to PROJECTNAME

```sh
cd PROJECTNAME
git mv django_heroku_template PROJECTNAME
```

Find and replace any instance of django_heroku_template to PROJECTNAME in all files. 
As of now, the only files affected are:

```
./PROJECTNAME/settings.py
./PROJECTNAME/urls.py
./PROJECTNAME/wsgi.py
./manage.py
./Procfile
```

Create a database in postgres, and add a .env file in root directory to tell foreman
where to look for the local database. Contents of .env file should be:

```
DATABASE_URL=postgres://localhost/DATABASE_NAME
```

Set up a virtualenv, activate it, and install all dependencies. 
```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt --allow-all-external
```

Here's some info on forking your own stuff.... 

http://bitdrift.com/post/4534738938/fork-your-own-project-on-github

Someday I'll make a script to actually do all this. 


