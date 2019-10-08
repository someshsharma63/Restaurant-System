from tkinter import *

root=Tk()
root.title("MAGGIE")
root.geometry("500x500")

frameMaggie=Frame(root)
frameMaggie.pack(side="right",fill=BOTH,expand=True)

ButtonPLAINMAGGIE=Button(frameMaggie,text="PLAIN MAGGIE",width="15",font=("calibri",17,"bold"),height=5)
ButtonPLAINMAGGIE.grid(row=0,column=0,sticky="nsew")

ButtonMASALAMAGGIE=Button(frameMaggie,text="MASALA MAGGIE",width="15",font=("calibri",17,"bold"),height=5)
ButtonMASALAMAGGIE.grid(row=0,column=1,sticky="nsew")

ButtonTOMATOMAGGIE=Button(frameMaggie,text="TOMATO MAGGIE",width="15",font=("calibri",17,"bold"),height=5)
ButtonTOMATOMAGGIE.grid(row=0,column=2,sticky="nsew")


ButtonBREADMAGGIE=Button(frameMaggie,text="BREAD MAGGIE",width="15",font=("calibri",17,"bold"),height=5)
ButtonBREADMAGGIE.grid(row=1,column=0,sticky="nsew")


ButtonSOUPYMAGGIE=Button(frameMaggie,text="SOUPY MAGGIE",width="15",font=("calibri",17,"bold"),height=5)
ButtonSOUPYMAGGIE.grid(row=1,column=1,sticky="nsew")

ButtonPRAWNMAGGIE=Button(frameMaggie,text="PRAWN MAGGIE",width="15",font=("calibri",17,"bold"),height=5)
ButtonPRAWNMAGGIE.grid(row=1,column=2,sticky="nsew")


ButtonCHEESEMAGGIE=Button(frameMaggie,text="CHEESE MAGGIE",width="15",font=("calibri",17,"bold"),height=5)
ButtonCHEESEMAGGIE.grid(row=2,column=0,sticky="nsew")


ButtonCAPSICCUMMAGGIE=Button(frameMaggie,text="GARLIC MAGGIE",width="15",font=("calibri",17,"bold"),height=5)
ButtonCAPSICCUMMAGGIE.grid(row=2,column=1,sticky="nsew")

ButtonDEEPFRYMAGGIE=Button(frameMaggie,text="DEEPFRY MAGGIE",width="15",font=("calibri",17,"bold"),height=5)
ButtonDEEPFRYMAGGIE.grid(row=2,column=2,sticky="nsew")

ButtonONIONMAGGIE=Button(frameMaggie,text="ONION MAGGIE",width="15",font=("calibri",17,"bold"),height=5)
ButtonONIONMAGGIE.grid(row=3,column=0,sticky="nsew")

ButtonSALSAMAGGIE=Button(frameMaggie,text="SALSA MAGGIE",width="15",font=("calibri",17,"bold"),height=5)
ButtonSALSAMAGGIE.grid(row=3,column=1,sticky="nsew")

ButtonBUTTERMAGGIE=Button(frameMaggie,text="BUTTER MAGGIE",width="15",font=("calibri",17,"bold"),height=5)
ButtonBUTTERMAGGIE.grid(row=3,column=2,sticky="nsew")

root.mainloop()

