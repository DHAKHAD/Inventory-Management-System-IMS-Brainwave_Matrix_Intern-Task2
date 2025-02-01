import sqlite3
from tkinter import BOTH, BOTTOM, END, HORIZONTAL, RIDGE, RIGHT, VERTICAL, W, X, Y, Button, Frame, Image, Label, LabelFrame, StringVar, Tk, messagebox, ttk
from PIL import Image, ImageTk

class cat:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x600+0+0")
        self.root.title("Inventory Management System")


        

        title_lbl=Label(self.root,text="Inventory Management System", font=("Times New Roman", 30, "bold"), bg="darkblue", fg="white")
        title_lbl.place(x=0, y=0, width=1520, height=50)


        self.var_ItemID=StringVar()
        self.var_ItemName=StringVar()
        self.var_searchby=StringVar()
        self.var_searchtext=StringVar() 


        main_frame=Frame(self.root, bd=2,bg="white")
        main_frame.place(x=10, y=55, width=1500, height=520)

        img=Image.open(r"Img/leftm.jpg")
        img=img.resize((750,250),Image.LANCZOS)
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(main_frame,image=self.photoimg)
        bg_img.place(x=0,y=270,width=750,height=250)


        title_lbl = Label(main_frame, text="Manage Product Category",anchor="center", font=("Times New Roman", 40, "bold"), bg="#87ceeb", fg="black")
        title_lbl.place(x=0, y=0, width=1500, height=70)


        Employee_Information_frame=LabelFrame(main_frame,bd=2,bg="white", relief=RIDGE, text="Employee Information", font=("Times New Roman",15, "bold"))
        Employee_Information_frame.place(x=0, y=80, width=750, height=190)

        user_label=Label(Employee_Information_frame, text="Item Name",bg="white", font=("Times New Roman",15, "bold"))
        user_label.grid(row=0, column=0, padx=10)
  
        pass_entry=ttk.Entry(Employee_Information_frame, textvariable=self.var_ItemName,width=17, font=("times new roman", 15, "bold"))
        pass_entry.grid(row=0, column=1, padx=2,pady=10, sticky=W)
         
        user_label=Label(Employee_Information_frame, text="Item ID",bg="white", font=("Times New Roman",15, "bold"))
        user_label.grid(row=0, column=2, padx=10)
  
        pass_entry=ttk.Entry(Employee_Information_frame, textvariable=self.var_ItemID,width=17, font=("times new roman", 15, "bold"))
        pass_entry.grid(row=0, column=3, padx=2,pady=10, sticky=W)


        btn_frame=Frame(Employee_Information_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=0, y=80, width=748, height=80)
  
        save_btn=Button(btn_frame,text="Save",command=self.add_data, width=31,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
  
        update_btn=Button(btn_frame,text="Update",command=self.update_data, width=31,font=("Times New Roman", 15, "bold"), bg="green", fg="white")
        update_btn.grid(row=0, column=1)
  
        Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data, width=31,font=("Times New Roman", 15, "bold"), bg="red", fg="white")
        Delete_btn.grid(row=1, column=0)
  
        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data ,width=31,font=("Times New Roman", 15, "bold"), bg="#009688", fg="white")
        Reset_btn.grid(row=1, column=1)

        Search_frame=LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("Times New Roman", 15, "bold"))
        Search_frame.place(x=750, y=80, width=730, height=110)

        search_combo=ttk.Combobox(Search_frame,textvariable=self.var_searchby, font=("Times New Roman",15, "bold"), width=12, state="readonly")
        search_combo["values"]=("Select","Item ID", "Item Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=1,padx=20, pady=10, sticky=W)

        SearchEntry=ttk.Entry(Search_frame,textvariable=self.var_searchtext, width=18, font=("Times New Roman",15, "bold"))
        SearchEntry.grid(row=0, column=2,padx=20, pady=10, sticky=W)

        search_btn=Button(Search_frame,text="Search",command=self.search, width=12,font=("Times New Roman", 12, "bold"), bg="green", fg="white")
        search_btn.grid(row=0, column=3, padx=15, pady=10)

        Showall_btn=Button(Search_frame,text="Show All",command=self.show, width=12,font=("Times New Roman", 12, "bold"), bg="blue", fg="white")
        Showall_btn.grid(row=0, column=4, padx=20, pady=10)

      #=============Table Frame==============
        Table_frame=Frame(main_frame, bd=2, bg="white", relief=RIDGE)
        Table_frame.place(x=750, y=190, width=730, height=330)

        scroll_x=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.category_table=ttk.Treeview(Table_frame,column=("ItemName","ItemID"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.category_table.xview)
        scroll_y.config(command=self.category_table.yview)

        
        self.category_table.heading("ItemName", text="Item Name")
        self.category_table.heading("ItemID", text="Item ID")
       

        self.category_table["show"]="headings"
        self.category_table.column("ItemName", width=100)

        self.category_table.pack(fill=BOTH, expand=1)
        self.category_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()

    # =================Function================
    def add_data(self):
      if self.var_ItemName.get()=="" or self.var_ItemID.get()=="" or self.var_ItemName.get()=="Select ItemName":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
      else:
        try: 
          conn=sqlite3.connect('SQL Database/IMS.db')
          my_cursor = conn.cursor()
          my_cursor.execute("INSERT INTO category VALUES(?,?)", (
            
            self.var_ItemName.get(),
            self.var_ItemID.get()
      
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
      my_cursor.execute("select * from category")
      data=my_cursor.fetchall()

      if len(data)!=0:
        self.category_table.delete(*self.category_table.get_children())
        for i in data:
          self.category_table.insert('',END, values=i)
      conn.commit()
      conn.close()

    #===================get cursor==============
    def get_cursor(self,event=""):
      cursor_focus=self.category_table.focus()
      content=self.category_table.item(cursor_focus)
      data=content["values"]
      
      self.var_ItemName.set(data[0])
      self.var_ItemID.set(data[1])
    
      
    #=======================update================
    
    def update_data(self):
        if self.var_ItemName.get() == "" or self.var_ItemID.get() == "" or self.var_ItemName.get() == "Select ItemName":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this Category details?", parent=self.root)
                if update:
                    conn = sqlite3.connect('SQL Database/IMS.db')
                    my_cursor = conn.cursor()
    
                    my_cursor.execute(
                        "UPDATE category SET ItemName=? WHERE ItemID=?",
                        (
                            self.var_ItemName.get(),
                            self.var_ItemID.get()  # Ensure EmployeeID is in the WHERE condition
                        )
                    )
    
                    conn.commit()
                    conn.close()
    
                    messagebox.showinfo("Success", "Category details updated", parent=self.root)
                    self.fetch_data()
    
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    #============================delete=============
    def delete_data(self):
      if self.var_ItemID.get()=="":
        messagebox.showerror("Error", "Category Id must be required", parent=self.root)
      else:
        try:
            delete=messagebox.askyesno("Category Delete Page", "Do you want to delete this Category", parent=self.root)
            if delete>0:
              conn=sqlite3.connect('SQL Database/IMS.db')
              my_cursor = conn.cursor()
              sql="DELETE FROM category WHERE ItemID=?"
              val=(self.var_ItemID.get(),)
              my_cursor.execute(sql,val)
            else:
              if not delete:
                return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Category details deleted", parent=self.root)
        except Exception as es:
          messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root) 
    
    def reset_data(self):
        self.var_ItemName.set("")
        self.var_ItemID.set("")
        
       
        self.var_searchby.set("")
        self.var_searchtext.set("")

    #======================================Generate Data====================
    def generate_dataset(self):
      if self.var_ItemName.get()=="" or self.var_ItemID.get()=="" or self.var_ItemName.get()=="Select  ItemName":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
      else:
        try: 
          conn=sqlite3.connect('SQL Database/IMS.db')
          my_cursor = conn.cursor()
          my_cursor.execute("SELECT * FROM category")
          myresult=my_cursor.fetchall()
          
          my_cursor.execute("UPDATE category SET ItemName=? where ItemID=?", (
            self.var_ItemName.get(),
            self.var_ItemID.get(),
            
      
            ))
          messagebox.showinfo("Result", "Generating dataset completed")
        except Exception as es:
          messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root) 



    def search(self):
            con = sqlite3.connect(database=r'SQL Database/IMS.db')
            cur = con.cursor()
            try:
                if self.var_searchtext.get() == "":
                    messagebox.showerror("Error", "Search input should be required", parent=self.root)
                else:
                    
                    cur.execute("SELECT * FROM category WHERE ItemID=?", ( self.var_searchtext.get(),))
                    row = cur.fetchone()
                    
                    if row != None:
                        self.category_table.delete(*self.category_table.get_children())
                        self.category_table.insert('', 'end', values=row)
                    else:
                        messagebox.showerror("Error", "No Record found!!!", parent=self.root)
            
            except Exception as ex:
                messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)
    

    def show(self):
        con=sqlite3.connect(database=r'SQL Database/IMS.db')
        cur=con.cursor()
        try:
            cur.execute("select * from category")
            rows = cur.fetchall()
            self.category_table.delete(*self.category_table.get_children())
            for row in rows:
                self.category_table.insert('',END,values=row)
        except Exception as exs:
          messagebox.showerror("Error",f"Error due to : {str(exs)}",parent=self.root)   


if __name__ == "__main__":
    root=Tk()
    obj=cat(root)
    root.mainloop()  