from tkinter import *

root=Tk()
root.title("Soup")
root.geometry("500x500")

frameSoup=Frame(root)
frameSoup.pack(side="right",fill=BOTH,expand=True)

ButtonCABBAGESOUP=Button(frameSoup,text="CABBAGE SOUP",width="15",font=("calibri",17,"bold"),height=5)
ButtonCABBAGESOUP.grid(row=0,column=0,sticky="nsew")

ButtonCARROTSOUP=Button(frameSoup,text="CARROT SOUP",width="15",font=("calibri",17,"bold"),height=5)
ButtonCARROTSOUP.grid(row=0,column=1,sticky="nsew")

ButtonASPARAGUSSOUP=Button(frameSoup,text="LENTIL SOUP",width="15",font=("calibri",17,"bold"),height=5)
ButtonASPARAGUSSOUP.grid(row=0,column=2,sticky="nsew")

ButtonMUSHROOMSOUP=Button(frameSoup,text="TOMATO SOUP",width="15",font=("calibri",17,"bold"),height=5)
ButtonMUSHROOMSOUP.grid(row=1,column=0,sticky="nsew")

ButtonCUCUMBERSOUP=Button(frameSoup,text="CUCUMBER SOUP",width="15",font=("calibri",17,"bold"),height=5)
ButtonCUCUMBERSOUP.grid(row=1,column=1,sticky="nsew")

ButtonERU=Button(frameSoup,text="KALE SOUP",width="15",font=("calibri",17,"bold"),height=5)
ButtonERU.grid(row=1,column=2,sticky="nsew")

ButtonSOURSOUP=Button(frameSoup,text="SOUR SOUP",width="15",font=("calibri",17,"bold"),height=5)
ButtonSOURSOUP.grid(row=2,column=0,sticky="nsew")


ButtonKAWLATA=Button(frameSoup,text="KAWLATA",width="15",font=("calibri",17,"bold"),height=5)
ButtonKAWLATA.grid(row=2,column=1,sticky="nsew")

ButtonKUSKSU=Button(frameSoup,text="KUSKSU",width="15",font=("calibri",17,"bold"),height=5)
ButtonKUSKSU.grid(row=2,column=2,sticky="nsew")

ButtonBROCCOLISOUP=Button(frameSoup,text="BROCCOLI SOUP",width="15",font=("calibri",17,"bold"),height=5)
ButtonBROCCOLISOUP.grid(row=3,column=0,sticky="nsew")

ButtonFRENCHSOUP=Button(frameSoup,text="FRENCH SOUP",width="15",font=("calibri",17,"bold"),height=5)
ButtonFRENCHSOUP.grid(row=3,column=1,sticky="nsew")

ButtonMINESTRONE=Button(frameSoup,text="MINESTRONE",width="15",font=("calibri",17,"bold"),height=5)
ButtonMINESTRONE.grid(row=3,column=2,sticky="nsew")












root.mainloop()

