import gevent  # 协程
import requests, time

start = time.time()
# print(time.strftime('%Y-%m-%d %H:%M:%S'))


def f(url):
    rest = requests.get(url)  # 请求url地址
    data = rest.text  # 获取网页html树
    print('获取网站 %s的字节长度为：%s' % (url, len(data)))


# 多进程并发
gevent.joinall([
        gevent.spawn(f, 'https://docs.python.org/zh-cn/3/'),
        gevent.spawn(f, 'https://www.ctrip.com/'),
        gevent.spawn(f, 'https://www.baidu.com/'),
        gevent.spawn(f, 'https://www.sina.com.cn/')
])

print('用时:', time.time() - start)