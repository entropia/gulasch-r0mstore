Almost secret deployment battle plan
====================================

1. Install dependencies: ```aptitude install python3 virtualenv python3-virtualenv libjpeg-dev zlib1g-dev libtiff-dev libtiff-dev libwebp-dev libopenjpeg-dev python3-dev```
1. Create linux user for running the romstore ```adduser --disabled-login romstore```
2. Create database + database user
  - postgres
    ```
    su postgres
    createuser -D -P -S romstore
    createdb -O romstore romstore
    ```
3. ```git clone https://github.com/LongHairedHacker/gulasch-r0mstore/```
4. ```virtualenv -p python3 virtenv; source virtenv/bin/activate```
5. ```pip install -r requirements.txt```
6. Generate new secret key and set it in gulashromstore/settings.py: ```pwgen -sy 64 5```
8. Setup database in gulashromstore/settings.py
  - Mysql:
    - ```pip install mysqlclient```
    - Follow: https://docs.djangoproject.com/en/1.11/ref/databases/#connecting-to-the-database
  - Postgres:
    - ```pip install psycopg2```
    - Refer to example configuration https://docs.djangoproject.com/en/1.11/ref/settings/#databases
9. Setup mail configuration https://docs.djangoproject.com/en/1.11/ref/settings/#email
10. ```manage.py migrate```
11. ```manage.py createsuperuser```
12. ```manage.py collectstatic```
13. Set up a uswgi configuration (use systemd/uwsgi.ini)
    - update paths
    - update user/group ids
15. Setup systemd service and socket files
14. Setup nginx, see https://uwsgi.readthedocs.io/en/latest/tutorials/Django_and_nginx.html#configure-nginx-for-your-site
    - set paths for media, static and the socket
    - make sure static points to static_root not static
15. Testrun without ssl
15. Setup ssl
16. Change DEBUG to False in gulashromstore/settings.py
