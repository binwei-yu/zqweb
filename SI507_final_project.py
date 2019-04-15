from flask import Flask, render_template
from movies_tools import Movie
import random
import MySQLdb
#module for read data from mysql database
import pymysql.cursors
import pymysql
import pandas as pd
import random
from PIL import Image,ImageDraw,ImageFont

# Set up application
app = Flask(__name__)


# Routes
# Route1 for validate
@app.route('/validate/',methods = ['POST'])
def validata():
    #get data from the post
    username = request.form.get("username",type = str, default=None)
    password = request.form.get("password",type = str, default=None)
    # get data from database

# 打开数据库连接
    db = MySQLdb.connect("localhost", "testuser", "123456", "test", charset='utf8' )

# 使用cursor()方法获取操作游标
    cursor = db.cursor()

# SQL 查询语句
    sql = "SELECT * FROM test"
    try:
    # 执行SQL语句
        cursor.execute(sql)
    # 获取所有记录列表
        results = cursor.fetchall()
        for row in results:
            print(row[1])
#            username = row[1]
#            password_data = row[1]
#        if password == password_data:
#            return 'Login successfully'
#        else:
#            return 'wrong password'


@app.route('/validate_map/')
def validata_map():
#定义使用Image类实例化一个长为200px,宽为100px,基于RGB的(255,255,255)颜色的图片
    img1=Image.new(mode="RGB",size=(200,100),color=(255,255,255))

#实例化一支画笔
    draw1=ImageDraw.Draw(img1,mode="RGB")

#定义要使用的字体
    font1=ImageFont.truetype("OpenSans-Bold.ttf",28)
    validate_number = ""
    for i in range(5):
    #每循环一次,从a到z中随机生成一个字母或数字
    #65到90为字母的ASCII码,使用chr把生成的ASCII码转换成字符
    #str把生成的数字转换成字符串
        char1=random.choice([chr(random.randint(65,90)),str(random.randint(0,9))])

    #每循环一次重新生成随机颜色
        color1=(random.randint(0,255),random.randint(0,255),random.randint(0,255))

    #把生成的字母或数字添加到图片上
    #图片长度为200px,要生成5个数字或字母则每添加一个,其位置就要向后移动40px
        draw1.text([i*40,0],char1,color1,font=font1)
        validate_number = validate_number + char1
#把生成的图片保存为"pic.png"格式
    print(validate_number)
    with open("pic.png","wb") as f:
            img1.save(f,format="png")


if __name__ == '__main__':
    app.run()


#@app.route('/movies/ratings/')
#def sample_of_movies():
#    test_sample_movie = Movie.Sample_movie()
#    return '<h1 style="color:blue";><b><center>{}</center></b></h1>'.format(test_sample_movie)
#
#@app.route('/movies/MPAA/ratings/')
#def MAPP_of_movies():
#    test_MAPP_sample_movie = Movie.Rating_movie()
#    return '<h1 style="color:green";><b><center>{}</center></b></h1>'.format(test_MAPP_sample_movie)
#
#
#@app.route('/movies/date/')
#def date_of_movies():
#    date_movie = Movie.date_movie()
#    return '<h1 style="color:red";><b><center>{}</center></b></h1>'.format(date_movie)


# @app.route('/bank/<name>')
# def welcome_word_for_bank(name):
#     return '<h1 style="color:blue">Welcome to {}!</h1>'.format(name)




