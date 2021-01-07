#!/bin/bash

# 参数读取
if [ "$1" = "" ] || [ $1 = 0 ]; then
  echo "不绑定域名"
  wget https://raw.githubusercontent.com/m18018230731/kantan-tools/master/%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85nginx%E5%8F%8D%E4%BB%A3steam%20%E5%B9%B6%E5%AE%89%E8%A3%85socks%E5%92%8Chttp%E4%BB%A3%E7%90%86/nginx_ip.conf -O nginx.conf
else
  echo "绑定域名：$1"
  wget https://raw.githubusercontent.com/m18018230731/kantan-tools/master/%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85nginx%E5%8F%8D%E4%BB%A3steam%20%E5%B9%B6%E5%AE%89%E8%A3%85socks%E5%92%8Chttp%E4%BB%A3%E7%90%86/nginx_domain.conf -O nginx.conf
  sed -i "s/your_domain/$1/" nginx.conf
fi
if [ "$2" = "" ] || [ $2 = 0 ]; then
  echo "不需要安装 Socks5"
else
  echo "已选择需要安装 Socks5"
fi

# 事前准备
setenforce 0
sed -i 's/SELINUX=enforcing/SELINUX=disabled/' /etc/selinux/config
yum -y install epel-release

# Nginx 安装
yum -y install nginx
mv -f nginx.conf /etc/nginx/nginx.conf
chmod 777 /etc/nginx/nginx.conf
nginx -s reload
systemctl start nginx.service
systemctl enable nginx.service
firewall-cmd --add-port=80/tcp --permanent

# Tinyproxy 安装
yum -y install tinyproxy
wget https://raw.githubusercontent.com/m18018230731/kantan-tools/master/%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85nginx%E5%8F%8D%E4%BB%A3steam%20%E5%B9%B6%E5%AE%89%E8%A3%85socks%E5%92%8Chttp%E4%BB%A3%E7%90%86/tinyproxy.conf
mv -f tinyproxy.conf /etc/tinyproxy/tinyproxy.conf
systemctl start tinyproxy.service
systemctl enable tinyproxy.service
firewall-cmd --add-port=18779/tcp --permanent

# Socks5 安装（由于滥用暂时废弃）
# if [ "$2" = "" ] || [ $2 = 0 ]; then
#   wget https://raw.githubusercontent.com/qinghuas/socks5-install/master/socks5.sh;bash socks5.sh
#   socks5 install
#   socks5 user add rabproxy 12z991
#   wget https://raw.githubusercontent.com/m18018230731/kantan-tools/master/%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85nginx%E5%8F%8D%E4%BB%A3steam%20%E5%B9%B6%E5%AE%89%E8%A3%85socks%E5%92%8Chttp%E4%BB%A3%E7%90%86/ss5
#   mv -f ss5 /etc/init.d/ss5
#   socks5 start
# fi

# 完成
firewall-cmd --reload
echo "Completed!"
