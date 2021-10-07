from pymysqlpool import ConnectionPool
import uuid
import random
import time

config = {'pool_name': 'test',
          'host': 'localhost',
          'user': 'root',
          'password': '123456',
          'database': 'user'}


def connection_pool():
    # 创建数据库连接池，返回指定个数的连接
    pool = ConnectionPool(max_pool_size=20, **config)
    return pool


# for obj in connection_pool():
#     obj.cursor().execute('TRUNCATE users')


# with connection_pool().cursor() as cursor:
#     result = cursor.execute('TRUNCATE users')
#     # print(result)  # 返回受影响的记录


def batch():
    # 创建游标对象
    with connection_pool().cursor() as cursor:

        try:

            sql = 'insert into `users` (`email`, `password`) values'

            for i in range(10000):

                sql += '("'+str(uuid.uuid4())+'","'+str(random.randint(0, 10000))+'"),'

            sql = sql.rstrip(',')

            start = time.perf_counter()
            result = cursor.execute(sql)
            print('受影响行数：{}，耗费时间：{}'.format(result, time.perf_counter() - start))

            # connection.commit()

        except Exception as e:

            print("错误信息：", e)
            # connection.rollback()

        finally:
            # connection.close()
            pass


if __name__ == '__main__':

    batch()

