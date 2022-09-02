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
   
