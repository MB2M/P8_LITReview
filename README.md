# P8_LITReview
    
*This repository hosts a project to achieve during my training OpenClassRooms.com*

This script was created on Python 3.9 and use the Django framework in its 3.1.5 version.

The purpose of this application is to manage a book's review.
Users can login post and ask for reviews.


## Installation

Download the files in the directories of your choice

### 1) Create a Virtual Environment :
 
Go to the directory where you downloaded files and run this command on your terminal:

    python3 -m venv env
    
Then, initialize it :
 
- On Windows, run:

        env\Scripts\activate.bat
    
- On Unix or MacOS, run:

        source env/bin/activate
        
For more information, refer to the python.org documentation :

<https://docs.python.org/3/tutorial/venv.html>
    
### 2) Install the requirements

Still on you terminal, with the environment activated, run the following command to install the required libraries
    
    pip install -r requirements

### 3) Start the server

Go to the litreview/ repository and start the server using command:

    python manage.py runserver

Server is now running on

    http://127.0.0.1:8000/
    
### 4) Connect as an admin:

Login as an admin  using one of those 2 links:

<http://127.0.0.1:8000/admin/>
<http://127.0.0.1:8000/accounts/login/>

login: admin
password: admin

### 5) Django administration

Go to <http://127.0.0.1:8000/admin/>

### 6) 

You have to be logged to use this application.

You can:
    - register / login / disconnect
    - ask for a review
    - publish a review
    - Follow other user


