# Usage 

## Install python, pip, virtual-environment

1. install python 3.6
2. install virtualenv:

##### Install **pip** first

    sudo apt-get install python3-pip

##### Then install **virtualenv** using pip3

    sudo pip3 install virtualenv 

##### Now create a virtual environment 

    virtualenv venv 

>you can use any name insted of **venv**

##### You can also use a Python interpreter of your choice

    virtualenv -p /usr/bin/python2.7 venv
  
## Active your virtual environment:    
    
    source venv/bin/activate

## Clone project repository

    git clone https://github.com/rupesh2120/DjangoLibraryApplication.git

## Enter into project directory

    cd DjangoLibraryApplication/

## Install dependencies

    pip install -r requirement.txt 

## Migrate database

    python manage.py migrate

## Create admin/superuser

    python manage.py createsuperuser
    >Username [enter your username]
    >Password [enter your password]

## Run server @localhost

    python manage.py runserver

## Now access development server at http://127.0.0.1:8000/




# Deploying application on heroku platform

1. Create your own account on https://www.heroku.com/
2. install heroku cli 

    https://devcenter.heroku.com/articles/heroku-cli
3. Getting started 

    $ heroku login
    >Enter your Heroku credentials.

### Configure Django for Heroku

1. For the Django app to work on Heroku, some Heroku specific configuration is required:
Add a Procfile to let Heroku know how to start your app:

        echo "web: gunicorn django_tasklist.wsgi --log-file -" Procfile

    in case of our application it will be

        echo "web: gunicorn ProjectMDN.wsgi --log-file -" Procfile


2. install required package in next step 

        pip install django_heroku
        pip install pipenv
        pip install gunicorn
        pip freeze > requirements.txt
        


3. Add the Heroku specific configuration to the settings which the Django app requires in order to work on Heroku, mainly for the database to work and the static files to be served. Luckily, there is a django-heroku package that takes care of all that. So on the bottom of the file django_tasklist/settings.py add the following lines:

        import django_heroku
        django_heroku.settings(locals())



4. create pipfile

        pipenv install

5. Update pipfile as follows

        [[source]]
        url = "https://pypi.org/simple"
        verify_ssl = true
        name = "pypi"
        [packages]
        django = "*"
        gunicorn = "*"
        django-heroku = "*"
        [requires]
        python_version = "3.6"

6. Update pipfile 

  (reference: https://stackoverflow.com/questions/49460486/pipfile-lock-out-of-date)

        pipenv lock
        pipenv install
        pipenv lock




# Final step: Deploy on Heroku

Our code needs to be added to a git repository before it can be deployed to Heroku. First, edit .gitignore and adding the following lines to exclude unnecessary files:

    venv
    *.pyc
    db.sqlite3

Then initialize a git repository and make a commit:

    git init
    git add .
    git commit -m "Empty django app"

Now, create a Heroku app using heroku create:

    heroku create
    Creating app... done, ⬢ blooming-ridge-97247
    https://blooming-ridge-97247.herokuapp.com/ | 
    https://git.heroku.com/blooming-ridge-97247.git

And then deploy the app:

    git push heroku master

Finally, you can use the Heroku CLI to view the app in your browser:

    heroku open


# References

### Django-MDN-Tutorials
https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django


### Scaling a Django Application with Memcache

https://devcenter.heroku.com/articles/django-memcache

### Deploying Python and Django Apps on Heroku

https://devcenter.heroku.com/articles/deploying-python

### Getting Started on Heroku with Python

https://devcenter.heroku.com/articles/getting-started-with-python
  
