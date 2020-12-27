# Sending-Mail-in-django_Using-Gmail
Project Structure:

[summergeek]/                  <- project root
├── [summergeek]/              <- Django root
│   ├── __init__.py
│   ├── settings.py
│   │── urls.py 
│   │── wsgi.py│   
│  
├── assignment/
│   └── __init__.py
|   │__apps.py
|   │__models.py
|   |__admin.py
|   |__urls.py
|   |__tests.py
|   |__views.py
|   |
|   |__templates/
|      |__index.html
|   |
└── manage.py

In the above project structure in settings.py we need to put in host email details for send_email to work
Also we need zerosms account credentials for sms to work.

Requirements:
1.zerosms package
2.python3
3.django(latest version)

Also we will need to setup host email so that it allows emails to be sent.

