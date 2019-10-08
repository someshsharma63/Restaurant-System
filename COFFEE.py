from tkinter import *

root=Tk()
root.title("Coffee")
root.geometry("500x500")

frameCoffee=Frame(root)
frameCoffee.pack(side="right",fill=BOTH,expand=True)

ButtonCOLDCOFFEE=Button(frameCoffee,text="COLD COFFEE",width="15",font=("calibri",17,"bold"),height=5)
ButtonCOLDCOFFEE.grid(row=0,column=0,sticky="nsew")

ButtonHOTCOFFEE=Button(frameCoffee,text="HOT COFFEE",width="15",font=("calibri",17,"bold"),height=5)
ButtonHOTCOFFEE.grid(row=0,column=1,sticky="nsew")

ButtonCOFFEEAMERICANO=Button(frameCoffee,text="AMERICANO",width="15",font=("calibri",17,"bold"),height=5)
ButtonCOFFEEAMERICANO.grid(row=0,column=2,sticky="nsew")

ButtonCAPPUCCINO=Button(frameCoffee,text="CAPPUCCINO",width="15",font=("calibri",17,"bold"),height=5)
ButtonCAPPUCCINO.grid(row=1,column=0,sticky="nsew")

ButtonESPRESSOCOFFEE=Button(frameCoffee,text="ESPRESSO COFFEE",width="15",font=("calibri",17,"bold"),height=5)
ButtonESPRESSOCOFFEE.grid(row=1,column=1,sticky="nsew")

ButtonWHITECOFFEE=Button(frameCoffee,text="WHITE COFFEE",width="15",font=("calibri",17,"bold"),height=5)
ButtonWHITECOFFEE.grid(row=1,column=2,sticky="nsew")


ButtonIRISHCOFFEE=Button(frameCoffee,text="IRISH COFFEE",width="15",font=("calibri",17,"bold"),height=5)
ButtonIRISHCOFFEE.grid(row=2,column=0,sticky="nsew")

ButtonMOCHACCINO=Button(frameCoffee,text="MOCHACCINO",width="15",font=("calibri",17,"bold"),height=5)
ButtonMOCHACCINO.grid(row=2,column=1,sticky="nsew")

ButtonVIENNACOFFEE=Button(frameCoffee,text="VIENNA COFFEE",width="15",font=("calibri",17,"bold"),height=5)
ButtonVIENNACOFFEE.grid(row=2,column=2,sticky="nsew")

ButtonICECREAMCOFFEE=Button(frameCoffee,text="ICECREAM COFFEE",width="15",font=("calibri",17,"bold"),height=5)
ButtonICECREAMCOFFEE.grid(row=3,column=0,sticky="nsew")

ButtonBLACKCOFFEE=Button(frameCoffee,text="BLACK COFFEE",width="15",font=("calibri",17,"bold"),height=5)
ButtonBLACKCOFFEE.grid(row=3,column=1,sticky="nsew")

ButtonAFFOGATO=Button(frameCoffee,text="AFFOGATO",width="15",font=("calibri",17,"bold"),height=5)
ButtonAFFOGATO.grid(row=3,column=2,sticky="nsew")












root.mainloop()

