import tkinter as tk
import random
bot = False


def func():
    global bot
    if bot==False:
        bot=True
        var.set("有请第%d组上台" % random.randint(1, 14))
        var2.set("点击重新开始")
    else:
        bot=False
        var.set('---------')
        var2.set("点击开始抽取")


window = tk.Tk()   # 创建一个窗口对象
window.title("随机点名器1.0")  # 设置窗口标题
window.geometry('600x600')  # 设置窗口大小
var=tk.StringVar()  # 创建一个文字对象
var2 = tk.StringVar()
text_lable = tk.Label(textvar=var,font=('Arial',25),bg='pink',width=30,height=11)  # 创建标签对象 设置文字内容，背景颜色，高和宽
text_lable.pack()  # 放置按钮
but = tk.Button(text="点击开始抽取",textvar=var2,width=50,height=4,command=func)  # 创建按钮对象设置属性 command用来连接功能函数（方法）
but.pack()  # 放置按钮
window.mainloop()  # 运行
