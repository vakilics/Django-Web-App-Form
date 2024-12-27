## Create django project!
* django-admin startproject mysite .
## create new app named job_application
* python3 manage.py startapp job_application
### In pycharm:
* Register this app: mysite -> settings.py -> change "INSTALLED_APPS" and add  "'job_application',"
* python3 manage.py runserver

### In django, we do bottom-up approach! so start with database model
* after creating class "Form" from models, we run migrations to create python code which later can 
create table.  
```
# python3 manage.py makemigrations
Migrations for 'job_application':
  job_application/migrations/0001_initial.py
    - Create model Form
```
* Now, code for migration is ready in job_application -> migrations -> 0001_initial.py
* And, then run below to create tables in databse!:
```
python3 manage.py migrate

Operations to perform:
  Apply all migrations: admin, auth, contenttypes, job_application, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK

...
```
## view the Form in browser when browsing the url by editing migrations -> views.py:
* create "templates" directory in migrations folder and place html file to be used for view
* create views.py which contains index function to call/request index.html
* now, create file named urls.py containing urlpatterns path to be used and call our index.html in view
* include this path also in mysite -> urls.py
* NOW: refresh the browser to see the applied index.html on page! 