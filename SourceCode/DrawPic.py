def five_pointed_star(long):
    t.begin_fill()
    for i in range(5):
        t.forward(long)
        t.right(144)
    t.end_fill()
import turtle as t

screen = t.Screen()
t.screensize(2000,5000)
screen.setup(2000,2000,0,0) #750,500  50
t.colormode(255)
t.speed(9)
t.tracer(False)
t.bgcolor(200,200,250)
t.color(244,0,2)
t.goto(-750,500)
t.begin_fill()
for i in range(2):
    t.forward(1500)
    t.right(90)
    t.forward(1000)
    t.right(90)
t.end_fill()

t.color(250,244,8)

#大五角星
t.penup()
t.goto(-650,270)
five_pointed_star(300)
#小五角星
t.goto(-300,340)
t.setheading(48)
five_pointed_star(80)

t.goto(-200,270)
t.setheading(30)
five_pointed_star(80)

t.goto(-200,160)
t.setheading(-3)
five_pointed_star(80)

t.goto(-300,80)
t.setheading(-12)
five_pointed_star(80)

t.tracer(True)
t.goto(-775,500)
t.pendown()
t.pencolor(100,100,100)
t.pensize(50)
t.setheading(-90)
t.forward(3250)

t.pencolor("grey")
t.goto(-1000,-2500)
t.goto(1000,-2500)

#t.filling()

#t.penup()
#t.begin_poly()#开始记录多边形的顶点
#for i in range(6):
#    t.forward(100)
#    t.right(60)
#t.end_poly()
#获取多边形
#shape=t.get_poly()
#注册多边形
#t.register_shape("shape",shape)
#t.pendown()
#t.shape('shape')#绘制这个图形
t.tracer(False)
t.goto(700,-650)
t.write("何易霖", font = ("宋体", 20, "normal"))

t.exitonclick()
