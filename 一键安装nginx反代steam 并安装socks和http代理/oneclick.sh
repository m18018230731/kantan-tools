#!/bin/bash

# nginx
firewall-cmd --add-port=80/tcp --permanent
# http
firewall-cmd --add-port=18779/tcp --permanent
# socks5
firewall-cmd --add-port=15055/tcp --permanent
firewall-cmd --reload  

yum install epel-release
yum -y install wget curl
# nginx
yum install nginx
wget https://raw.githubusercontent.com/m18018230731/kantan-tools/master/%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85nginx%E5%8F%8D%E4%BB%A3steam%20%E5%B9%B6%E5%AE%89%E8%A3%85socks%E5%92%8Chttp%E4%BB%A3%E7%90%86/nginx.conf
mv nginx.conf /etc/nginx/ -y
nginx -s reload
service nginx start
# tinyproxy
yum -y install tinyproxy
wget https://raw.githubusercontent.com/m18018230731/kantan-tools/master/%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85nginx%E5%8F%8D%E4%BB%A3steam%20%E5%B9%B6%E5%AE%89%E8%A3%85socks%E5%92%8Chttp%E4%BB%A3%E7%90%86/tinyproxy.conf
mv tinyproxy.conf /etc/tinyproxy/ -y
systemctl start tinyproxy.service
# socks5
wget https://raw.githubusercontent.com/qinghuas/socks5-install/master/socks5.sh;bash socks5.sh
socks5 install -y
socks5 user add rabproxy 12z991
socks5 start
# completed
echo "Completed!"