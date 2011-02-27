Django project boilerplate
===========================

:Authors:
   Jori Lallo
:Version: 0.1


This is a simple Django project boilerplate which I use for my hobby and prototyping projects. Please keep in mind that this made using personal prefences and it doesn't work for everyone. This is also the first release and it's not perfect by any means. Comments are welcome!

Few things it provides

 * ``Main app``. I usually use only one app which has the basic logic of the project. If there's more stuff then it's easier to slice specific parts into their own apps (or slide and dice within the ``main`` app)
 * ``CleverCSS``. Project includes forked django-css and CleverCSS libraries so that you can write beatiful CSS from the start. Read more about them here: http://blog.clear.com.ua/2009/09/clevercss/
 * ``960.gs & Toucan CSS Reset``. These come from personal preference: 960.gs is nice and widely used and Toucan provides beatiful resets to go with it
 * ``UserProfile``. Basic user profile with ``user.profile`` binding is added. And the whole main app uses South for migration so just add your own fields
 * ``Settings goodies``. Settings.py includes my favourite path settings and probably not so elegant DEBUG swithing based on hostname (you might be better off using local_settings.py)
 
Added apps
===========

This project includes the following apps that I use with all of my projects:

 * ``django-annoying``. Seriously, must have
 * ``South``. Model migrations
 * ``django-robots``. robots.txt management
 * ``johnny-cache, postmark``. *(Recommended)* Didn't add these but there's some settings available for them


Installation
=============

This is how you get started::

    git clone git://github.com/jorde/django_boilerplate.git
    cd django_boilerplate
    pip install -r requirements.txt # sudo this
    python manage.py syncdb
    python manage.py migrate
    python manage.py runserver

If all goes well your new project will be available at http://127.0.0.1:8000/
    
Before this I highly recommend that you use virtuelenv for your project. Also remember to change following stuff for your project.

 * Rename the folder to reflect your project
 * In ``settings.py`` change ``ROOT_URLCONF`` to match your project name

TODO
=====

* Switch to use local_settings.py
* Add apache configs and fabric deploy scripts
