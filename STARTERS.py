from tkinter import *

root=Tk()
root.title("Starters")
root.geometry("500x500")

frameStarters=Frame(root)
frameStarters.pack(side="right",fill=BOTH,expand=True)

ButtonPIZZASAUCE=Button(frameStarters,text="PIZZA SAUCE",width="15",font=("calibri",17,"bold"),height=5)
ButtonPIZZASAUCE.grid(row=0,column=0,sticky="nsew")


ButtonBREADROOLS=Button(frameStarters,text="BREAD ROOLS",width="15",font=("calibri",17,"bold"),height=5)
ButtonBREADROOLS.grid(row=0,column=1,sticky="nsew")

ButtonFRIEDWONTONS=Button(frameStarters,text="FRIED WONTONS",width="15",font=("calibri",17,"bold"),height=5)
ButtonFRIEDWONTONS.grid(row=0,column=2,sticky="nsew")

ButtonAFGHANIPANEER=Button(frameStarters,text="AFGHANI PANEER",width="15",font=("calibri",17,"bold"),height=5)
ButtonAFGHANIPANEER.grid(row=1,column=0,sticky="nsew")

ButtonALOOTUK=Button(frameStarters,text="ALOO TUK",width="15",font=("calibri",17,"bold"),height=5)
ButtonALOOTUK.grid(row=1,column=1,sticky="nsew")

ButtonCAPSICUMDIP=Button(frameStarters,text="CAPSICUM DIP",width="15",font=("calibri",17,"bold"),height=5)
ButtonCAPSICUMDIP.grid(row=1,column=2,sticky="nsew")


ButtonCHEESEPOPPERS=Button(frameStarters,text="CHEESE POPPERS",width="15",font=("calibri",17,"bold"),height=5)
ButtonCHEESEPOPPERS.grid(row=2,column=0,sticky="nsew")

ButtonCHEESETACOS=Button(frameStarters,text="CHEESE TACOS",width="15",font=("calibri",17,"bold"),height=5)
ButtonCHEESETACOS.grid(row=2,column=1,sticky="nsew")

ButtonPANEERFRITTERS=Button(frameStarters,text="PANEER FRITTERS",width="15",font=("calibri",17,"bold"),height=5)
ButtonPANEERFRITTERS.grid(row=2,column=2,sticky="nsew")

ButtonDRAGONROLLS=Button(frameStarters,text="DRAGON ROLLS",width="15",font=("calibri",17,"bold"),height=5)
ButtonDRAGONROLLS.grid(row=3,column=0,sticky="nsew")


ButtonCHEESEFONDUE=Button(frameStarters,text="CHEESE FONDUE",width="15",font=("calibri",17,"bold"),height=5)
ButtonCHEESEFONDUE.grid(row=3,column=1,sticky="nsew")

ButtonVEGETABLECOINS=Button(frameStarters,text="VEGETABLE COINS",width="15",font=("calibri",17,"bold"),height=5)
ButtonVEGETABLECOINS.grid(row=3,column=2,sticky="nsew")





root.mainloop()

