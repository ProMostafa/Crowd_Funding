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
![][3] \
![][4] \
![][5] \
![][6] \


[1]: https://github.com/ProMostafa/Crowd_Funding/blob/master/1.png
[2]: https://github.com/ProMostafa/Crowd_Funding/blob/master/2.png
[3]: https://github.com/ProMostafa/Crowd_Funding/blob/master/3.png
[4]: https://github.com/ProMostafa/Crowd_Funding/blob/master/4.png
[5]: https://github.com/ProMostafa/Crowd_Funding/blob/master/5.png
[6]: https://github.com/ProMostafa/Crowd_Funding/blob/master/6.png
