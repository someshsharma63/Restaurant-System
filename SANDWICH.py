from tkinter import *

root=Tk()
root.title("Sandwich")
root.geometry("500x500")

frameSandwich=Frame(root)
frameSandwich.pack(side="right",fill=BOTH,expand=True)

ButtonGRILLEDSANDWICH=Button(frameSandwich,text="BAURU",width="15",font=("calibri",17,"bold"),height=5)
ButtonGRILLEDSANDWICH.grid(row=0,column=0,sticky="nsew")

ButtonVEGETABLESANDWICH=Button(frameSandwich,text="CUBAN",width="15",font=("calibri",17,"bold"),height=5)
ButtonVEGETABLESANDWICH.grid(row=0,column=1,sticky="nsew")

ButtonAMERICANSANDWICH=Button(frameSandwich,text="DELI",width="15",font=("calibri",17,"bold"),height=5)
ButtonAMERICANSANDWICH.grid(row=0,column=2,sticky="nsew")

ButtonALOOMATARSANDWICH=Button(frameSandwich,text="GARLIC",width="15",font=("calibri",17,"bold"),height=5)
ButtonALOOMATARSANDWICH.grid(row=1,column=0,sticky="nsew")

ButtonTOMATOSANDWICH=Button(frameSandwich,text="TOMATO",width="15",font=("calibri",17,"bold"),height=5)
ButtonTOMATOSANDWICH.grid(row=1,column=1,sticky="nsew")

ButtonCHEESESANDWICH=Button(frameSandwich,text="CHEESE",width="15",font=("calibri",17,"bold"),height=5)
ButtonCHEESESANDWICH.grid(row=1,column=2,sticky="nsew")


ButtonPANEERSANDWICH=Button(frameSandwich,text="PANEER",width="15",font=("calibri",17,"bold"),height=5)
ButtonPANEERSANDWICH.grid(row=2,column=0,sticky="nsew")


ButtonGARLICSANDWICH=Button(frameSandwich,text="HAM",width="15",font=("calibri",17,"bold"),height=5)
ButtonGARLICSANDWICH.grid(row=2,column=1,sticky="nsew")

ButtonPLAINSANDWICH=Button(frameSandwich,text="PLAIN",width="15",font=("calibri",17,"bold"),height=5)
ButtonPLAINSANDWICH.grid(row=2,column=2,sticky="nsew")

ButtonCLUBSANDWICH=Button(frameSandwich,text="CLUB",width="15",font=("calibri",17,"bold"),height=5)
ButtonCLUBSANDWICH.grid(row=3,column=0,sticky="nsew")

ButtonJAMSANDWICH=Button(frameSandwich,text="JAM",width="15",font=("calibri",17,"bold"),height=5)
ButtonJAMSANDWICH.grid(row=3,column=1,sticky="nsew")

ButtonCORNSANDWICH=Button(frameSandwich,text="CORN",width="15",font=("calibri",17,"bold"),height=5)
ButtonCORNSANDWICH.grid(row=3,column=2,sticky="nsew")








root.mainloop()

