from tkinter import *
window = Tk()
window.geometry("500x500")
window.title("calculator")
window.configure(bg="grey")
for i in range(4):
    window.columnconfigure(i,weight=1)
for i in range(5):
    window.rowconfigure(i,weight=1)
display_box = Entry(window, bg="blue",fg="white",font=("Arial",20),width=25)
display_box.grid(row=0,column=0,columnspan=4,padx=2, pady=2,ipady=15,sticky="ew")

def hello(value):
    print("button clicked")
    display_box.insert(END, value)
def clear():
    display_box.delete(0,END)
def calculate():
    try:
        expression = display_box.get()
        result = eval(expression)
        display_box.delete(0,END)
        display_box.insert(END,str(result))
    except Exception as e:
        print("Error:",e)
        display_box.delete(0,END)
        display_box.insert(END,"Error")



button1 = Button(window,text="7",width=5,height=5,fg="black",command=lambda:hello("7"))
button2 = Button(window,text="8",width=5,height=5,fg="black",command=lambda:hello("8"))
button3 = Button(window,text="9",width=5,height=5,fg="black",command=lambda:hello("9"))
button4 = Button(window,text="/",width=5,height=5,fg="red",command=lambda:hello("/"))
button5 = Button(window,text="4",width=5,height=5,fg="black",command=lambda:hello("4"))
button6 = Button(window,text="5",width=5,height=5,fg="black",command=lambda:hello("5"))
button7 = Button(window,text="6",width=5,height=5,fg="black",command=lambda:hello("6"))
button8 = Button(window,text="*",width=5,height=5,fg="red",command=lambda:hello("*"))
button9 = Button(window,text="1",width=5,height=5,fg="black",command=lambda:hello("1"))
button10 = Button(window,text="2",width=5,height=5,fg="black",command=lambda:hello("2"))
button11 = Button(window,text="3",width=5,height=5,fg="black",command=lambda:hello("3"))
button12 = Button(window,text="-",width=5,height=5,fg="red",command=lambda:hello("-"))
button13 = Button(window,text="0",width=5,height=5,fg="black",command=lambda:hello("0"))
button14 = Button(window,text=".",width=5,height=5,fg="black",command=lambda:hello("."))
button15 = Button(window,text="+",width=5,height=5,fg="red",command=lambda:hello("+"))
button16 = Button(window,text="=",width=5,height=5,fg="red",command=calculate)
button17 = Button(window,text="clear",width=5,height=5,fg="red",command=clear)

button1.grid(row=1,column=0)
button2.grid(row=1,column=1)
button3.grid(row=1,column=2)
button4.grid(row=1,column=3)
button5.grid(row=2,column=0)
button6.grid(row=2,column=1)
button7.grid(row=2,column=2)
button8.grid(row=2,column=3)
button9.grid(row=3,column=0)
button10.grid(row=3,column=1)
button11.grid(row=3,column=2)
button12.grid(row=3,column=3)
button13.grid(row=4,column=0)
button14.grid(row=4,column=1)
button15.grid(row=4,column=2)
button16.grid(row=4,column=3)
button17.grid(row=1,column=4)
window.mainloop()
