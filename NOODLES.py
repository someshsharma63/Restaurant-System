from tkinter import *

root=Tk()
root.title("Noodles")
root.geometry("500x500")

frameNoodles=Frame(root)
frameNoodles.pack(side="right",fill=BOTH,expand=True)

ButtonSESAMENODDLES=Button(frameNoodles,text="SESAME",width="15",font=("calibri",17,"bold"),height=5)
ButtonSESAMENODDLES.grid(row=0,column=0,sticky="nsew")

ButtonCHOWMEIN=Button(frameNoodles,text="CHOWMEIN",width="15",font=("calibri",17,"bold"),height=5)
ButtonCHOWMEIN.grid(row=0,column=1,sticky="nsew")

ButtonTOMATONODDLES=Button(frameNoodles,text="TOMATO",width="15",font=("calibri",17,"bold"),height=5)
ButtonTOMATONODDLES.grid(row=0,column=2,sticky="nsew")

ButtonMANCHOWNODDLES=Button(frameNoodles,text="MANCHOW",width="15",font=("calibri",17,"bold"),height=5)
ButtonMANCHOWNODDLES.grid(row=1,column=0,sticky="nsew")

ButtonHAKKANODDLES=Button(frameNoodles,text="HAKKA",width="15",font=("calibri",17,"bold"),height=5)
ButtonHAKKANODDLES.grid(row=1,column=1,sticky="nsew")

ButtonPANEERNODDLES=Button(frameNoodles,text="PANEER",width="15",font=("calibri",17,"bold"),height=5)
ButtonPANEERNODDLES.grid(row=1,column=2,sticky="nsew")


ButtonASIANNODDLES=Button(frameNoodles,text="ASIAN",width="15",font=("calibri",17,"bold"),height=5)
ButtonASIANNODDLES.grid(row=2,column=0,sticky="nsew")

ButtonOATSNODDLES=Button(frameNoodles,text="OATS",width="15",font=("calibri",17,"bold"),height=5)
ButtonOATSNODDLES.grid(row=2,column=1,sticky="nsew")

ButtonMEDITERNODDLES=Button(frameNoodles,text="MEDITER",width="15",font=("calibri",17,"bold"),height=5)
ButtonMEDITERNODDLES.grid(row=2,column=2,sticky="nsew")

ButtonSCHEZWAMNODDLES=Button(frameNoodles,text="SCHEZWAM",width="15",font=("calibri",17,"bold"),height=5)
ButtonSCHEZWAMNODDLES.grid(row=3,column=0,sticky="nsew")

ButtonSINGAPORENODDLES=Button(frameNoodles,text="GARLIC",width="15",font=("calibri",17,"bold"),height=5)
ButtonSINGAPORENODDLES.grid(row=3,column=1,sticky="nsew")

ButtonVEGETABLESNODDLES=Button(frameNoodles,text="VEGETABLES",width="15",font=("calibri",17,"bold"),height=5)
ButtonVEGETABLESNODDLES.grid(row=3,column=2,sticky="nsew")











root.mainloop()

