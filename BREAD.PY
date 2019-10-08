from tkinter import *

root=Tk()
root.title("BREAD")
root.geometry("500x500")

framebread=Frame(root)
framebread.pack(side="right",fill=BOTH,expand=True)

ButtonTOAST=Button(framebread,text="TOAST",width="15",font=("calibri",17,"bold"),height=5)
ButtonTOAST.grid(row=0,column=0,sticky="nsew")

ButtonPIZZABREAD=Button(framebread,text="PIZZA BREAD",width="15",font=("calibri",17,"bold"),height=5)
ButtonPIZZABREAD.grid(row=0,column=1,sticky="nsew")

ButtonBANANABREAD=Button(framebread,width="15",text="BANANA BREAD",font=("calibri",17,"bold"),height=5)
ButtonBANANABREAD.grid(row=0,column=2,sticky="nsew")


ButtonBAGUETTE=Button(framebread,text="BAGUETTE",width="15",font=("calibri",17,"bold"),height=5)
ButtonBAGUETTE.grid(row=1,column=0,sticky="nsew")

ButtonRYEBREAD=Button(framebread,text="RYE BREAD",width="15",font=("calibri",17,"bold"),height=5)
ButtonRYEBREAD.grid(row=1,column=1,sticky="nsew")

ButtonBRIOCHE=Button(framebread,text="BRIOCHE",width="15",font=("calibri",17,"bold"),height=5)
ButtonBRIOCHE.grid(row=1,column=2,sticky="nsew")


ButtonBUN=Button(framebread,text="BUN",width="15",font=("calibri",17,"bold"),height=5)
ButtonBUN.grid(row=2,column=0,sticky="nsew")

ButtonFOCACCIA=Button(framebread,width="15",text="FOCACCIA",font=("calibri",17,"bold"),height=5)
ButtonFOCACCIA.grid(row=2,column=1,sticky="nsew")

ButtonSOURDOUGH=Button(framebread,width="15",text="SOURDOUGH",font=("calibri",17,"bold"),height=5)
ButtonSOURDOUGH.grid(row=2,column=2,sticky="nsew")

ButtonWHITEBREAD=Button(framebread,width="15",text="WHITE BREAD",font=("calibri",17,"bold"),height=5)
ButtonWHITEBREAD.grid(row=3,column=0,sticky="nsew")

ButtonBROWNBREAD=Button(framebread,width="15",text="BROWN BREAD",font=("calibri",17,"bold"),height=5)
ButtonBROWNBREAD.grid(row=3,column=1,sticky="nsew")

ButtonCIABATTA=Button(framebread,text="CIABATTA",width="15",font=("calibri",17,"bold"),height=5)
ButtonCIABATTA.grid(row=3,column=2,sticky="nsew")













root.mainloop()

