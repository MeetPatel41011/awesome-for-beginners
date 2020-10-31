# -*- coding: utf-8 -*-
"""
Created on Sun Aug  9 12:47:27 2020

@author: Geet Patel
"""
from tkinter import * 
import tkinter.messagebox as MessageBox
import mysql.connector

def insert():
    name2=name.get()
    add2=add.get();
    num2=int(num.get());
    Mild2=int(Mild.get());
    Moderate2=int(Moderate.get());
    Severe2=int(Severe.get());
    Critical2=int(Critical.get());
    
    mydb = mysql.connector.connect( 
    	user='root',
        password='meet41011',
        host="localhost",
      	database='pmp', 
      	)
    mycursor=mydb.cursor()
    
    #mycursor.execute=("insert into seats values('"+ name2 +"','"+ add2 +"','"+ num2 +"','"+ Mild2 +"','"+ Moderate2 +"','"+ Severe2 +"','"+ Critical2 +"')")
    #mycursor.execute("Create table seat2(name varchar(200), address varchar(20), num int(200), mild int(200), Moderate int(200), severe int(200), critical int(200))")
    mycursor.execute("INSERT INTO seat2 (name,address,num,mild,Moderate,severe,critical) VALUES (%s,%s,%s,%s,%s,%s,%s)" , (name2,add2,num2,Mild2,Moderate2,Severe2,Critical2 ))
    mydb.commit()
    
    MessageBox.showinfo("Insert Status", "Insert Successfully")
 
    name.delete(0,'end')
    add.delete(0,'end')
    num.delete(0,'end')
    Mild.delete(0,'end')
    Moderate.delete(0,'end')
    Severe.delete(0,'end')
    Critical.delete(0,'end')
    
    second()

def second():
    list1=[]
    
    mydb = mysql.connector.connect( 
    	user='root',
        password='meet41011',
        host="localhost",
      	database='pmp', 
      	)
    mycursor=mydb.cursor()
    
    mycursor.execute("SELECT * FROM seat2")
    myresult=mycursor.fetchall()
    root.destroy()
    root2=Tk()

    root2.title("Total number of seats")
    
    root2.geometry("700x700")
    
    listbox=Listbox(root2, width="700")
    listbox.insert(END, "H_Name | H_Add | H_Num | For Mild Patient | For Moderate Patient | For Severe Patient | For Critical Patient")
 
    listbox.grid(row="3", column="2")
   
    for item in myresult:
        listbox.insert(END, item)
    
    root2.mainloop()

root=Tk()

root.title("Total number of seats")

root.geometry("700x700")

#root.configure(background="black")

hospital_name=Label(root, text="Hospital Name", font = ('Helvetica', 12))
hospital_add=Label(root, text="Hospital Address", font = ('Helvetica', 12))
hospital_con_num=Label(root, text="Hospital Contact Number", font = ('Helvetica', 12))
For_Mild_Patient=Label(root, text="Seats For Mild Covid Patient", font = ('Helvetica', 12))
For_Moderate_Patient=Label(root, text="Seats For Moderate Covid Patient", font = ('Helvetica', 12))
For_Severe_Patient=Label(root, text="Seats For Severe Covid Patient", font = ('Helvetica', 12))
For_Critical_Patient=Label(root, text="Seats For Critical Covid Patient", font = ('Helvetica', 12))
                            
name=Entry(root)
add=Entry(root)
num=Entry(root)
Mild=Entry(root)
Moderate=Entry(root)
Severe=Entry(root)
Critical=Entry(root)

btn1=Button(root, text="Submit", command=insert, activebackground="red", activeforeground="black", width="25", bg="black", fg="red")
btn2=Button(root, text="For patient", command=second, activebackground="red", activeforeground="black", width="25", bg="black", fg="red")
hospital_name.grid(row="0", column="0")
hospital_add.grid(row="1", column="0")
hospital_con_num.grid(row="2", column="0")
For_Mild_Patient.grid(row="3", column="0")
For_Moderate_Patient.grid(row="4", column="0")
For_Severe_Patient.grid(row="5", column="0")
For_Critical_Patient.grid(row="6", column="0")

name.grid(row="0", column="2")
add.grid(row="1", column="2")
num.grid(row="2", column="2")
Mild.grid(row="3", column="2")
Moderate.grid(row="4", column="2")
Severe.grid(row="5", column="2")
Critical.grid(row="6", column="2")

btn1.grid(row="8", column="1")
btn2.grid(row="9", column="1")
root.mainloop()
#_______

    
