import pymysql
import random
import uuid
import time


# 创建数据库连接对象
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='user',
                             cursorclass=pymysql.cursors.DictCursor)


def sort(page=1, pagesize=10):

    try:
        # 创建游标对象
        cursor = connection.cursor()
        # 编写sql
        sql = 'SELECT email,password FROM `users` limit %s,%s'

        cursor.execute(sql, ((page-1)*pagesize, pagesize))
        result = cursor.fetchall()
        print(result)

    except Exception as e:

        print("错误信息：", e)

    finally:
        connection.close()


if __name__ == '__main__':

    sort(page=2)