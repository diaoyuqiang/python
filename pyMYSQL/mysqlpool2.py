import pandas as pd
from pymysqlpool import ConnectionPool


config = {'pool_name': 'test',
          'host': 'localhost',
          'user': 'root',
          'password': '123456',
          'database': 'user'
          }


def connection_pool():
    # 创建数据库连接池，返回指定个数的连接
    pool = ConnectionPool(max_pool_size=20, **config)
    return pool


# print(connection_pool().pool_size)  # 查看连接数

with connection_pool().connection() as conn:  # 获取一个连接对象

    data = pd.read_sql('SELECT * FROM users limit 10', conn)
    print(data)

    # 或者__________________________________________________________
    connection = connection_pool().borrow_connection()  # 获取一个连接对象

    data = pd.read_sql('SELECT * FROM users limit 10', conn)
    print(data)

print(connection_pool().pool_size)

print(connection_pool().return_connection(connection))  # 获取连接状态
