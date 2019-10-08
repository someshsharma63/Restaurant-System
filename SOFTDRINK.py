from tkinter import *

root=Tk()
root.title("SOFTDRINK")
root.geometry("500x500")

frameSoftdrink=Frame(root)
frameSoftdrink.pack(side="right",fill=BOTH,expand=True)

ButtonTHUMSUP=Button(frameSoftdrink,text="THUMS UP",width="15",font=("calibri",17,"bold"),height=5)
ButtonTHUMSUP.grid(row=0,column=0,sticky="nsew")

ButtonPEPSI=Button(frameSoftdrink,text="PEPSI",width="15",font=("calibri",17,"bold"),height=5)
ButtonPEPSI.grid(row=0,column=1,sticky="nsew")

ButtonCOCACOLA=Button(frameSoftdrink,text="COCA-COLA",width="15",font=("calibri",17,"bold"),height=5)
ButtonCOCACOLA.grid(row=0,column=2,sticky="nsew")


ButtonLIMCA=Button(frameSoftdrink,text="LIMCA",width="15",font=("calibri",17,"bold"),height=5)
ButtonLIMCA.grid(row=1,column=0,sticky="nsew")

ButtonMIRINDA=Button(frameSoftdrink,text="MIRINDA",width="15",font=("calibri",17,"bold"),height=5)
ButtonMIRINDA.grid(row=1,column=1,sticky="nsew")

ButtonFANTA=Button(frameSoftdrink,text="FANTA",width="15",font=("calibri",17,"bold"),height=5)
ButtonFANTA.grid(row=1,column=2,sticky="nsew")


ButtonMAAZA=Button(frameSoftdrink,text="MAAZA",width="15",font=("calibri",17,"bold"),height=5)
ButtonMAAZA.grid(row=2,column=0,sticky="nsew")

ButtonMOUNTAINDEW=Button(frameSoftdrink,text="MOUNTAIN DEW",width="15",font=("calibri",17,"bold"),height=5)
ButtonMOUNTAINDEW.grid(row=2,column=1,sticky="nsew")

ButtonSLICE=Button(frameSoftdrink,text="SLICE",width="15",font=("calibri",17,"bold"),height=5)
ButtonSLICE.grid(row=2,column=2,sticky="nsew")

ButtonSPRITE=Button(frameSoftdrink,text="SPRITE",width="15",font=("calibri",17,"bold"),height=5)
ButtonSPRITE.grid(row=3,column=0,sticky="nsew")

Button7Up=Button(frameSoftdrink,text="7 Up",width="15",font=("calibri",17,"bold"),height=5)
Button7Up.grid(row=3,column=1,sticky="nsew")

ButtonFROOTI=Button(frameSoftdrink,text="FROOTI",width="15",font=("calibri",17,"bold"),height=5)
ButtonFROOTI.grid(row=3,column=2,sticky="nsew")















root.mainloop()

