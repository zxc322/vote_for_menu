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
### Few words about how app works

We can create 2 types of users (Employees and Restorators) to let them permissions for different actions.

Only restorators can create restaurants and only restaurant creator can create/update/delete menu of his restaurant.

Only employees can make a vote for a menu.

Every employee has a field (FK) which has a id of voted menu or None.

Every menu has a votes (IntField).

That 2 fields are setting to 0 everyday at midnight by celery.

New day - new voting.
   
Since you start running app you can find urls documentation at 
        http://localhost/api/v2/swagger/

      
