from tkinter import *
root=Tk()
root.title('калькулятор')
def function1():
    canvas.itemconfig(a,fill='white')
def function2():
    canvas.itemconfig(b,fill='white',outline='white')
def function3():
    canvas.itemconfig(c,fill='cyan',outline='white')
root.geometry('1000x1300')
canvas=Canvas(root, width=800, height=800, bg='black')
canvas.pack()
a=canvas.create_polygon(350,400,180,500,550,500,fill='black')
b=canvas.create_rectangle(520,810,210,495,fill='black',outline='black')
c=canvas.create_rectangle(470,650,260,510,fill='black')
Button(root,text='нажми меня 1',command=function1).pack()
Button(root,text='а меня 2',command=function2).pack()
Button(root,text='ну значит меня 3',command=function3).pack()
root.mainloop()
