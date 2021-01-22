# Crowd Funding

### how to install on linux ubuntu

Suposed you have installed python3, virtual environment module and pip. 

```shell
Crowd-Funding-Web-app$ python3 -m venv .venv
Crowd-Funding-Web-app$ source .venv/bin/active
Crowd-Funding-Web-app$ pip3 install -r requirements.txt
```
After that you have to update settings.py file to adjust database configration.


Then migrate database
```shell
Crowd-Funding-Web-app$ python3 manage.py makemigrations
Crowd-Funding-Web-app$ python3 manage.py migrate
Crowd-Funding-Web-app$ python3 manage.py runserver
```
### Snippest from Project
![][1] \
![][2] \
![][3]


[1]: 
[2]: 
[3]: 
