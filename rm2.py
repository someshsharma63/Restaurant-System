from tkinter import *

root=Tk()
root.geometry("1200x1500")
root.title("Project Pack")


frame1=Frame(root)
frame1.pack(fill=BOTH,expand=True)

frame2=Frame(frame1,bg="orange",height="1200",width="200")
frame2.pack(side="left")

frame3=Frame(frame1,bg="blue",height="1200",width="500")
frame3.pack(side="right")

ButtonTOAST=Button(frame3,text="TOAST",width="15",font=("calibri",17,"bold"),height=5)
ButtonTOAST.grid(row=0,column=0,sticky="nsew")

ButtonPIZZABREAD=Button(frame3,text="PIZZA BREAD",width="15",font=("calibri",17,"bold"),height=5)
ButtonPIZZABREAD.grid(row=0,column=1,sticky="nsew")

ButtonBANANABREAD=Button(frame3,text="BANANA BREAD",width="15",font=("calibri",17,"bold"),height=5)
ButtonBANANABREAD.grid(row=0,column=2,sticky="nsew")


ButtonBAGUETTE=Button(frame3,text="BAGUETTE",width="15",font=("calibri",17,"bold"),height=5)
ButtonBAGUETTE.grid(row=1,column=0,sticky="nsew")

ButtonRYEBREAD=Button(frame3,text="RYE BREAD",width="15",font=("calibri",17,"bold"),height=5)
ButtonRYEBREAD.grid(row=1,column=1,sticky="nsew")

ButtonBRIOCHE=Button(frame3,text="BRIOCHE",width="15",font=("calibri",17,"bold"),height=5)
ButtonBRIOCHE.grid(row=1,column=2,sticky="nsew")


ButtonBUN=Button(frame3,text="BUN",width="15",font=("calibri",17,"bold"),height=5)
ButtonBUN.grid(row=2,column=0,sticky="nsew")

ButtonFOCACCIA=Button(frame3,width="15",text="FOCACCIA",font=("calibri",17,"bold"),height=5)
ButtonFOCACCIA.grid(row=2,column=1,sticky="nsew")

ButtonSOURDOUGH=Button(frame3,width="15",text="SOURDOUGH",font=("calibri",17,"bold"),height=5)
ButtonSOURDOUGH.grid(row=2,column=2,sticky="nsew")

ButtonWHITEBREAD=Button(frame3,width="15",text="WHITE BREAD",font=("calibri",17,"bold"),height=5)
ButtonWHITEBREAD.grid(row=3,column=0,sticky="nsew")

ButtonBROWNBREAD=Button(frame3,width="15",text="BROWN BREAD",font=("calibri",17,"bold"),height=5)
ButtonBROWNBREAD.grid(row=3,column=1,sticky="nsew")


ButtonCIABATTA=Button(frame3,text="CIABATTA",width="15",font=("calibri",17,"bold"),height=5)
ButtonCIABATTA.grid(row=3,column=2,sticky="nsew")

frame4=Frame(frame1,height="1200",width="700")
frame4.pack(anchor="center")


button1=Button(frame2,text="Groups",width="18",height="3",bg="black",fg="yellow",font=("calibri",14,"bold"))
button1.pack(anchor="nw",padx="30",pady="10")

button2=Button(frame2,text="Clear All",width="18",height="3",bg="black",fg="yellow",font=("calibri",14,"bold"))
button2.pack(anchor="nw",padx="30",pady="10")

button3=Button(frame2,text="Hold",bg="black",width="18",height="3",fg="yellow",font=("calibri",14,"bold"))
button3.pack(anchor="nw",padx="30",pady="10")

button4=Button(frame2,text="Records",bg="black",width="18",height="3",fg="yellow",font=("calibri",14,"bold"))
button4.pack(anchor="nw",padx="30",pady="10")

button5=Button(frame2,text="Change Payment Type",bg="black",width="18",height="3",fg="yellow",font=("calibri",14,"bold"))
button5.pack(anchor="nw",padx="30",pady="10")

button6=Button(frame2,text="Items",bg="black",width="18",fg="yellow",height="3",font=("calibri",14,"bold"))
button6.pack(anchor="nw",padx="30",pady="10")

button6=Button(frame2,text="Pay",bg="black",width="18",fg="yellow",height="3",font=("calibri",14,"bold"))
button6.pack(anchor="nw",padx="30",pady="10")




frame2=Frame(frame4,height="250",bg="skyblue",width="1400")
frame2.pack(side=TOP)

frame3=Frame(frame4,height="50",width="1600")
frame3.pack(side=TOP)

frame4=Frame(frame1,height="500",width="1400")
frame4.pack(side=TOP)

label1=Label(frame3,text="Quality",font=("calibri",18,"bold"))
label1.pack(side="left")

userEntry=Entry(frame3,width="3",font=("calibri",15,"bold"))
userEntry.pack(side="left",padx="9")

label2=Label(frame3,text="Total Amount",font=("calibri",18,"bold"))
label2.pack(side="left")

userEntry=Entry(frame3,width="7",font=("calibri",15,"bold"))
userEntry.pack(side="left",padx="9")

button=Button(frame3,text="<<Backspace",width="12",bd=7,font=("calibri",15,"bold"))
button.pack(side=RIGHT,padx="10");

frame5=Frame(frame4)
frame5.pack(side=TOP,fill=X)

userEntry=Entry(frame5,width="50",font=("calibri",15,"bold"))
userEntry.pack(side="top",pady=10)

frame2=Frame(frame4,bg="white",width="50")
frame2.pack(side=TOP,fill=BOTH,expand=True,pady=20)

frame11=Frame(frame2,height=800,width=200)
frame11.grid(row=0,column=0,sticky="nsew");

button=Button(frame11,bg="orange",text="7",height=1,width=10,font=("calibri",25,"bold"))
button.pack(fill=BOTH,expand=True);

frame12=Frame(frame2,height=80,width=200)
frame12.grid(row=0,column=1,sticky="nsew");

button=Button(frame12,bg="orange",text="8",width=10,font=("calibri",25,"bold"))
button.pack(fill=BOTH,expand=True);

frame13=Frame(frame2,height=80,width=200)
frame13.grid(row=0,column=2,sticky="nsew");

button=Button(frame13,bg="orange",text="9",width=10,font=("calibri",25,"bold"))
button.pack(fill=BOTH,expand=True);

frame14=Frame(frame2,height=80,width=200)
frame14.grid(row=1,column=0,sticky="nsew");

button=Button(frame14,bg="orange",text="4",width=10,height=1,font=("calibri",25,"bold"))
button.pack(fill=BOTH,expand=True);

frame15=Frame(frame2,height=80,width=200)
frame15.grid(row=1,column=1,sticky="nsew");

button=Button(frame15,bg="orange",text="5",width=10,font=("calibri",25,"bold"))
button.pack(fill=BOTH,expand=True);

frame16=Frame(frame2,height=80,width=200)
frame16.grid(row=1,column=2,sticky="nsew");

button=Button(frame16,bg="orange",text="6",width=10,font=("calibri",25,"bold"))
button.pack(fill=BOTH,expand=True);

frame17=Frame(frame2,height=80,width=200)
frame17.grid(row=2,column=0,sticky="nsew");

button=Button(frame17,bg="orange",text="1",width=10,height=1,font=("calibri",25,"bold"))
button.pack(fill=BOTH,expand=True);

frame18=Frame(frame2,height=80,width=200)
frame18.grid(row=2,column=1,sticky="nsew");

button=Button(frame18,bg="orange",text="2",width=10,font=("calibri",25,"bold"))
button.pack(fill=BOTH,expand=True);

frame19=Frame(frame2,height=80,width=200)
frame19.grid(row=2,column=2,sticky="nsew");

button=Button(frame19,bg="orange",text="3",width=10,font=("calibri",25,"bold"))
button.pack(fill=BOTH,expand=True);

frame20=Frame(frame2,height=80,width=200)
frame20.grid(row=3,column=0,sticky="nsew");

button=Button(frame20,bg="orange",text=".",width=10,height=1,font=("calibri",25,"bold"))
button.pack(fill=BOTH,expand=True);

frame21=Frame(frame2,height=80,width=200)
frame21.grid(row=3,column=1,sticky="nsew");

button=Button(frame21,bg="orange",text="0",width=10,font=("calibri",25,"bold"))
button.pack(fill=BOTH,expand=True);

frame22=Frame(frame2,height=80,width=200)
frame22.grid(row=3,column=2,sticky="nsew");

button=Button(frame22,bg="orange",text="Qty",width=10,font=("calibri",25,"bold"))
button.pack(fill=BOTH,expand=True);

root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_rowconfigure(2,weight=1)
root.grid_rowconfigure(3,weight=1)
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)




root.mainloop()