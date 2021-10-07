import pymysql.cursors
import datetime


# 创建数据库连接对象
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='user',
                             cursorclass=pymysql.cursors.DictCursor  # 返回字典类型
)


def update(email, passwd):

    # 创建游标对象
    cursor = connection.cursor()
    # 编写sql
    sql = 'insert into `users` (`email`, `password`) VALUES ("'+email+'", "'+passwd+'")'  # 拼接字符串变量
    print(sql)
    result = cursor.execute(sql)  # 返回受影响的行数
    print(result)

    connection.commit()


# def query_many(email):
#
#     cursor = connection.cursor()
#     sql = 'select email, password from users where email like %s'
#     cursor.execute(sql, '%'+email+'%')
#     result = cursor.fetchmany(1)  # 设置返回条数
#     print(result)


# def update(time,num):
#
#     try:
#         cursor = connection.cursor()
#         sql = 'update users set create_time = \'%s\' where id = %s' % (time, num)
#         print(sql)
#         result = cursor.execute(sql)
#         print('受影响行数：', result)
#         connection.commit()
#
#     except Exception as e:
#         print("错误信息：", e)
#         connection.rollback()
#
#     finally:
#         connection.close()


def apply():

    email = input("请输入邮箱：")
    passwd = input("密码：")
    update(email, passwd)
    # query_many(email)
    # time = datetime.datetime.now()
    # num = 4
    # update(time,num)


if __name__ == '__main__':
    apply()
