import pymysql

#connect to Mysql
connection = pymysql.connect(host='localhost',
                             user='Priya',
                             password='654321',
                             db='to_do_list_manager',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


cursor = connection.cursor()
# cursor.execute('select * from tasks')
# result = cursor.fetchall()
# print(result)

