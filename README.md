# How to run ( short manual)
### Clone project 
    $ git clone https://github.com/zxc322/vote_for_menu.git
### Simple way is to run docker-compose
###### Go to directory with docker-compose.yml and run
    $ docker-compose up --build -d
###### Create admin if needed
    $ docker exec -it django_app bash
    $ python manage.py createsuperuser
### And thats it, application is running

### Or for simple test w/o docker
###### in config/settings.py set (default=true)

###### it switch default db to sqlite and change redis url to localhost
        USE_DOCKER_and_POSTGRES = False
        
###### from directory with manage.py run

    $ docker run -d -p 6379:6379 redis
    $ pip install -r req.txt
    $ python manage.py makemigrations && python manage.py migrate
    $ python manage.py createsuperuser
    $ python manage.py runserver
    


### Few words about how app works

We can create 2 types of users (Employees and Restorators) to let them permissions for different actions.

Only restorators can create restaurants and only restaurant creator can create/update/delete menu of his restaurant.

Only employees can make a vote for a menu.

Every employee has a field (FK) which has a id of voted menu or None.

Every menu has a votes (IntField).

That 2 fields are setting to 0 everyday at midnight by celery. You can change it in config/settings.py
        CELERY_BEAT_SCHEDULE = {
            "sample_task": {
                "task": "menus.tasks.pruner",
                "schedule": crontab(minute=0, hour=0),
            },
        }

New day - new voting.
   
Since you start running app you can find urls documentation at 
        http://localhost/api/v2/swagger/

      
