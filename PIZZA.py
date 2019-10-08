from tkinter import *

root=Tk()
root.title("Pizza")
root.geometry("500x500")

framePizza=Frame(root)
framePizza.pack(side="right",fill=BOTH,expand=True)

button1=Button(framePizza,text="MUSHROOM",width="15",font=("calibri",17,"bold"),height=5)
button1.grid(row=0,column=0,sticky="nsew")


button2=Button(framePizza,text="CHEESE",width="15",font=("calibri",17,"bold"),height=5)
button2.grid(row=0,column=1,sticky="nsew")

button3=Button(framePizza,text="CORN",width="15",font=("calibri",17,"bold"),height=5)
button3.grid(row=0,column=2,sticky="nsew")


button4=Button(framePizza,text="CAPSICUM",width="15",font=("calibri",17,"bold"),height=5)
button4.grid(row=1,column=0,sticky="nsew")


button5=Button(framePizza,text="AMERICAN",width="15",font=("calibri",17,"bold"),height=5)
button5.grid(row=1,column=1,sticky="nsew")

button6=Button(framePizza,text="CORN",width="15",font=("calibri",17,"bold"),height=5)
button6.grid(row=1,column=2,sticky="nsew")

button8=Button(framePizza,text="JAIN",width="15",font=("calibri",17,"bold"),height=5)
button8.grid(row=2,column=0,sticky="nsew")


button9=Button(framePizza,text="ITALIAN",width="15",font=("calibri",17,"bold"),height=5)
button9.grid(row=2,column=1,sticky="nsew")

button10=Button(framePizza,text="BAKED",width="15",font=("calibri",17,"bold"),height=5)
button10.grid(row=2,column=2,sticky="nsew")

button11=Button(framePizza,text="GARLIC",width="15",font=("calibri",17,"bold"),height=5)
button11.grid(row=3,column=0,sticky="nsew")

button12=Button(framePizza,text="TOMATO",width="15",font=("calibri",17,"bold"),height=5)
button12.grid(row=3,column=1,sticky="nsew")

button13=Button(framePizza,text="SPECIAL PIZZAS",width="15",font=("calibri",17,"bold"),height=5)
button13.grid(row=3,column=2,sticky="nsew")












root.mainloop()

