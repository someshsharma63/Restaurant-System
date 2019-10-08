from tkinter import *

root=Tk()
root.geometry("1200x1500")
root.title("Project Pack")

framebg=Frame(root)
framebg.pack(fill=BOTH,expand=True)

frameleft=Frame(framebg,bg="orange",height="1200",width="180")
frameleft.pack(side="left")


button1=Button(frameleft,text="Groups",width="17",height="3",bg="whitesmoke",fg="orangered",font=("calibri",14,"bold"))
button1.pack(anchor="nw",padx="15",pady="10")

button2=Button(frameleft,text="Clear All",width="17",height="3",bg="whitesmoke",fg="orangered",font=("calibri",14,"bold"))
button2.pack(anchor="nw",padx="15",pady="10")

button3=Button(frameleft,text="Hold",bg="whitesmoke",width="17",height="3",fg="orangered",font=("calibri",14,"bold"))
button3.pack(anchor="nw",padx="15",pady="10")

button4=Button(frameleft,text="Records",bg="whitesmoke",width="17",height="3",fg="orangered",font=("calibri",14,"bold"))
button4.pack(anchor="nw",padx="15",pady="10")

button5=Button(frameleft,text="Change Payment Type",bg="whitesmoke",width="17",height="3",fg="orangered",font=("calibri",14,"bold"))
button5.pack(anchor="nw",padx="15",pady="10")

button6=Button(frameleft,text="Items",bg="whitesmoke",width="17",fg="orangered",height="3",font=("calibri",14,"bold"))
button6.pack(anchor="nw",padx="15",pady="10")

button7=Button(frameleft,text="Pay",bg="whitesmoke",width="17",fg="orangered",height="3",font=("calibri",14,"bold"))
button7.pack(anchor="nw",padx="15",pady="10")

frameright=Frame(framebg,bg="red",height="1200",width="500")
frameright.pack(side="right")





button1=Button(frameright,text="STARTERS",fg="yellow",bg="purple",font=("calibri",17,"bold"),height=5)
button1.grid(row=0,column=0,sticky="nsew")


button2=Button(frameright,text="SOUTH INDIAN",fg="yellow",bg="purple",font=("calibri",17,"bold"))
button2.grid(row=0,column=1,sticky="nsew")

button3=Button(frameright,text="SOUP",fg="yellow",bg="purple",font=("calibri",17,"bold"))
button3.grid(row=0,column=2,sticky="nsew")


button4=Button(frameright,text="SOFT-DRINK",fg="yellow",bg="purple",font=("calibri",17,"bold"))
button4.grid(row=0,column=3,sticky="nsew")


button5=Button(frameright,text="SANDWICH",fg="yellow",bg="purple",font=("calibri",17,"bold"),height=5)
button5.grid(row=1,column=0,sticky="nsew")


button6=Button(frameright,text="PIZZA",fg="yellow",bg="purple",font=("calibri",17,"bold"))
button6.grid(row=1,column=1,sticky="nsew")

button7=Button(frameright,text="PAVBHAJI",fg="yellow",bg="purple",font=("calibri",17,"bold"))
button7.grid(row=1,column=2,sticky="nsew")

button8=Button(frameright,text="PASTA",fg="yellow",bg="purple",font=("calibri",17,"bold"))
button8.grid(row=1,column=3,sticky="nsew")

button9=Button(frameright,text="NOODLES",fg="yellow",bg="purple",font=("calibri",17,"bold"),height=5)
button9.grid(row=2,column=0,sticky="nsew")


button10=Button(frameright,text="MUNCHIES",fg="yellow",bg="purple",font=("calibri",17,"bold"))
button10.grid(row=2,column=1,sticky="nsew")

button11=Button(frameright,text="MANCHURIAN",fg="yellow",bg="purple",font=("calibri",17,"bold"))
button11.grid(row=2,column=2,sticky="nsew")

button12=Button(frameright,text="MAGGIE",fg="yellow",bg="purple",font=("calibri",17,"bold"))
button12.grid(row=2,column=3,sticky="nsew")


button13=Button(frameright,text="FRENCHFRIES",fg="yellow",bg="purple",font=("calibri",17,"bold"),height=5)
button13.grid(row=3,column=0,sticky="nsew")


button14=Button(frameright,text="COOKIES",fg="yellow",bg="purple",font=("calibri",17,"bold"))
button14.grid(row=3,column=1,sticky="nsew")

button15=Button(frameright,text="COFFEE",fg="yellow",bg="purple",font=("calibri",17,"bold"))
button15.grid(row=3,column=2,sticky="nsew")

button16=Button(frameright,text="BREAD",fg="yellow",bg="purple",font=("calibri",17,"bold"))
button16.grid(row=3,column=3,sticky="nsew")

framecenter=Frame(framebg,height="250",bg="skyblue",width="1400")
framecenter.pack(side=TOP)

framecenter1=Frame(framebg,bg="red",height="70",width="1600")
framecenter1.pack(side=TOP,fill=BOTH,expand=True)


label1=Label(framecenter1,text="Quantity",font=("calibri",18,"bold"))
label1.pack(side="left",pady="5",padx="4")

userEntry=Entry(framecenter1,width="3",font=("calibri",15,"bold"))
userEntry.pack(side="left",padx="9")

label2=Label(framecenter1,text="Total Amount",font=("calibri",18,"bold"))
label2.pack(side="left")

userEntry=Entry(framecenter1,width="7",font=("calibri",15,"bold"))
userEntry.pack(side="left",padx="9")

button1=Button(framecenter1,text="<<Backspace",width="12",bd=7,font=("calibri",15,"bold"))
button1.pack(side=RIGHT,padx="10");


framecenter2=Frame(framebg,bg="green",padx=70,height="200",width="900")
framecenter2.pack(side=TOP,fill=X)



def btnClick (numbers):
	global operator
	operator=operator + str(numbers)
	text_Input.set(operator)

def btnClearDisplay():
	global operator
	operator=""
	text_Input.set("")

def btnEqualsInput():
	global operator
	sumup=str(eval (operator))
	text_Input.set(sumup)
	operator=""


operator=""
text_Input =StringVar()

txtDisplay = Entry(framecenter2,font=('arial',20,'bold'),textvariable=text_Input,bd=15,insertwidth=4,bg="powder blue",justify='right')
txtDisplay.grid(columnspan=4)

btn7=Button(framecenter2,padx=16,pady=16,bd=5,fg="black",font=('arial',16,'bold'),text="7",width=5,bg="powder blue",command=lambda:btnClick(7))
btn7.grid(row=2,column=0)

btn8=Button(framecenter2,padx=16,pady=16,bd=5,fg="black",font=('arial',16,'bold'),text="8",width=5,bg="powder blue",command=lambda:btnClick(8))
btn8.grid(row=2,column=1)

btn9=Button(framecenter2,padx=16,pady=16,bd=5,fg="black",font=('arial',16,'bold'),text="9",width=5,bg="powder blue",command=lambda:btnClick(9))
btn9.grid(row=2,column=2)

btn4=Button(framecenter2,padx=16,pady=16,bd=5,fg="black",font=('arial',16,'bold'),text="4",width=5,bg="powder blue",command=lambda:btnClick(4))
btn4.grid(row=3,column=0)

btn5=Button(framecenter2,padx=16,pady=16,bd=5,fg="black",font=('arial',16,'bold'),text="5",width=5,bg="powder blue",command=lambda:btnClick(5))
btn5.grid(row=3,column=1)

btn6=Button(framecenter2,padx=16,pady=16,bd=5,fg="black",font=('arial',16,'bold'),text="6",width=5,bg="powder blue",command=lambda:btnClick(6))
btn6.grid(row=3,column=2)


btn1=Button(framecenter2,padx=16,pady=16,bd=5,fg="black",font=('arial',16,'bold'),text="1",width=5,bg="powder blue",command=lambda:btnClick(1))
btn1.grid(row=4,column=0)

btn2=Button(framecenter2,padx=16,pady=16,bd=5,fg="black",font=('arial',16,'bold'),text="2",width=5,bg="powder blue",command=lambda:btnClick(2))
btn2.grid(row=4,column=1)

btn3=Button(framecenter2,padx=16,pady=16,bd=5,fg="black",font=('arial',16,'bold'),text="3",width=5,bg="powder blue",command=lambda:btnClick(3))
btn3.grid(row=4,column=2)

btn0=Button(framecenter2,padx=16,pady=16,bd=5,fg="black",font=('arial',16,'bold'),text="0",width=5,bg="powder blue",command=lambda:btnClick(0))
btn0.grid(row=5,column=0)

btnClear=Button(framecenter2,padx=16,pady=16,bd=5,fg="black",font=('arial',16,'bold'),text="C",width=5,bg="powder blue",command=btnClearDisplay)
btnClear.grid(row=5,column=1)

btnQty=Button(framecenter2,padx=16,pady=16,bd=5,fg="black",font=('arial',16,'bold'),text="Qty",width=5,bg="powder blue",command=lambda:btnClick())
btnQty.grid(row=5,column=2)

root.mainloop()



