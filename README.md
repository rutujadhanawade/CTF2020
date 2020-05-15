# lakshya 2020



#### Running Locally 
Lakshya CTF is designed using the [Django framework](https://djangoproject.com). Building the project requires PIP3 and Python 3. It is recommended to install all the Python dependencies in a [virtual environment](https://pypi.org/project/virtualenv/). 

To get started, create a virtual environment - 

```bash

pip3 install virtualenv
virtualenv venv
source venv/bin/activate 
pip3 install django


```

Migrate the Django SQLite database before running the server. 

```bash
cd CTF2020/lakshya
python3 manage.py makemigrations  
python3 manage.py migrate
python3 manage.py runserver

```



## final update 
:star2: :star2: :star2: :star2: :star2: :star2: 


1. Qpage

- [x] submitting response
- [x] score updation
- [x] storing difficulty level
- [x] hint logic
     * [x] score updation
- [x] solved tag 
- [x] chart
- [x] colour models
- [x] timer


2. leaderboard
- [x] username, time, score printing
- [x] graph ...
- [x] submit time, pass time,
- [x] sorting according to score
- [x] sorting acc to time

3. [x] logout button

4. [x] SESSION

### update

1.~~INTEGRATION WITH frontend~~

- Home Page 
- Login Page
- Register Page
- Challenge / Quests Page
- 404 Not Found Page
- Leaderboard Page
- About / Rules Page
- Instructions Page   


2. Qpage
- rating for questions
- hint on question page 
   - score updation

3. leaderboard
   - graph
   - sorting according to score
   - sorting acc to time





## update 6/3/20

1. question page (first.html in our project)
   - ~~challenges should be displayed~~
   - ~~input field to accept the answer~~
   - ~~comparing~~
   - ~~score updation~~
   

2. leaderboard
   - ~~user name~~
   - ~~score~~
   - sorting according to score
   - sorting acc to time



4. ~~timer~~


