import pymysql.cursors
import random
import uuid
import time


# 创建数据库连接对象
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='user',
                             cursorclass=pymysql.cursors.DictCursor)


def batch():

    try:
        # 创建游标对象
        cursor = connection.cursor()
        # 编写sql
        sql = 'insert into `users` (`email`, `password`) values'

        for i in range(10000):

            sql += '("'+str(uuid.uuid4())+'","'+str(random.randint(0, 10000))+'"),'

        sql = sql.rstrip(',')

        start = time.perf_counter()
        result = cursor.execute(sql)
        print('受影响行数：{}，耗费时间：{}'.format(result, time.perf_counter() - start))

        connection.commit()

    except Exception as e:

        print("错误信息：", e)
        connection.rollback()

    finally:
        connection.close()


if __name__ == '__main__':

    batch()