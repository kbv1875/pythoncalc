from tkinter import *

window=Tk()
window.geometry("500x500")
window.title("calculator")
window.configure(bg="blue")

def which_buton(button_press):
    lb["text"]=lb["text"]+button_press
def equal():
    total = lb["text"]
    sum=eval(total)
    lb["text"]=str(sum)

lb=Label(window,bg="grey",width=60,height=5,textvariable="")
lb.pack(pady=20)
bt1=Button(window,text="1",width=5,height=3,command=lambda m="1": which_buton(m))
bt1.pack(side=TOP,pady=20)
bt2=Button(window,text="2",width=5,height=3,command=lambda m="2": which_buton(m))
bt2.pack(side=TOP,pady=20)
bt3=Button(window,text="3",width=5,height=3,command=lambda m="3": which_buton(m))
bt3.pack(side=TOP,pady=20)
bt3=Button(window,text="+",width=5,height=3,command=lambda m="+": which_buton(m))
bt3.pack(side=LEFT,pady=20)
bt3=Button(window,text="=",width=5,height=3,command=equal)
bt3.pack(side=RIGHT,pady=20)
bt3=Button(window,text="-",width=5,height=3,command=lambda m="-": which_buton(m))
bt3.pack(side=BOTTOM,pady=20)
bt3=Button(window,text="/",width=5,height=3,command=lambda m="/": which_buton(m))
bt3.pack(side=LEFT,padx=50)
bt3=Button(window,text="*",width=5,height=3,command=lambda m="*": which_buton(m))
bt3.pack(side=RIGHT,padx=50)
window.mainloop()