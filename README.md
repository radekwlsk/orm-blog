# Django ORM tips&tricks demo app

This application was created to present database schema and 
allow trying out concepts from [*Django ORM tips&tricks* 
presentation](https://docs.google.com/presentation/d/1ApNBIzdBbAc9FTzeO2kGINDS5EuUQQlF2LadPY7_vso/edit?usp=sharing) from [**wroc.py** meetup on June 2, 2020](https://www.meetup.com/en-AU/wrocpy/events/fzctlrybcjbdb/).

## How to use

### Build

Application is dockerized, to run it make sure that you have 
Docker and `docker-compose` installed and configured properly.

Run in projects root directory:
```bash
$ docker-compose build
```

Setup the database tables:
```bash
$ docker-compose run --rm app ./manage.py migrate
```


### Run

To startup the application run
```bash
$ docker-compose up
```
You can then use it like regular Django application (but 
**you shouldn't** as there is nothing more than the database 
schema defined in this app).


### Play
To try out the queries and see the SQL representation run 
Django shell with:
```bash
$ docker-compose run --rm app ./manage.py shell
```

In the shell execute following commands:
```python
from orm_blog.blog.models import BlogPost, Author, Category, Comment
from django.db import connection, reset_queries
```

Now you have access to the app's Django Models and you can monitor 
queries (make sure that `DEBUG` setting is `True`, which is the 
default when running locally).

You can execute queries and check the raw SQL executed with:
```python
# execute query
BlogPost.objects.values("title")
# print queries
connection.queries
# to reset queries list run
reset_queries()  
 ```

Full shell execution look like following:
```python
In [2]: from orm_blog.blog.models import BlogPost, Author, Category, Comment           

In [3]: from django.db import connection, reset_queries                                

In [4]: BlogPost.objects.values("title")                                               
Out[4]: <QuerySet []>

In [5]: connection.queries                                                             
Out[5]: 
[{'sql': 'SELECT "blog_blogpost"."title" FROM "blog_blogpost" LIMIT 21',
  'time': '0.005'}]

In [6]: reset_queries()                                                                

In [7]: connection.queries                                                             
Out[7]: []
``` 
