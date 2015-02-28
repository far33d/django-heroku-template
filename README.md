django-heroku-template
======================

A starting point for django environments on heroku. In order to get started do 3 things: 

Clone/Fork the repo and rename to PROJECTNAME.

```sh
git clone django_heroku_template PROJECTNAME
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

Make a new git repo (if you are me, since you can't fork your own stuff) and fix
the remote reference: 

```
git remote set-url origin git@github.com:far33d/PROJECTNAME.git
```

Someday I'll make a script to actually do all this. 

