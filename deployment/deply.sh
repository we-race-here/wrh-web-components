#!/bin/bash
git clone https://github.com/vincentdavis/zp-results.git /home/jenkins/zp-results
cd /home/jenkins/zp-results
git checkout main
mkdir -p media

sudo cp -rf ../nginx.conf  /etc/nginx/nginx.conf
sudo cp -rf ../default.conf  /etc/nginx/sites-available/default
cp ../.env /home/jenkins/zp-results/zp_result/
cp ../ca-certificate.crt /home/jenkins/zp-results/
pip install uwsgi
python manage.py collectstatic

# Restart nginx
sudo /etc/init.d/nginx start || sudo /etc/init.d/nginx start

# Running Server
uwsgi --socket mysite.sock --module zp_result.wsgi --buffer-size=100000 --chmod-socket=666 --master --processes 4 --threads 2