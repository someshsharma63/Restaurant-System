from tkinter import *

root=Tk()
root.title("Pasta")
root.geometry("500x500")

framePasta=Frame(root)
framePasta.pack(side="right",fill=BOTH,expand=True)

ButtonCHEESEPASTA=Button(framePasta,text="CHEESE PASTA",width="15",font=("calibri",17,"bold"),height=5)
ButtonCHEESEPASTA.grid(row=0,column=0,sticky="nsew")

ButtonPEASPASTA=Button(framePasta,text="PEAS PASTA",width="15",font=("calibri",17,"bold"),height=5)
ButtonPEASPASTA.grid(row=0,column=1,sticky="nsew")

ButtonGRILLEDPASTA=Button(framePasta,text="GRILLED PASTA",width="15",font=("calibri",17,"bold"),height=5)
ButtonGRILLEDPASTA.grid(row=0,column=2,sticky="nsew")


ButtonSHEUPASTA=Button(framePasta,text="SHEU PASTA",width="15",font=("calibri",17,"bold"),height=5)
ButtonSHEUPASTA.grid(row=1,column=0,sticky="nsew")

ButtonBROCCOLIPASTA=Button(framePasta,text="BROCCOLI PASTA",width="15",font=("calibri",17,"bold"),height=5)
ButtonBROCCOLIPASTA.grid(row=1,column=1,sticky="nsew")

ButtonHERBPASTA=Button(framePasta,text="HERB PASTA",width="15",font=("calibri",17,"bold"),height=5)
ButtonHERBPASTA.grid(row=1,column=2,sticky="nsew")


ButtonBEANSPASTA=Button(framePasta,text="BEANS PASTA",width="15",font=("calibri",17,"bold"),height=5)
ButtonBEANSPASTA.grid(row=2,column=0,sticky="nsew")

ButtonSPINACHPASTA=Button(framePasta,text="SPINACH PASTA",width="15",font=("calibri",17,"bold"),height=5)
ButtonSPINACHPASTA.grid(row=2,column=1,sticky="nsew")

ButtonITALIANPASTA=Button(framePasta,text="ITALIAN PASTA",width="15",font=("calibri",17,"bold"),height=5)
ButtonITALIANPASTA.grid(row=2,column=2,sticky="nsew")

ButtonONIONPASTA=Button(framePasta,text="ONION PASTA",width="15",font=("calibri",17,"bold"),height=5)
ButtonONIONPASTA.grid(row=3,column=0,sticky="nsew")

ButtonTOMATOPASTA=Button(framePasta,text="TOMATO PASTA",width="15",font=("calibri",17,"bold"),height=5)
ButtonTOMATOPASTA.grid(row=3,column=1,sticky="nsew")

ButtonGARLICPASTA=Button(framePasta,text="GARLIC PASTA",width="15",font=("calibri",17,"bold"),height=5)
ButtonGARLICPASTA.grid(row=3,column=2,sticky="nsew")











root.mainloop()

