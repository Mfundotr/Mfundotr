from tkinter import *
from tkinter import messagebox

race =[]
def displayInfo(race, name):
    found =False
    pos =0
    while pos <  len(race) and not found:
         if race[pos][0] == name:
                     found =True
         pos +=1
    if found:
        messagebox.showerror(message="___Verified Tickit_____")
        
    else:
        messagebox.showerror(message="Invalid Tickit")
def clickArea():
    fin =set(displayInfo(race, name.get()))
    fin=IntVar()
    
def createList() :
    racefile =open("List.txt","r")
    for line in racefile:
        racer = line.split()
        race.append(racer)
    
    racefile.close()
    return race
root =Tk()
root.title('mfundo.com')

name =StringVar()
Entry(root, textvariable=name, bg="grey",fg="black", width="25",).place(x=160,y=200) 
Label(root, text ="Note: No record no entry!", bg="grey",fg="black", width="25", height="2").place(x=160,y=100)

button =Button(root, text="CHECK ", command=clickArea).place(x=260,y=690)
createList()
root.mainloop( )
