from tkinter import *

root=Tk()
root.title("SouthIndian")
root.geometry("500x500")

frameSouthIndian=Frame(root)
frameSouthIndian.pack(side="right",fill=BOTH,expand=True)

ButtonIDLISAMBHAR=Button(frameSouthIndian,text="IDLI SAMBHAR",width="15",font=("calibri",17,"bold"),height=5)
ButtonIDLISAMBHAR.grid(row=0,column=0,sticky="nsew")

ButtonIDLIVADAMIX=Button(frameSouthIndian,text="IDLIVADA MIX",width="15",font=("calibri",17,"bold"),height=5)
ButtonIDLIVADAMIX.grid(row=0,column=1,sticky="nsew")

ButtonSAMBHARVADA=Button(frameSouthIndian,text="SAMBHAR VADA",width="15",font=("calibri",17,"bold"),height=5)
ButtonSAMBHARVADA.grid(row=0,column=2,sticky="nsew")


ButtonPLAINDOSA=Button(frameSouthIndian,text="PLAIN DOSA",width="15",font=("calibri",17,"bold"),height=5)
ButtonPLAINDOSA.grid(row=1,column=0,sticky="nsew")

ButtonCHEESEDOSA=Button(frameSouthIndian,text="CHEESE DOSA",width="15",font=("calibri",17,"bold"),height=5)
ButtonCHEESEDOSA.grid(row=1,column=1,sticky="nsew")

ButtonRAVADOSA=Button(frameSouthIndian,text="RAVA DOSA",width="15",font=("calibri",17,"bold"),height=5)
ButtonRAVADOSA.grid(row=1,column=2,sticky="nsew")

ButtonCHEESEDOSA=Button(frameSouthIndian,text="CHEESE DOSA",width="15",font=("calibri",17,"bold"),height=5)
ButtonCHEESEDOSA.grid(row=2,column=0,sticky="nsew")


ButtonTOMATODOSA=Button(frameSouthIndian,text="TOMATO DOSA",width="15",font=("calibri",17,"bold"),height=5)
ButtonTOMATODOSA.grid(row=2,column=1,sticky="nsew")

ButtonMASALADOSA=Button(frameSouthIndian,text="MASALA DOSA",width="15",font=("calibri",17,"bold"),height=5)
ButtonMASALADOSA.grid(row=2,column=2,sticky="nsew")

ButtonMASALADOSA=Button(frameSouthIndian,text="MASALA DOSA",width="15",font=("calibri",17,"bold"),height=5)
ButtonMASALADOSA.grid(row=3,column=0,sticky="nsew")

ButtonONIONDOSA=Button(frameSouthIndian,text="ONION DOSA",width="15",font=("calibri",17,"bold"),height=5)
ButtonONIONDOSA.grid(row=3,column=1,sticky="nsew")

ButtonUTTAPUM=Button(frameSouthIndian,text="UTTAPUM",width="15",font=("calibri",17,"bold"),height=5)
ButtonUTTAPUM.grid(row=3,column=2,sticky="nsew")

root.mainloop()

