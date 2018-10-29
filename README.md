# NFC BLOG

##Django 2.0 Blog site

[Demo](https://nfcblog.herokuapp.com)

>About

This is a demo project for practicing Django. The idea was to build some basic blogging platform.

It was made using ```Python 3.6 + Django``` and database is ```SQLite.``` ```Bootstrap``` was used for styling. Testing is done using untitest module.

There is a 
```
* login
* registration
* password change
* password reset
* Django CKeditor
* disqus comment 
* django crispy form
```
functionality included.

User has his own blog page, where he can add new blog posts. Home page is paginated list of all posts. Non-authenticated users can cannot add new posts but adding comment in any post.

App is covered with tests.
Prerequisites

[Optional] Install virtual environment:

```$ python -m virtualenv env```

[Optional] Activate virtual environment:

On macOS and Linux:

```$ source env/bin/activate```

On Windows:

$ .\env\Scripts\activate

Install dependencies:

```$ pip install -r requirements.txt```

How to run
Default

You can run the application from the command line with ```manage.py```. Go to the root folder of the application.

Run migrations:

```$ python manage.py migrate```

Run server on port 8000:

```$ python manage.py runserver 8000```

Post Installation

Go to the web browser and visit http://localhost:8000

Admin username: 

Admin password: 

User username: 

User password: 

Helper Tools
Django Admin

It is possible to add additional admin user who can login to the admin site. Run the following command:

```$ python manage.py createsuperuser```

Enter your desired username and press enter.
```
Username: admin_username
```
You will then be prompted for your desired email address:
```
Email address: admin@example.com
```
The final step is to enter your password. You will be asked to enter your password twice, the second time as a confirmation of the first.
```python
Password: **********
Password (again): *********
Superuser created successfully.
```
Go to the web browser and visit ```http://localhost:8000/admin```

Tests
Default

Activate virtual environment:

On macOS and Linux:
```
$ source env/bin/activate
```
On Windows:
```
$ .\env\Scripts\activate
```
Running tests:
```
$ python manage.py test blog
```
