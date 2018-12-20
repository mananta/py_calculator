from tkinter import *
root=Tk()
root.title("CALCULATOR")
# root=Frame(Root,width=500,height=500)
# root.pack()
eqn=""
data=StringVar()
screen=Label(root,bg='white',textvariable=data)
screen.grid(columnspan=4)
#data.set("2.0000")
def button(num):
    global eqn
    eqn=eqn+str(num)
    data.set(eqn)

def clear():
    global eqn
    eqn=""
    data.set(eqn)

def calculate():
    global eqn
    eqn=str(eval(eqn))
    data.set(eqn)
    eqn=''

button7=Button(root,text="7",bg='black',fg='white',command=lambda:button(7))
button7.grid(row=2,column=0)
button8=Button(root,text="8",bg='black',fg='white',command=lambda:button(8))
button8.grid(row=2,column=1)
button9=Button(root,text="9",bg='black',fg='white',command=lambda:button(9))
button9.grid(row=2,column=2)
button4=Button(root,text="4",bg='black',fg='white',command=lambda:button(4))
button4.grid(row=3,column=0)
button5=Button(root,text="5",bg='black',fg='white',command=lambda:button(5))
button5.grid(row=3,column=1)
button6=Button(root,text="6",bg='black',fg='white',command=lambda:button(6))
button6.grid(row=3,column=2)
button1=Button(root,text="1",bg='black',fg='white',command=lambda:button(1))
button1.grid(row=4,column=0)
button2=Button(root,text="2",bg='black',fg='white',command=lambda:button(2))
button2.grid(row=4,column=1)
button3=Button(root,text="3",bg='black',fg='white',command=lambda:button(3))
button3.grid(row=4,column=2)
button0=Button(root,text="0",bg='black',fg='white',command=lambda:button(0))
button0.grid(row=5,columnspan=2,sticky=N+S+E+W)
button_=Button(root,text=".",bg='black',fg='white',command=lambda:button('.'))
button_.grid(row=5,column=2)
buttonc=Button(root,text="C",bg='black',fg='white',command=clear)
buttonc.grid(row=1,column=0)
divide=Button(root,text="/",bg='black',fg='white',command=lambda:button('/'))
divide.grid(row=1,column=1)
multiply=Button(root,text="*",bg='black',fg='white',command=lambda:button('*'))
multiply.grid(row=1,column=2)
minus=Button(root,text="-",bg='black',fg='white',command=lambda:button('-'))
minus.grid(row=1,column=3)
plus=Button(root,text="+",bg='black',fg='white',command=lambda:button('+'))
plus.grid(column=3,row=2,rowspan=2,sticky=E+W+N+S)
equal=Button(root,text="=",bg='black',fg='white',command=calculate)
equal.grid(column=3,row=4,rowspan=2,sticky=E+W+N+S)




root.mainloop()
