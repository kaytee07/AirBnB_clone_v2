#!/usr/bin/env bash
# setup servers for the deployment of web_static.


if ! command -v "nginx" >/dev/null;
then
    sudo apt update
    sudo apt install -y nginx
fi
sudo mkdir -p /data/web_static/releases/test/
sudo mkdir -p /data/web_static/shared/


printf %s "<html> \n
<head> \n
<title>Taylor</title> \n
</head> \n
<body> \n
<h1>Hello Taylor</h1> \n
</body> \n
</html>
" > /data/web_static/releases/test/index.html

sudo rm -rf /data/web_static/current
sudo mkdir /data/web_static/current
sudo ln -sf /data/web_static/releases/test/ /data/web_static/current

chown -R ubuntu /data/
chgrp -R ubuntu /data/

printf %s "server {
   listen 80 default_server;
   listen [::]:80 default_server;

   location / {
      root /var/www/html/;
      index index.html;
   }

   location /hbnb_static {
        alias /data/web_static/current;
        index index.html index.htm;
    }

   location /redirect_me {
      return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
   }

   error_page 404 /404.html;
   location = /404.html{
      internal;
   }

   add_header X-Served-By \$hostname;

}" > /etc/nginx/sites-available/default

sudo service nginx restart
