# Django / Tirsvad CMS Skeleton

[![Build Status](https://travis-ci.org/TirsvadCMS/skeleton.svg?branch=master)](https://travis-ci.org/TirsvadCMS/skeleton)

## Futures
Site skeleton with following
* User login
* Ready Bootstrap-themed pages
* Navigation bar
* Multilanguages
* Templates
* Static files collection to static root

## Todo
* User Registration/Sign up
* Change language

## Usage
##### Prerequirements
    Install virtualenv and active it
    $ pip install django
##### setup
1. `$ django-admin.py startproject --template=https://github.com/TirsvadCMS/skeleton/archive/master.zip --extension=py my_project`
2. `$ cd my_project`
3. `$ pip install -r requirements.txt `
4. `$ python manage.py migrate`
5. `$ python manage.py collectstatic`
6. `$ python manage.py runserver` See if it's runing

### Use Bash Script to install
It will install VirtualEnv Django and Tirsvad CMS Sḱeleton.

Edit the file where it's say change me.

https://github.com/TirsvadCMS/BashScript-GetSkeleton/raw/master/get_skeleton.sh