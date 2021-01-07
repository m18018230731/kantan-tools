#!/bin/bash

# 自定义域名
read -p "输入需要绑定的域名（不填则为不绑定域名）：" domain
# 判断是否需要安装 Socks5 代理
read -p "是否需要安装 Socks5 代理（0：否 1：是；默认为否）：" socks5_flg

# Nginx
firewall-cmd --add-port=80/tcp --permanent
# HTTP
firewall-cmd --add-port=18779/tcp --permanent
# Socks5
firewall-cmd --add-port=15055/tcp --permanent
firewall-cmd --reload  

yum -y update
yum -y install epel-release
# yum -y install wget curl -y

# Nginx
yum -y install nginx
# 如果不需要绑定域名
if [! -n ${domain}]; then
  wget https://raw.githubusercontent.com/m18018230731/kantan-tools/master/%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85nginx%E5%8F%8D%E4%BB%A3steam%20%E5%B9%B6%E5%AE%89%E8%A3%85socks%E5%92%8Chttp%E4%BB%A3%E7%90%86/nginx_ip.conf -O nginx.conf
else
  wget https://raw.githubusercontent.com/m18018230731/kantan-tools/master/%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85nginx%E5%8F%8D%E4%BB%A3steam%20%E5%B9%B6%E5%AE%89%E8%A3%85socks%E5%92%8Chttp%E4%BB%A3%E7%90%86/nginx_domain.conf -O nginx.conf
  sed -i 's/your_domain/${domain}/' nginx.conf
fi
mv -f nginx.conf /etc/nginx/nginx.conf
chmod 777 /etc/nginx/nginx.conf
nginx -s reload
service nginx start
systemctl enable nginx.service

# Tinyproxy
yum -y install tinyproxy
wget https://raw.githubusercontent.com/m18018230731/kantan-tools/master/%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85nginx%E5%8F%8D%E4%BB%A3steam%20%E5%B9%B6%E5%AE%89%E8%A3%85socks%E5%92%8Chttp%E4%BB%A3%E7%90%86/tinyproxy.conf
mv -f tinyproxy.conf /etc/tinyproxy/tinyproxy.conf
systemctl start tinyproxy.service
systemctl enable tinyproxy.service

# Socks5
if [-n ${socks5_flg}] || [test ${socks5_flg} -gt 0]; then
  wget https://raw.githubusercontent.com/qinghuas/socks5-install/master/socks5.sh;bash socks5.sh
  socks5 install
  socks5 user add rabproxy 12z991
  wget https://raw.githubusercontent.com/m18018230731/kantan-tools/master/%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85nginx%E5%8F%8D%E4%BB%A3steam%20%E5%B9%B6%E5%AE%89%E8%A3%85socks%E5%92%8Chttp%E4%BB%A3%E7%90%86/ss5
  mv -f ss5 /etc/init.d/ss5
  socks5 start
fi

# Completed
echo "Completed!"
