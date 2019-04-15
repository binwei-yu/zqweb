from flask import Flask, session, escape, request
import sqlite3
app = Flask(__name__)
app.secret_key = 'please-generate-a-random-secret_key'


@app.route("/")
def index():
    if 'username' in session:
        return 'hello, {}\n'.format(escape(session['username']))
    return 'hello, stranger\n'


@app.route("/login/", methods=['POST'])
#@app.route("/login/<username>/<password>/")
def login():
    if session['username'] = request.form['username']
        return 'login success'
    else:
        return 'you are not one of our members,please register.'

#def validata(username,password):
#    #get data from the post
#    #    username = request.form.get("username",type = str, default=None)
#    #    password = request.form.get("password",type = str, default=None)
#
#    # get data from database
#    #创建一个访问数据库test.db的连接
#    conn = sqlite3.connect("test.db")
#    # 创建一个访问数据库test.db的连接
#    conn = sqlite3.connect("test.db")
#    # 创建游标
#    c = conn.cursor()
#    # 获取user表中所有的记录
#    c.execute("SELECT * FROM user")
#    #获取结果
#    result = c.fetchall()
#    #关闭连接
#    conn.close()
#    #查看数据
#    for i in range(len(result)):
#        a = result[i][1]
#        if a == username:
#            if password == result[i][2]:
#                return('Login successfully')
#            else:
#                return('wrong password')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
