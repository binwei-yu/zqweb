#
#from PIL import Image
#
#img1=Image.new(mode="RGB",size=(400,400),color=(255,255,255))
#
#with open("pic.png","wb") as f:
#    img1.save(f,format="png")
#
##img1.show()
##创建画笔,用于在图片上生成内容
#draw1=ImageDraw.Draw(img1,mode="RGB")
#
##在(100,100)坐标上生成一个红点,指定的坐标不能超过图片的尺寸
#draw1.point([100,100],pill="red")
##在(80,80)坐标上生成一个黑点,指定的坐标不能超过图片的尺寸
#draw1.point([80,80],fill=(0,0,0))
#
##第一个括号里面的参数是坐标,前两个数为开始坐标,后两个数为结束坐标
##括号里的第二个参数指定颜色,可以直接指定,也可以用RGB来表示颜色
#draw1.line((100,100,100,300),fill="red")
#draw1.line((100,200,200,100),fill="blue")
#
##括号里的第一个参数是坐标,前两个数为起始坐标,后两个为结束坐标
##用这两个坐标之间的正方形区域生成一个圆,大括号里的第二个参数为圆的开始角度
##第三个参数为圆的结束角度,0到360表示所画的是一个完整的圆形,
##也可以指定的数字来生成一段为圆弧,最后一个参数表示颜色,也可以用RGB来表示想要的颜色
#draw1.arc((100,100,300,300),0,360,fill="red")
#draw1.arc((0,0,300,300),0,90,fill="blue")
#
##使用画笔的text方法在图片上生成文本
##第一个参数为坐标,第二个参数为所有生成的文本的内容
##第三个参数为文本的颜色
#draw1.text([0,0],"python","blue")
#
##先实例化一个字体对象,第一个参数表示字体的路径,第二个参数表示字体大小
#font1=ImageFont.truetype("One Chance.ttf",28)
#
##在图片上生成字体
##第一个括号里的参数表示坐标,第二个参数表示写入的内容
##第三个参数表示颜色,第四个参数表示使用的字体对象
#draw1.text([200,200],"linux","red",font=font1)



#导入random模块
import random

#导入Image,ImageDraw,ImageFont模块
from PIL import Image,ImageDraw,ImageFont

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
    #图片长度为120px,要生成5个数字或字母则每添加一个,其位置就要向后移动24px
    draw1.text([i*40,0],char1,color1,font=font1)
    validate_number = validate_number + char1
#把生成的图片保存为"pic.png"格式
print(validate_number)
with open("pic.png","wb") as f:
    img1.save(f,format="png")
