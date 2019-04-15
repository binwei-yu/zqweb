import sqlite3
from flask import Flask, render_template

app = Flask(__name__)
#

#@app.route('/validate',methods = ['POST'])



@app.route('/validate/<username>/<password>')
def validata(username,password):
    #get data from the post
#    username = request.form.get("username",type = str, default=None)
#    password = request.form.get("password",type = str, default=None)

    # get data from database
    #创建一个访问数据库test.db的连接
    conn = sqlite3.connect("test.db")
    # 创建一个访问数据库test.db的连接
    conn = sqlite3.connect("test.db")
    # 创建游标
    c = conn.cursor()
    # 获取user表中所有的记录
    c.execute("SELECT * FROM user")
    #获取结果
    result = c.fetchall()
    #关闭连接
    conn.close()
    #查看数据
    for i in range(len(result)):
        a = result[i][1]
        if a == username:
            if password == result[i][2]:
                return('Login successfully')
            else:
                return('wrong password')




@app.route('/test/<name>', methods=['GET'])
def test(name):
    print(name)

if __name__ == '__main__':
    app.run(debug=True)


#
#print(validata('ybw','0524'))
