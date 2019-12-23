#/bin/sh
# CMD to be run at the devops-main container's creation
service nginx start
python3 /usr/share/nginx/html/Devops/manage.py db init
python3 /usr/share/nginx/html/Devops/manage.py db migrate
python3 /usr/share/nginx/html/Devops/app.py
