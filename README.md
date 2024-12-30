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
* And, then run below to create tables in database!:
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
### View the Form in browser when browsing the url by editing migrations -> views.py:
* create "templates" directory in migrations folder and place html file to be used for view
* create views.py which contains index function to call/request index.html
* now, create file named urls.py containing urlpatterns path to be used and call our index.html in view
* include this path also in mysite -> urls.py
* NOW: refresh the browser to see the applied index.html on page! 

### Now, we get the values of Form entered in browser. We edit  views.py for "post request"
* import Form from .models to access arguments (first_name, last_nane,...) and create (Form.objects.create(first_name=first_name,...)) them (store into database)

### Send Email to the submitted user
* adding module "from django.core.mail import EmailMessage" into views.py
does the job!
* Then specify sender (gmail settigs) in settings.py 

### Add Admin Interface (Admin Panel) 
* in job_application -> admin.py 
from .module import Form and then admin.site.register(Form)
* Then: http://127.0.0.1:8000/admin 
* Create supper user admin account
* python3 manage.py createsupperuser
  (avakili -> G0dn...123)

### Customize admin Interface
* Create class like FormAdmin and add fields


### Create Base Template
* we create base.htl as template and remove extra tags from other files

