#!/bin/bash
git https://github.com/we-race-here/wrh-web-components.git /home/jenkins/zp-results
cd /home/jenkins/zp-results
git checkout master

sudo cp -rf ../nginx.conf  /etc/nginx/nginx.conf
sudo cp -rf ../default.conf  /etc/nginx/sites-available/default
cp ../.env /home/jenkins/zp-results/zp_result/
pip install uwsgi
python manage.py collectstatic
python manage.py makemigrations migrate

# Restart nginx
sudo /etc/init.d/nginx start || sudo /etc/init.d/nginx start

# Running Server
uwsgi --socket mysite.sock --module zp_result.wsgi --buffer-size=100000 --chmod-socket=666 --master --processes 4 --threads 2