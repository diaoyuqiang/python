import pymysql.cursors


# 创建数据库连接对象
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='user',
                             cursorclass=pymysql.cursors.DictCursor
)

# 创建游标对象
with connection:
    with connection.cursor() as cursor:  # cursor = connection.cursor()
        # 编写sql
        sql = 'insert into `users` (`email`, `password`) VALUES (%s, %s)'
        result = cursor.execute(sql, ('hb@123', '123456'))  # 返回受影响的行数
        print(result)

    connection.commit()

    with connection.cursor() as cursor:
        # 编写sql
        sql = 'SELECT `id`, `password` FROM `users`'
        cursor.execute(sql)
        result = cursor.fetchone()  # 获取第一行
        print(result)