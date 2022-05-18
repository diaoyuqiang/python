# coding=utf-8
import time
from collections import deque


class DataNode(object):
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.create_clock = int(round(time.time() * 1000000))  # 微秒级

    def __repr__(self):
        return "{{key: {}, create_clock: {}}}".format(self.key, self.create_clock)


class MaxSizeCache(object):
    """
    有序(按放入时间顺序)且有最大存储量的缓存
    最先放入的数据居于最左, 最早过期
    max_size 最大存储量, 超过则抛弃最早放入的数据
    """

    def __init__(self, max_size=1024):
        self._dict = dict()  # 字典数据
        self._deque = deque(maxlen=max_size)  # 双端队列
        self.max_size = max_size  # 最大保存数据量
        self.data_cls = DataNode  # 数据类型

    @property
    def size(self):
        return len(self._dict)

    def get(self, key):
        data = self._dict.get(key)
        if data is None:
            return None
        return data.value

    def put(self, key, value):
        data = self._dict.get(key)
        if data:
            self._dict.pop(key)
        data = self.data_cls(key, value)
        if self.size >= self.max_size:
            self.delete_prev_data()
        self._dict[key] = data
        self._deque.append(data)

    def delete_prev_data(self, key=None):
        if not key:  # 没有传递key, 只删除最左侧一个数据
            data = self._deque.popleft()
            self._dict.pop(data.key)
        else:  # 有key, 则key之前的数据都删除
            pop_data = self._dict.get(key)
            if pop_data:
                break_flag = False
                for i in range(self.max_size):
                    data = self._deque.popleft()
                    if data.create_clock <= pop_data.create_clock and data.key != pop_data.key:
                        self._dict.pop(data.key)
                    else:
                        self._deque.appendleft(data)
                        break_flag = True
                    if break_flag:
                        self._deque.popleft()
                        self._dict.pop(data.key)
                        break

    def __repr__(self):
        return "{{size: {}, data: {}}}".format(self.size, self._deque)


if __name__ == '__main__':
    cache1 = MaxSizeCache(3)
    cache1.put(1, {"name": "1", "sex": "man"})
    cache1.put(2, {"name": "2", "sex": "woman"})
    cache1.put(3, {"name": "3", "sex": "man"})
    cache1.put(4, {"name": "4", "sex": "man"})
    print(cache1._dict)
    print(cache1._deque)

    print("get something...start")
    print(cache1.get(2))
    print(cache1.get(9))
    print("get something...end")

    cache1.delete_prev_data()
    print("delete one...start")
    print(cache1._dict)
    print(cache1._deque)
    print(cache1)
    print("delete one...end")

    cache1.put(5, {"name": "5", "sex": "woman"})
    cache1.put(6, {"name": "6", "sex": "man"})
    print(cache1)
    cache1.delete_prev_data(5)
    print(cache1._dict)
    print(cache1._deque)
    print(cache1)
