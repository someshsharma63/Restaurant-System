from tkinter import *

root=Tk()
root.title("Cookies")
root.geometry("500x500")

frameCookies=Frame(root)
frameCookies.pack(side="right",fill=BOTH,expand=True)

ButtonBLUEBERRYYOGURT=Button(frameCookies,text="YOGURT",width="15",font=("calibri",17,"bold"),height=5)
ButtonBLUEBERRYYOGURT.grid(row=0,column=0,sticky="nsew")


ButtonROLLSUGAR=Button(frameCookies,text="ROLL SUGAR",width="15",font=("calibri",17,"bold"),height=5)
ButtonROLLSUGAR.grid(row=0,column=1,sticky="nsew")

ButtonBUTTEROATMEAL=Button(frameCookies,text="BUTTER OATMEAL",width="15",font=("calibri",17,"bold"),height=5)
ButtonBUTTEROATMEAL.grid(row=0,column=2,sticky="nsew")

ButtonBROWNSPICE=Button(frameCookies,text="BROWN SPICE",width="15",font=("calibri",17,"bold"),height=5)
ButtonBROWNSPICE.grid(row=1,column=0,sticky="nsew")


ButtonVANILLABEAN=Button(frameCookies,text="VANILLA BEAN",width="15",font=("calibri",17,"bold"),height=5)
ButtonVANILLABEAN.grid(row=1,column=1,sticky="nsew")

ButtonCARAMELPECAN=Button(frameCookies,text="CARAMEL PECAN ",width="15",font=("calibri",17,"bold"),height=5)
ButtonCARAMELPECAN.grid(row=1,column=2,sticky="nsew")


ButtonPIECRUST=Button(frameCookies,text="PIE CRUST",width="15",font=("calibri",17,"bold"),height=5)
ButtonPIECRUST.grid(row=2,column=0,sticky="nsew")


ButtonNUTELLALAVA=Button(frameCookies,text="NUTELLA LAVA",width="15",font=("calibri",17,"bold"),height=5)
ButtonNUTELLALAVA.grid(row=2,column=1,sticky="nsew")

ButtonPUBCOOKIES=Button(frameCookies,text="PUB COOKIES",width="15",font=("calibri",17,"bold"),height=5)
ButtonPUBCOOKIES.grid(row=2,column=2,sticky="nsew")


ButtonKITSILANO=Button(frameCookies,text="KITSILANO",width="15",font=("calibri",17,"bold"),height=5)
ButtonKITSILANO.grid(row=3,column=0,sticky="nsew")

ButtonAPRICOTOATMEAL=Button(frameCookies,text="APRICOT OATMEAL",width="15",font=("calibri",17,"bold"),height=5)
ButtonAPRICOTOATMEAL.grid(row=3,column=1,sticky="nsew")

ButtonALMONDJAM=Button(frameCookies,text="ALMOND JAM",width="15",font=("calibri",17,"bold"),height=5)
ButtonALMONDJAM.grid(row=3,column=2,sticky="nsew")







root.mainloop()

