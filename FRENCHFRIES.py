from tkinter import *

root=Tk()
root.title("FRENCHFRIES")
root.geometry("500x500")

frameFrenchfries=Frame(root)
frameFrenchfries.pack(side="right",fill=BOTH,expand=True)

ButtonCHEESEFRIES=Button(frameFrenchfries,text="CHEESE FRIES",width="15",font=("calibri",17,"bold"),height=5)
ButtonCHEESEFRIES.grid(row=0,column=0,sticky="nsew")

ButtonCOTTAGEFRIES=Button(frameFrenchfries,text="COTTAGE FRIES",width="15",font=("calibri",17,"bold"),height=5)
ButtonCOTTAGEFRIES.grid(row=0,column=1,sticky="nsew")

ButtonGARLICFRIES=Button(frameFrenchfries,text="GARLIC FRIES",width="15",font=("calibri",17,"bold"),height=5)
ButtonGARLICFRIES.grid(row=0,column=2,sticky="nsew")


ButtonSHOESTRINGFRIES=Button(frameFrenchfries,text="SHOESTRING FRIES",width="15",font=("calibri",17,"bold"),height=5)
ButtonSHOESTRINGFRIES.grid(row=1,column=0,sticky="nsew")

ButtonBELGIANFRIES=Button(frameFrenchfries,text="BELGIAN FRIES",width="15",font=("calibri",17,"bold"),height=5)
ButtonBELGIANFRIES.grid(row=1,column=1,sticky="nsew")

ButtonSTANDARDFRIES=Button(frameFrenchfries,text="STANDARD FRIES",width="15",font=("calibri",17,"bold"),height=5)
ButtonSTANDARDFRIES.grid(row=1,column=2,sticky="nsew")

ButtonCRINKLECUTFRIES=Button(frameFrenchfries,text="CRINKLECUT FRIES",width="15",font=("calibri",17,"bold"),height=5)
ButtonCRINKLECUTFRIES.grid(row=2,column=0,sticky="nsew")


ButtonPOTATOFRIES=Button(frameFrenchfries,text="POTATO FRIES",width="15",font=("calibri",17,"bold"),height=5)
ButtonPOTATOFRIES.grid(row=2,column=1,sticky="nsew")

ButtonWAFFLEFRIES=Button(frameFrenchfries,text="WAFFLE FRIES",width="15",font=("calibri",17,"bold"),height=5)
ButtonWAFFLEFRIES.grid(row=2,column=2,sticky="nsew")

ButtonCURLYFRIES=Button(frameFrenchfries,text="CURLY FRIES",width="15",font=("calibri",17,"bold"),height=5)
ButtonCURLYFRIES.grid(row=3,column=0,sticky="nsew")

ButtonSTEAKFRIES=Button(frameFrenchfries,text="STEAK FRIES",width="15",font=("calibri",17,"bold"),height=5)
ButtonSTEAKFRIES.grid(row=3,column=1,sticky="nsew")

ButtonPOTATOWEDGES=Button(frameFrenchfries,text="POTATO WEDGES",width="15",font=("calibri",17,"bold"),height=5)
ButtonPOTATOWEDGES.grid(row=3,column=2,sticky="nsew")

root.mainloop()

