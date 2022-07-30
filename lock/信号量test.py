import threading
import time
import random

sites = ["https://www.baidu.com/", "https://github.com/Fiz1994", "https://stackoverflow.com/",
         "https://www.sogou.com/",
         "http://english.sogou.com/?b_o_e=1&ie=utf8&fr=common_index_nav&query="] * 20
sites_index = 0
maxconnections = 2
pool_sema = threading.BoundedSemaphore(value=maxconnections)


def test():
    with pool_sema:
        global sites_index, sites
        url = str(sites[sites_index])
        k = random.randint(10, 20)
        print("爬取: " + url + " 需要时间 : " + str(k))
        sites_index += 1
        # print(url)
        time.sleep(k)
        print('退出 ', url)


for i in range(100):
    threading.Thread(target=test).start()
