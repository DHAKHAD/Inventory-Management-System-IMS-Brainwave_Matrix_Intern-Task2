from email import message_from_string
from logging import root
from multiprocessing import parent_process
from multiprocessing.context import set_spawning_popen
from os import stat
from tkinter import*
from tkinter import ttk
from PIL import Image, ImageTk
from numpy import save
from tkinter import messagebox
import cv2
import os
import sqlite3
from tkcalendar import DateEntry

class sup:
    def __init__(self,root):
      self.root=root
      self.root.geometry("1530x790+0+0")
      self.root.title("Inventory Management System")

      # ============variables================
      self.var_EmployeeName=StringVar()
      self.var_EmployeeID=StringVar()
      self.var_Date=StringVar()
      self.var_Invoice=StringVar()
      self.var_Mobile=StringVar()
      self.var_Address=StringVar()
      self.var_searchby=StringVar()
      self.var_searchtext=StringVar() 


      #background Image
      img=Image.open(r"Img/leftm.jpg")
      img=img.resize((1530,790),Image.LANCZOS)
      self.photoimg=ImageTk.PhotoImage(img)

      bg_img=Label(self.root,image=self.photoimg)
      bg_img.place(x=0,y=0,width=1530,height=790)

      title_lbl=Label(bg_img,text="Manage Product Supplier", font=("Times New Roman", 30, "bold"), bg="darkblue", fg="white")
      title_lbl.place(x=0, y=0, width=1530, height=50)

      main_frame=Frame(bg_img, bd=2,bg="white")
      main_frame.place(x=10, y=55, width=1500, height=720)

      #Left Frame
      Left_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Employee Details", font=("Times New Roman",15, "bold"))
      Left_frame.place(x=15, y=10, width=720, height=680)

      #Right Frame
      Right_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Employee Details", font=("Times New Roman",15, "bold"))
      Right_frame.place(x=755, y=10, width=720, height=680)

      img=Image.open(r"Img/supp.png")
      img=img.resize((700,220),Image.LANCZOS)
      self.photoimg=ImageTk.PhotoImage(img)

      bg_img=Label(Right_frame,image=self.photoimg)
      bg_img.place(x=10,y=430,width=700,height=220)

      #Current Course Frame
      Currrent_Course_frame=LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE, text="Current  Details", font=("Times New Roman",15, "bold"))
      Currrent_Course_frame.place(x=5, y=10, width=705, height=150)
      #department

      year_label = Label(Currrent_Course_frame, text="Date", font=("times new roman", 12, "bold"), bg="white")
      year_label.grid(row=1, column=0, padx=10, sticky=W)

# DateEntry for date selection
      year_entry = DateEntry(Currrent_Course_frame,textvariable=self.var_Date, width=20,font=("times new roman", 12, "bold"), background='white', foreground='white', borderwidth=2, date_pattern='mm-dd-yyyy') # type: ignore
      year_entry.grid(row=1, column=1, padx=6, pady=10, sticky=W)
      #course
      
      user_label=Label(Currrent_Course_frame, text="Invoice No.",bg="white", font=("Times New Roman",15, "bold"))
      user_label.grid(row=2, column=0, padx=10)

      pass_entry=ttk.Entry(Currrent_Course_frame, textvariable=self.var_Invoice,width=17, font=("times new roman", 15, "bold"))
      pass_entry.grid(row=2, column=1, padx=2,pady=10, sticky=W)

      #Student Information
      Employee_Information_frame=LabelFrame(Left_frame,bd=2,bg="white", relief=RIDGE, text="Employee Information", font=("Times New Roman",15, "bold"))
      Employee_Information_frame.place(x=5, y=165, width=705, height=480)

      StudentId_label=Label(Employee_Information_frame, text="Employee ID",bg="white", font=("Times New Roman",15, "bold"))
      StudentId_label.grid(row=0, column=0, padx=10,pady=10, sticky=W)

      StudentId_entry=ttk.Entry(Employee_Information_frame,textvariable=self.var_EmployeeID, width=50, font=("times new roman", 15, "bold"))
      StudentId_entry.grid(row=0, column=1, padx=10,pady=10, sticky=W)

      StudentName_label=Label(Employee_Information_frame, text="Employee Name",bg="white", font=("Times New Roman",15, "bold"))
      StudentName_label.grid(row=1, column=0, padx=10,pady=10, sticky=W)

      StudentName_entry=ttk.Entry(Employee_Information_frame, textvariable=self.var_EmployeeName,width=50, font=("times new roman", 15, "bold"))
      StudentName_entry.grid(row=1, column=1, padx=10,pady=10, sticky=W)
      Contact_label=Label(Employee_Information_frame, text="Contact Number",bg="white", font=("Times New Roman",15, "bold"))
      Contact_label.grid(row=4, column=0, padx=10,pady=10, sticky=W)

      Contact_entry=ttk.Entry(Employee_Information_frame,textvariable=self.var_Mobile ,width=50, font=("times new roman", 15, "bold"))
      Contact_entry.grid(row=4, column=1, padx=10,pady=10, sticky=W)

      add_label=Label(Employee_Information_frame, text="Address",bg="white", font=("Times New Roman",15, "bold"))
      add_label.grid(row=6, column=0, padx=10,pady=10, sticky=W)

      add_entry=ttk.Entry(Employee_Information_frame, textvariable=self.var_Address,width=50, font=("times new roman", 15, "bold"))
      add_entry.grid(row=6, column=1,ipady=20, padx=10,pady=10, sticky=W)


      #buttons Frame
      btn_frame=Frame(Employee_Information_frame, bd=2, relief=RIDGE, bg="white")
      btn_frame.place(x=0, y=340, width=700, height=80)

      save_btn=Button(btn_frame,text="Save",command=self.add_data, width=29,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
      save_btn.grid(row=0, column=0)

      update_btn=Button(btn_frame,text="Update",command=self.update_data, width=29,font=("Times New Roman", 15, "bold"), bg="green", fg="white")
      update_btn.grid(row=0, column=1)

      Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data, width=29,font=("Times New Roman", 15, "bold"), bg="red", fg="white")
      Delete_btn.grid(row=1, column=0)

      Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data ,width=29,font=("Times New Roman", 15, "bold"), bg="#009688", fg="white")
      Reset_btn.grid(row=1, column=1)

      

      #=============Search System================
      Search_frame=LabelFrame(Right_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("Times New Roman", 15, "bold"))
      Search_frame.place(x=10, y=5, width=700, height=100)

      search_combo=ttk.Combobox(Search_frame,textvariable=self.var_searchby, font=("Times New Roman",15, "bold"), width=12, state="readonly")
      search_combo["values"]=("Select","Invoice No.", "Mobile No.")
      search_combo.current(0)
      search_combo.grid(row=0, column=1,padx=2, pady=10, sticky=W)

      SearchEntry=ttk.Entry(Search_frame,textvariable=self.var_searchtext, width=18, font=("Times New Roman",15, "bold"))
      SearchEntry.grid(row=0, column=2,padx=2, pady=10, sticky=W)

      search_btn=Button(Search_frame,text="Search",command=self.search, width=12,font=("Times New Roman", 12, "bold"), bg="green", fg="white")
      search_btn.grid(row=0, column=3, padx=2, pady=10)

      Showall_btn=Button(Search_frame,text="Show All",command=self.show, width=12,font=("Times New Roman", 12, "bold"), bg="blue", fg="white")
      Showall_btn.grid(row=0, column=4, padx=2, pady=10)

      #=============Table Frame==============
      Table_frame=Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
      Table_frame.place(x=10, y=130, width=700, height=300)

      scroll_x=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
      scroll_y=ttk.Scrollbar(Table_frame, orient=VERTICAL)

      self.supplier_table=ttk.Treeview(Table_frame,column=("EmployeeName", "EmployeeID",  "Date", "Invoice", "Mobile","Address"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
      scroll_x.pack(side=BOTTOM, fill=X)
      scroll_y.pack(side=RIGHT, fill=Y)
      scroll_x.config(command=self.supplier_table.xview)
      scroll_y.config(command=self.supplier_table.yview)

      self.supplier_table.heading("EmployeeName", text="Employee Name")
      self.supplier_table.heading("EmployeeID", text="Employee ID")
      
      self.supplier_table.heading("Date", text="Date")
      self.supplier_table.heading("Invoice", text="Invoice No.")
      self.supplier_table.heading("Mobile", text="Mobile No.")
      self.supplier_table.heading("Address",text="Address")

      self.supplier_table["show"]="headings"
      self.supplier_table.column("EmployeeName", width=100)

      self.supplier_table.pack(fill=BOTH, expand=1)
      self.supplier_table.bind("<ButtonRelease>",self.get_cursor)
      self.fetch_data()

    # =================Function================
    def add_data(self):
      if self.var_EmployeeName.get()=="" or self.var_EmployeeID.get()=="" or self.var_EmployeeName.get()=="Select EmployeeName":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
      else:
        try: 
          conn=sqlite3.connect('SQL Database/IMS.db')
          my_cursor = conn.cursor()
          my_cursor.execute("INSERT INTO supplier VALUES(?,?,?,?,?,?)", (
            self.var_EmployeeName.get(),
            self.var_EmployeeID.get(),
            self.var_Date.get(),
            self.var_Invoice.get(),
            self.var_Mobile.get(),
            self.var_Address.get()
      
            ))

          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Success", "Added Succesfully", parent=self.root)
        except Exception as es:
          messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    # ==============Fetch Data========================
    def fetch_data(self):
      conn=sqlite3.connect('SQL Database/IMS.db')
      my_cursor = conn.cursor()
      my_cursor.execute("select * from supplier")
      data=my_cursor.fetchall()

      if len(data)!=0:
        self.supplier_table.delete(*self.supplier_table.get_children())
        for i in data:
          self.supplier_table.insert('',END, values=i)
      conn.commit()
      conn.close()

    #===================get cursor==============
    def get_cursor(self,event=""):
      cursor_focus=self.supplier_table.focus()
      content=self.supplier_table.item(cursor_focus)
      data=content["values"]
      
      self.var_EmployeeName.set(data[0])
      self.var_EmployeeID.set(data[1])
      self.var_Date.set(data[4])
      self.var_Invoice.set(data[5])
      self.var_Mobile.set(data[6])
      self.var_Address.set(data[10])
    
      
    #=======================update================
    
    def update_data(self):
        if self.var_EmployeeName.get() == "" or self.var_EmployeeID.get() == "" or self.var_EmployeeName.get() == "Select EmployeeName":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this Supplier details?", parent=self.root)
                if update:
                    conn = sqlite3.connect('SQL Database/IMS.db')
                    my_cursor = conn.cursor()
    
                    my_cursor.execute(
                        "UPDATE supplier SET EmployeeName=?, Date=?, Invoice=?, Mobile=?,Address=? WHERE EmployeeID=?",
                        (
                            self.var_EmployeeName.get(),
                            self.var_Date.get(),
                            self.var_Invoice.get(),
                            self.var_Mobile.get(),
                            self.var_Address.get(),
                            self.var_EmployeeID.get()  # Ensure EmployeeID is in the WHERE condition
                        )
                    )
    
                    conn.commit()
                    conn.close()
    
                    messagebox.showinfo("Success", "Supplier details updated", parent=self.root)
                    self.fetch_data()
    
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    #============================delete=============
    def delete_data(self):
      if self.var_EmployeeID.get()=="":
        messagebox.showerror("Error", "Supplier Id must be required", parent=self.root)
      else:
        try:
            delete=messagebox.askyesno("Supplier Delete Page", "Do you want to delete this Supplier", parent=self.root)
            if delete>0:
              conn=sqlite3.connect('SQL Database/IMS.db')
              my_cursor = conn.cursor()
              sql="DELETE FROM supplier WHERE EmployeeID=?"
              val=(self.var_EmployeeID.get(),)
              my_cursor.execute(sql,val)
            else:
              if not delete:
                return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Supplier details deleted", parent=self.root)
        except Exception as es:
          messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root) 
    
    def reset_data(self):
      self.var_EmployeeName.set("")
      self.var_EmployeeID.set("")
      
      self.var_Date.set("")
      self.var_Invoice.set("")
      self.var_Mobile.set("")
      self.var_Address.set("")
      self.var_searchby.set("")
      self.var_searchtext.set("")

    #======================================Generate Data====================
    def generate_dataset(self):
      if self.var_EmployeeName.get()=="" or self.var_EmployeeID.get()=="" or self.var_EmployeeName.get()=="Select Employee Name":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
      else:
        try: 
          conn=sqlite3.connect('SQL Database/IMS.db')
          my_cursor = conn.cursor()
          my_cursor.execute("SELECT * FROM supplier")
          myresult=my_cursor.fetchall()
          
          my_cursor.execute("UPDATE supplier SET EmployeeName=?,  Date=?, Invoice=?, Mobile=?,Address=? where EmployeeID=?", (
            self.var_EmployeeName.get(),
            self.var_EmployeeID.get(),
            self.var_Date.get(),
            self.var_Invoice.get(),
            self.var_Salery.get(),
            self.var_Mobile.get(),
            self.var_Address.get()
      
            ))
          messagebox.showinfo("Result", "Generating dataset completed")
        except Exception as es:
          messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root) 

          #===============Search===========#
    
    def search(self):
            con = sqlite3.connect(database=r'SQL Database/IMS.db')
            cur = con.cursor()
            try:
                if self.var_searchtext.get() == "":
                    messagebox.showerror("Error", "Search input should be required", parent=self.root)
                else:
                    
                    cur.execute("SELECT * FROM supplier WHERE Invoice=?", ( self.var_searchtext.get(),))
                    row = cur.fetchone()
                    
                    if row != None:
                        self.supplier_table.delete(*self.supplier_table.get_children())
                        self.supplier_table.insert('', 'end', values=row)
                    else:
                        messagebox.showerror("Error", "No Record found!!!", parent=self.root)
            
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    
    


#===================================show alll


    def show(self):
      con=sqlite3.connect(database=r'SQL Database/IMS.db')
      cur=con.cursor()
      try:
          cur.execute("select * from supplier")
          rows = cur.fetchall()
          self.supplier_table.delete(*self.supplier_table.get_children())
          for row in rows:
              self.supplier_table.insert('',END,values=row)
      except Exception as exs:
        messagebox.showerror("Error",f"Error due to : {str(exs)}",parent=self.root)   


if __name__ == "__main__":
    root=Tk()
    obj=sup(root)
    root.mainloop()
