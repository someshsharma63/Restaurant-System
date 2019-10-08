from tkinter import *

root=Tk()
root.title("PavBhaji")
root.geometry("500x500")

framePavBhaji=Frame(root)
framePavBhaji.pack(side="right",fill=BOTH,expand=True)

ButtonSHADAPAVBHAJI=Button(framePavBhaji,text="SHADA",width="15",font=("calibri",17,"bold"),height=5)
ButtonSHADAPAVBHAJI.grid(row=0,column=0,sticky="nsew")

ButtonBUTTERPAVBHAJI=Button(framePavBhaji,text="BUTTER",width="15",font=("calibri",17,"bold"),height=5)
ButtonBUTTERPAVBHAJI.grid(row=0,column=1,sticky="nsew")

ButtonMASALAPAVBHAJI=Button(framePavBhaji,text="MASALA",width="15",font=("calibri",17,"bold"),height=5)
ButtonMASALAPAVBHAJI.grid(row=0,column=2,sticky="nsew")


ButtonSANDWICHPAVBHAJI=Button(framePavBhaji,text="SANDWICH",width="15",font=("calibri",17,"bold"),height=5)
ButtonSANDWICHPAVBHAJI.grid(row=1,column=0,sticky="nsew")


ButtonPAVBHAJIBURGER=Button(framePavBhaji,text="BURGER",width="15",font=("calibri",17,"bold"),height=5)
ButtonPAVBHAJIBURGER.grid(row=1,column=1,sticky="nsew")

ButtonJAINPAVBHAJI=Button(framePavBhaji,text="JAIN",width="15",font=("calibri",17,"bold"),height=5)
ButtonJAINPAVBHAJI.grid(row=1,column=2,sticky="nsew")

ButtonCHEESEPAVBHAJI=Button(framePavBhaji,text="CHEESE",width="15",font=("calibri",17,"bold"),height=5)
ButtonCHEESEPAVBHAJI.grid(row=2,column=0,sticky="nsew")

ButtonPAVBHAJIFONDUE=Button(framePavBhaji,text="FONDUE",width="15",font=("calibri",17,"bold"),height=5)
ButtonPAVBHAJIFONDUE.grid(row=2,column=1,sticky="nsew")

ButtonKHATIYAVADIPAVBHAJI=Button(framePavBhaji,text="KHATIYAVADI",width="15",font=("calibri",17,"bold"),height=5)
ButtonKHATIYAVADIPAVBHAJI.grid(row=2,column=2,sticky="nsew")

ButtonTOASTPAVBHAJI=Button(framePavBhaji,text="TOAST",width="15",font=("calibri",17,"bold"),height=5)
ButtonTOASTPAVBHAJI.grid(row=3,column=0,sticky="nsew")

ButtonKHADAPAVBHAJI=Button(framePavBhaji,text="KHADA",width="15",font=("calibri",17,"bold"),height=5)
ButtonKHADAPAVBHAJI.grid(row=3,column=1,sticky="nsew")

ButtonPUNJABIPAVBHAJI=Button(framePavBhaji,text="PUNJABI",width="15",font=("calibri",17,"bold"),height=5)
ButtonPUNJABIPAVBHAJI.grid(row=3,column=2,sticky="nsew")








root.mainloop()

