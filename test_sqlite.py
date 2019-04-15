# 导入SQLite驱动:
import sqlite3
# 连接到SQLite数据库
# 数据库文件是test.db
# 如果文件不存在，会自动在当前目录创建:
conn = sqlite3.connect('test.db')
# 创建一个Cursor:
cursor = conn.cursor()
# 执行一条SQL语句，创建user表:
cursor.execute('create table user (id varchar(20) primary key, name varchar(50),password_data varchar(20))')
# 继续执行一条SQL语句，插入一条记录:
cursor.execute('insert into user (id, name, password_data) values (\'1\', \'zq\',\'0524\')')
cursor.execute('insert into user (id, name, password_data) values (\'2\', \'ybw\',\'0305\')')
cursor.execute('insert into user (id, name, password_data) values (\'3\', \'ly\',\'0506\')')
#<sqlite3.Cursor object at 0x10f8aa260>
# 通过rowcount获得插入的行数:
cursor.rowcount
1
# 关闭Cursor:
cursor.close()
# 提交事务:
conn.commit()
# 关闭Connection:
conn.close()
