from tkinter import *

root=Tk()
root.title("MANCHURIAN")
root.geometry("500x500")

frameManchurian=Frame(root)
frameManchurian.pack(side="right",fill=BOTH,expand=True)

ButtonVEGMANCHURIAN=Button(frameManchurian,text="VEG",width="15",font=("calibri",17,"bold"),height=5)
ButtonVEGMANCHURIAN.grid(row=0,column=0,sticky="nsew")


ButtonDRYMANCHURIAN=Button(frameManchurian,text="DRY",width="15",font=("calibri",17,"bold"),height=5)
ButtonDRYMANCHURIAN.grid(row=0,column=1,sticky="nsew")

ButtonGRAVYMANCHURIAN=Button(frameManchurian,text="GRAVY",width="15",font=("calibri",17,"bold"),height=5)
ButtonGRAVYMANCHURIAN.grid(row=0,column=2,sticky="nsew")


ButtonDRYGOBIMANCHURIAN=Button(frameManchurian,text="GOBI",width="15",font=("calibri",17,"bold"),height=5)
ButtonDRYGOBIMANCHURIAN.grid(row=1,column=0,sticky="nsew")


ButtonTOMATOMANCHURIAN=Button(frameManchurian,text="TOMATO",width="15",font=("calibri",17,"bold"),height=5)
ButtonTOMATOMANCHURIAN.grid(row=1,column=1,sticky="nsew")


ButtonMASHROOMMANCHURIAN=Button(frameManchurian,text="MASHROOM",width="15",font=("calibri",17,"bold"),height=5)
ButtonMASHROOMMANCHURIAN.grid(row=1,column=2,sticky="nsew")

ButtonGARLICMANCHURIAN=Button(frameManchurian,text="GARLIC",width="15",font=("calibri",17,"bold"),height=5)
ButtonGARLICMANCHURIAN.grid(row=2,column=0,sticky="nsew")

ButtonDRYPANEERMANCHURIAN=Button(frameManchurian,text="DRYPANEER",width="15",font=("calibri",17,"bold"),height=5)
ButtonDRYPANEERMANCHURIAN.grid(row=2,column=1,sticky="nsew")

ButtonCORNMANCHURIAN=Button(frameManchurian,text="CORN",width="15",font=("calibri",17,"bold"),height=5)
ButtonCORNMANCHURIAN.grid(row=2,column=2,sticky="nsew")

ButtonGRAVYCORNMANCHURIAN=Button(frameManchurian,text="GRAVYCORN",width="15",font=("calibri",17,"bold"),height=5)
ButtonGRAVYCORNMANCHURIAN.grid(row=3,column=0,sticky="nsew")

ButtonIDLIMANCHURIAN=Button(frameManchurian,text="IDLI",width="15",font=("calibri",17,"bold"),height=5)
ButtonIDLIMANCHURIAN.grid(row=3,column=1,sticky="nsew")

ButtonDRYIDLIMANCHURIAN=Button(frameManchurian,text="DRYIDLI",width="15",font=("calibri",17,"bold"),height=5)
ButtonDRYIDLIMANCHURIAN.grid(row=3,column=2,sticky="nsew")

root.mainloop()

