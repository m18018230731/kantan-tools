# kantan-tools
存放一些小工具。

#### [生成指定大小的文件](https://github.com/senjianlu/kantan-tools/tree/master/%E7%94%9F%E6%88%90%E6%8C%87%E5%AE%9A%E5%A4%A7%E5%B0%8F%E7%9A%84%E6%96%87%E4%BB%B6)
```python
py main.py test.csv 100mb
```

#### [下载页面内容](https://github.com/senjianlu/kantan-tools/tree/master/%E4%B8%8B%E8%BD%BD%E9%A1%B5%E9%9D%A2%E5%86%85%E5%AE%B9)
```python
py main.py https://google.com
```

#### [Centos7 一键安装 Python3](https://github.com/senjianlu/kantan-tools/tree/master/Centos7%20%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%20Python3)
```linux
wget https://raw.githubusercontent.com/senjianlu/kantan-tools/master/Centos7%20%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%20Python3/install.sh
chmod +x ./install.sh
./install.sh
```

#### [生成随机数组](https://github.com/senjianlu/kantan-tools/tree/master/%E7%94%9F%E6%88%90%E9%9A%8F%E6%9C%BA%E6%95%B0%E7%BB%84)
```python
py main.py 1 100
```

#### [一键反代并安装代理软件](https://github.com/senjianlu/kantan-tools/tree/master/%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%20Nginx%20%E5%8F%8D%E4%BB%A3%20Steam%20%E5%B9%B6%E5%AE%89%E8%A3%85%20Tinyproxy)
```linux
yum -y install wget
wget https://raw.githubusercontent.com/senjianlu/kantan-tools/master/%E4%B8%80%E9%94%AE%E5%AE%89%E8%A3%85%20Nginx%20%E5%8F%8D%E4%BB%A3%20Steam%20%E5%B9%B6%E5%AE%89%E8%A3%85%20Tinyproxy/oneclick.sh
chmod +x oneclick.sh
./oneclick.sh your.domain.com
```
*测试用（切换服务器或本机）:*
```linux
curl -x http://rabproxy:12z991@your_ip:18779 http://ip-api.com/json/?lang=zh-CN
curl -x socks5://rabproxy:12z991@your_ip:15055 http://ip-api.com/json/?lang=zh-CN
```
