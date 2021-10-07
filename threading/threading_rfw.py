import threading
import time

rq = []
wq = []


def _read():
    while True:
        msg = input('>>:').strip()
        if not msg:
            continue
        rq.append(msg)


def _format():
    while True:
        if len(rq) != 0:
            data = rq.pop()
            wq.append(data.upper())


def _write():
    while True:
        if len(wq) != 0:
            data = wq.pop()
            with open('ob', 'w', encoding='utf-8') as f:
                f.write(data)


if __name__ == '__main__':
    t1 = threading.Thread(target=_read)
    t2 = threading.Thread(target=_format)
    t3 = threading.Thread(target=_write)

    t1.start()
    t2.start()
    t3.start()



