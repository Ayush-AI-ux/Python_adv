# from tkinter import *
# root=Tk()
# myLabel1=Label(root,text="Hello GLA!")
# myLabel2=Label(root,text="Tkinter GUI")
# myLabel1.grid(row=0,column=0)
# myLabel2.grid(row=0,column=5)
# root.mainloop()


# from tkinter import *

# root=Tk()
# def click():
#     label1=Label(root,text="Hello,How are you?")
#     label1.pack()
    
# myButton1=Button(root,text="Submit",command=click,fg="green",bg="yellow")
# myButton1.pack()
# root.mainloop()

# from tkinter import *
# root=Tk()

# root.geometry("2000x2000")
# mybutton1=Button(root,text="Submit")
# mybutton1.pack()
# root.mainloop()


# from tkinter import *
# root=Tk()
# mytext1=Entry(root,width=20)
# mytext1.pack()
# def fun():
#     label_1=Label(root,text=f"Welcome to this system: {mytext1.get()}")
#     label_1.pack()
# Button5=Button(root,text="Button5",bg="red",fg="white",command=fun,padx=20,pady=20)
# Button5.pack()
# root.geometry("2000x2000")
# i=0
# j=0
# k=0
# l=0
# def click():
#     global i
#     i+=1
#     label1=Label(root,text=f"Button1 is clicked {i} times.")
#     label1.pack()
# def click1():
#     global j
#     j+=1
#     label2=Label(root,text=f"Button2 is clicked {j} times.")
#     label2.pack()
# def click2():
#     global k
#     k+=1
#     label3=Label(root,text=f"Button3 is clicked {k} times.")
#     label3.pack()
# def click3():
#     global l
#     l+=1
#     label4=Label(root,text=f"Button4 is clicked {l} times.")
#     label4.pack()

# Button1=Button(root,text="Select Language",bg="red",fg="white",command=click,padx=20,pady=20)
# Button2=Button(root,text="Submit2",bg="blue",fg="white",command=click1,padx=20,pady=20)
# Button3=Button(root,text="Submit3",bg="green",fg="white",command=click2,padx=20,pady=20)
# Button4=Button(root,text="Submit4",bg="yellow",fg="white",command=click3,padx=20,pady=20)
# Button1.pack(side="left")
# Button2.pack(side="right")
# Button3.pack()
# Button4.pack()
# root.mainloop()


# from tkinter import *
# root=Tk()
# root.geometry("2000x2000")
# Button1=Button(root,text="Select Language",bg="lime",fg="black",)
# Button1.pack(side="left")
# root.mainloop()


# from tkinter import *
# root=Tk()
# root.geometry("200x200")
# checkvar=IntVar()
# def show():
#     mylabel1=Label(root,text=checkvar.get())
#     mylabel1.pack()
    
# cb1=Checkbutton(root,text="Hi, How are you?",variable=checkvar)
# cb1.pack()

# Button1=Button(root,text="Click button for help",command=show)
# Button1.pack()
# root.mainloop()

# from tkinter import *
# root=Tk()
# a=IntVar()
# def showfunc():
#     mylabel1=Label(root,text=a.get()).pack()
    
# check1=Checkbutton(root,text="value1",variable=a)
# check1.pack()
# mybutton=Button(root,text="clickheck",command=showfunc)
# mybutton.pack()
# root.mainloop()


# from tkinter import *
# root=Tk()
# a=StringVar()
# def show():
#     mylabel1=Label(root,text=a.get()).pack()
    
# cb1=Checkbutton(root,text="Hi are in Python Workshop",variable=a,onvalue="selected",offvalue="not selected")
# cb1.deselect()
# cb1.pack()

# mybutton1=Button(root,text="Click button for selection value",command=show)
# mybutton1.pack()
# root.mainloop()


# from tkinter import *
 
# top = Tk()
# Lb = Listbox(top)
# Lb.insert(1, 'Python')
# Lb.insert(2, 'Java')
# Lb.insert(3, 'C++')
# Lb.insert(4, 'Any other')
# Lb.pack()
# top.mainloop()

# add = lambda x,y: x+y
# result =add(3,5)
# print(result)

# from tkinter import *

# root=Tk()
# def on_button_click(value):
#     print(f"Button {value} clicked by user!")
    
# Button1=Button(root,text="ADD",command=lambda:on_button_click(1))
# Button2=Button(root,text="SUB",command=lambda:on_button_click(2))
# Button3=Button(root,text="MULT",command=lambda:on_button_click(3))
# Button1.pack()
# Button2.pack()
# Button3.pack()
# root.mainloop()


from tkinter import *
root=Tk()
root.title("Calculator")
entry1=Entry(root,width=15,borderwidth=5)
entry1.insert(0,"Enter the value")
entry1.grid(row=0,column=0,columnspan=4)
button0=Button(root,text="0",fg="white",bg="black",padx=6,pady=7)
button1=Button(root,text="1",fg="white",bg="black",padx=6,pady=7)
button2=Button(root,text=" 2  ",fg="white",bg="black",padx=6,pady=7)
button3=Button(root,text="3",fg="white",bg="black",padx=7,pady=7)
button4=Button(root,text="4",fg="white",bg="black",padx=6,pady=7)
button5=Button(root,text="5",fg="white",bg="black",padx=6,pady=7)
button6=Button(root,text=" 6  ",fg="white",bg="black",padx=6,pady=7)
button7=Button(root,text="7",fg="white",bg="black",padx=7,pady=7)
button8=Button(root,text="8",fg="white",bg="black",padx=6,pady=7)
button9=Button(root,text="9",fg="white",bg="black",padx=6,pady=7)
button00=Button(root,text=" 00",fg="white",bg="black",padx=6,pady=7)
button_add=Button(root,text="+",fg="white",bg="black",padx=6,pady=7)
button_sub=Button(root,text="-",fg="white",bg="black",padx=20,pady=7)
button_mult=Button(root,text=" *  ",fg="white",bg="black",padx=6,pady=7)
button_div=Button(root,text="/",fg="white",bg="black",padx=7,pady=7)
button0.grid(row=3,column=0)
button1.grid(row=3,column=1)
button2.grid(row=3,column=2)
button3.grid(row=3,column=3)
button4.grid(row=4,column=0)
button5.grid(row=4,column=1)
button6.grid(row=4,column=2)
button7.grid(row=4,column=3)
button8.grid(row=5,column=0)
button9.grid(row=5,column=1)
button00.grid(row=5,column=2)
button_add.grid(row=5,column=3)
button_sub.grid(row=6,column=0,columnspan=2)
button_mult.grid(row=6,column=2)
button_div.grid(row=6,column=3)
root.mainloop()

