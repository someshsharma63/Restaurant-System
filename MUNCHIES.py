from tkinter import *

root=Tk()
root.title("Munchies")
root.geometry("500x500")

frameMunchies=Frame(root)
frameMunchies.pack(side="right",fill=BOTH,expand=True)

ButtonTOPPINGS=Button(frameMunchies,text="TOPPINGS",width="15",font=("calibri",17,"bold"),height=5)
ButtonTOPPINGS.grid(row=0,column=0,sticky="nsew")

ButtonBURGERS=Button(frameMunchies,text="BURGERS",width="15",font=("calibri",17,"bold"),height=5)
ButtonBURGERS.grid(row=0,column=1,sticky="nsew")

ButtonDIPS=Button(frameMunchies,text="DIPS",width="15",font=("calibri",17,"bold"),height=5)
ButtonDIPS.grid(row=0,column=2,sticky="nsew")

ButtonSEAFOOD=Button(frameMunchies,text="SEA FOOD",width="15",font=("calibri",17,"bold"),height=5)
ButtonSEAFOOD.grid(row=1,column=0,sticky="nsew")

ButtonWRAPS=Button(frameMunchies,text="WRAPS",width="15",font=("calibri",17,"bold"),height=5)
ButtonWRAPS.grid(row=1,column=1,sticky="nsew")

ButtonNEWMOCKTAILS=Button(frameMunchies,text="NEW MOCKTAILS",width="15",font=("calibri",17,"bold"),height=5)
ButtonNEWMOCKTAILS.grid(row=1,column=2,sticky="nsew")


ButtonMILKSHAKES=Button(frameMunchies,text="MILK SHAKES",width="15",font=("calibri",17,"bold"),height=5)
ButtonMILKSHAKES.grid(row=2,column=0,sticky="nsew")


ButtonSALADS=Button(frameMunchies,text="SALADS",width="15",font=("calibri",17,"bold"),height=5)
ButtonSALADS.grid(row=2,column=1,sticky="nsew")

ButtonSOUPS=Button(frameMunchies,text="SOUPS",width="15",font=("calibri",17,"bold"),height=5)
ButtonSOUPS.grid(row=2,column=2,sticky="nsew")

ButtonTREATS=Button(frameMunchies,text="TREATS",width="15",font=("calibri",17,"bold"),height=5)
ButtonTREATS.grid(row=3,column=0,sticky="nsew")

ButtonDESSERTS=Button(frameMunchies,text="DESSERTS",width="15",font=("calibri",17,"bold"),height=5)
ButtonDESSERTS.grid(row=3,column=1,sticky="nsew")

ButtonPIZZAS=Button(frameMunchies,text="PIZZAS",width="15",font=("calibri",17,"bold"),height=5)
ButtonPIZZAS.grid(row=3,column=2,sticky="nsew")











root.mainloop()

