import turtle
import time

turtle.setup(1200,900,600,50)


def time_count():
    record1 = time.time()
    record1_1 = time.ctime()     #程序开始时间
    turtle.penup()
    turtle.goto(-450, 320)
    # turtle.color("violet")
    turtle.color("red")
    turtle.write("开始时间为:%s" % record1_1, font=('宋体', 40, 'normal',))

    sun_flower()    # 调用绘画程序

    record2_1= time.ctime()
    record2 = time.time()
    record_result = round(record2-record1, 3)   #程序运行持续时间
    turtle.penup()
    turtle.goto(-450, 270)
    turtle.color("red")
    turtle.write("结束时间为:%s" % record2_1, font=('宋体', 40, 'normal',))

    turtle.penup()
    turtle.goto(-450, 220)
    turtle.color("blue")
    turtle.write("持续时间为:%s" % record_result, font=('宋体', 40, 'normal',))    # Arial
    turtle.mainloop()

def sun_flower():
    # 同时设置pencolor=color1, fillcolor=color2
    turtle.penup()
    flower_pos = (-200,0)
    turtle.setpos(flower_pos)
    turtle.pendown()
    turtle.color("red", "yellow")

    turtle.begin_fill()
    for _ in range(6):     # 画36条线—— change
        turtle.forward(400)
        turtle.left(170)
    turtle.end_fill()


def main():
    time_count()


if __name__ == '__main__':
    main()
