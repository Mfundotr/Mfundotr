from tkinter import *
from tkcalendar import * 
root=Tk()
root.title("Loan app")
root.geometry("500x400")
root.maxsize(1000,800 )
def write():
    firstname_info=firstname.get()
    lastname_info=lastname.get()
    surname_info=surname.get()
    phonenumber_info=phone_number.get()
    addressnumber_info=address_number.get()
    creditrequest_info=credit_request.get()
    payday_info=pay_day.get_date()
    
    
    file = open("loaners.txt", "a")
    file.write("\n _______________________") 
    file.write("\n First_name: " + firstname_info)
    file.write("\n Last name: " + lastname_info) 
    file.write("\n Surname: "+ surname_info) 
    file.write("\n Phone_number:" +phonenumber_info)
    file.write("\n Address_number:" + addressnumber_info)
    file.write("\n Credit_request:" + creditrequest_info) 
    file.write("\n Pay_Day: " +payday_info)

    
  
    
    file.close()
intro=Label(root, text="Loan Application Program:",  bg="grey",fg="black", width="500", height="3") 
intro.pack()
first_name= Label (root,text="Enter First Name:" )
first_name.place(x=171, y=175)
last_name= Label (root,text="Enter Last Name:" )
last_name.place(x=171, y=245)
surname =Label (root, text ="Enter Surname:")
surname.place(x=171,y =317)
phone_number=Label(root, text="Phone Number :") 
phone_number.place(x=171, y=360)
address_number=Label(root, text="Address Number :") 
address_number.place(x=171, y=404)

credit_request=Label(root, text="Enter Credit_request:")
credit_request.place(x=171, y=615)
pay_day= Calendar(root,selectmode="day", year=2022, month=6, day =8)
pay_day.place(x=100, y=900)
text=Label(root, text ="" ,  bg="grey",fg="black", width="500", height="1")  
text.place(x=1, y=850)
txt=Label(root, text="Enter Phone number: ")
txt.place(x=171, y=495)

firstname =StringVar()
lastname=StringVar()
surname=StringVar()
age=IntVar()
phone_number=StringVar()
address_number=StringVar()
credit_request=StringVar()


firstname_entry=Entry(textvariable =firstname)
firstname_entry.place(x=171,y=210, width=440) 
lastname_entry=Entry(textvariable =lastname)
lastname_entry.place(x=171,y =280, width=440)
surname_entry=Entry(textvariable =surname )
surname_entry.place(x=171,y=355, width=440) 
address_entry=Entry(textvariable=address_number) 

address_entry.place(x=171,y=450, width=440)
phonenumber= Entry(root, textvariable="phone_number")
phonenumber.place(x=171,y=540, width=440)
credit_entry=Entry (textvariable =credit_request)
credit_entry.place(x=171, y=675, width=440,) 
button=Button(text ="Submit", command=write)
button.place(x=280,y=1300)


footer=Label(root, text="",  bg="grey",fg="black", width="500", height="2") 
footer.place(x=0,y=1390)
root.mainloop()
