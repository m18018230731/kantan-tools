#! /bin/bash
# python3.8.2 install
# author:20th
# https://github.com/clcc2019/install_python3/blob/master/py.sh

version='3.8.2'
echo '自动安装python3.x程序，与服务器自带版本共存，使用请执行python3'

#安装环境包
#yum install vim -y
yum -y install zlib zlib-devel bzip2 bzip2-devel ncurses ncurses-devel readline readline-devel openssl openssl-devel openssl-static xz lzma xz-devel sqlite sqlite-devel
yum -y install gdbm gdbm-devel
yum -y install tk tk-devel
yum -y install libffi libffi-devel
yum -y install zlib* libffi-devel
yum install gcc* glien* -y
wget https://www.python.org/ftp/python/$version/Python-$version.tgz
tar -xvf Python-$version.tgz && mkdir /usr/local/python3 && cd Python-$version
./configure --prefix=/usr/local/python3 && make && make install
if test $[python3 -V]==0; then echo '安装成功'; else echo'安装出错！';fi
ln -s /usr/local/python3/bin/python3.7 /usr/bin/python3
ln -s /usr/local/python3/bin/pip3.7 /usr/bin/pip3
PATH=$PATH:/usr/bin/python3
echo '安装完成'
read -p '回车查看版本' V
python3 -V