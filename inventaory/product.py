import sqlite3
from tkinter import BOTH, BOTTOM, END, HORIZONTAL, RIDGE, RIGHT, VERTICAL, W, X, Y, Button, Frame, Label, LabelFrame, StringVar, Tk, messagebox, ttk
from PIL import Image, ImageTk

class prod:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1305x790+0+0")
        self.root.title("Inventory Management System")



        self.var_Name=StringVar()
        self.var_ProductID=StringVar()
        self.var_Category=StringVar()
        self.var_Supplier=StringVar()
        self.var_Price=StringVar()
        self.var_Quantity=StringVar()
        self.var_Status=StringVar()
        self.var_searchby=StringVar()
        self.var_searchtext=StringVar() 
        self.Category_list=[]
        self.Supplier_list=[]
        self.fetch_data()
        


        title_lbl = Label(self.root, text="Manage Products",anchor="center", font=("Times New Roman", 40, "bold"), bg="#87ceeb", fg="black")
        title_lbl.place(x=0, y=0, width=1305, height=70)
        #==Left frame==#
        Left_frame=LabelFrame(self.root,bd=2,bg="white", relief=RIDGE, text="Employee Details", font=("Times New Roman",15, "bold"))
        Left_frame.place(x=1, y=71, width=500, height=680)
  
        #Center Frame
        Center_frame=LabelFrame(self.root,bd=2,bg="white", relief=RIDGE, text="Employee Details", font=("Times New Roman",15, "bold"))
        Center_frame.place(x=501, y=71, width=400, height=680)
        #==Right frame
        #Right_frame=LabelFrame(self.root,bd=2,bg="white", relief=RIDGE, text="Employee Details", font=("Times New Roman",15, "bold"))
        #Right_frame.place(x=902, y=71, width=400, height=680)
        title_footer = Label(self.root, text="IMS-Inventory Management System\n developed by Sunil Nagar",anchor="center", font=("Times New Roman", 10, "bold"), bg="#87ceeb", fg="black")
        title_footer.place(x=0, y=755, width=1305, height=30)

        img = Image.open(r"img/logo.jpg")  # Load the logo image
        img = img.resize((400, 680), Image.LANCZOS)  # Resize to fit header
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photoimg , bg="white")  # Create label with image
        bg_img.place(x=902, y=71, width=400, height=680)

        
        
        cate_label=Label(Left_frame, text="Category",bg="white", font=("Times New Roman",20, "bold"))
        cate_label.grid(row=0, column=0, padx=10,pady=20)

        cate_combo=ttk.Combobox(Left_frame,textvariable=self.var_Category, font=("Times New Roman",20, "bold"), width=20, state="readonly")
        cate_combo["values"]=self.Category_list
        cate_combo.current(0)
        cate_combo.grid(row=0, column=1,padx=2, pady=20, sticky=W)
        

        Supplier_label=Label(Left_frame, text="Supplier",bg="white", font=("Times New Roman",20, "bold"))
        Supplier_label.grid(row=1, column=0, padx=10)
        Supplier_combo=ttk.Combobox(Left_frame,textvariable=self.var_Supplier, font=("Times New Roman",20, "bold"), width=20, state="readonly")
        Supplier_combo["values"]=self.Supplier_list
        Supplier_combo.current(0)
        Supplier_combo.grid(row=1, column=1,padx=2, pady=10, sticky=W)





        Name_label=Label(Left_frame, text="Product Name",bg="white", font=("Times New Roman",20, "bold"))
        Name_label.grid(row=2, column=0, padx=10)
  
        pass_entry=ttk.Entry(Left_frame, textvariable=self.var_Name,width=21, font=("times new roman", 20, "bold"))
        pass_entry.grid(row=2, column=1, padx=2,pady=10, sticky=W)

        PID_label=Label(Left_frame, text="Product ID",bg="white", font=("Times New Roman",20, "bold"))
        PID_label.grid(row=3, column=0, padx=10)
  
        pass_entry=ttk.Entry(Left_frame, textvariable=self.var_ProductID,width=21, font=("times new roman", 20, "bold"))
        pass_entry.grid(row=3, column=1, padx=2,pady=10, sticky=W)

        Price_label=Label(Left_frame, text="Price",bg="white", font=("Times New Roman",20, "bold"))
        Price_label.grid(row=4, column=0, padx=10)
  
        pass_entry=ttk.Entry(Left_frame, textvariable=self.var_Price,width=21, font=("times new roman", 20, "bold"))
        pass_entry.grid(row=4, column=1, padx=2,pady=10, sticky=W)
        

        Quantity_label=Label(Left_frame, text="Quantity",bg="white", font=("Times New Roman",20, "bold"))
        Quantity_label.grid(row=5, column=0, padx=10)
  
        pass_entry=ttk.Entry(Left_frame, textvariable=self.var_Quantity,width=21, font=("times new roman", 20, "bold"))
        pass_entry.grid(row=5, column=1, padx=2,pady=10, sticky=W)


        Status_label=Label(Left_frame, text="Status",bg="white", font=("Times New Roman",20, "bold"))
        Status_label.grid(row=6, column=0, padx=10)
        Status_combo=ttk.Combobox(Left_frame,textvariable=self.var_Status, font=("Times New Roman",20, "bold"), width=20, state="readonly")
        Status_combo["values"]=("Select","Active", "InActive")
        Status_combo.current(0)
        Status_combo.grid(row=6, column=1,padx=2, pady=10, sticky=W)
        



        btn_frame=Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=500, width=490, height=80)
  
        save_btn=Button(btn_frame,text="Save",command=self.add_data, width=20,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
        save_btn.grid(row=0, column=0)
  
        update_btn=Button(btn_frame,text="Update",command=self.update_data, width=20,font=("Times New Roman", 15, "bold"), bg="green", fg="white")
        update_btn.grid(row=0, column=1)
  
        Delete_btn=Button(btn_frame,text="Delete",command=self.delete_data, width=20,font=("Times New Roman", 15, "bold"), bg="red", fg="white")
        Delete_btn.grid(row=1, column=0)
  
        Reset_btn=Button(btn_frame,text="Reset",command=self.reset_data ,width=20,font=("Times New Roman", 15, "bold"), bg="#009688", fg="white")
        Reset_btn.grid(row=1, column=1)
        











        Search_frame=LabelFrame(Center_frame, bd=2, bg="white", relief=RIDGE, text="Search System", font=("Times New Roman", 15, "bold"))
        Search_frame.place(x=10, y=1, width=380, height=150)
  
        search_combo=ttk.Combobox(Search_frame,textvariable=self.var_searchby, font=("Times New Roman",15, "bold"), width=12, state="readonly")
        search_combo["values"]=("Select","Category", "Supplier","Name")
        search_combo.current(0)
        search_combo.grid(row=0, column=0,padx=15, pady=10, sticky=W)
  
        SearchEntry=ttk.Entry(Search_frame,textvariable=self.var_searchtext, width=18, font=("Times New Roman",15, "bold"))
        SearchEntry.grid(row=0, column=1,padx=10, pady=1, sticky=W)
  
        search_btn=Button(Search_frame,text="Search",command=self.search, width=12,font=("Times New Roman", 12, "bold"), bg="green", fg="white")
        search_btn.grid(row=1, column=0, padx=20, pady=15)
  
        Showall_btn=Button(Search_frame,text="Show All",command=self.show, width=12,font=("Times New Roman", 12, "bold"), bg="blue", fg="white")
        Showall_btn.grid(row=1, column=1, padx=10, pady=15)
    






        Table_frame=Frame(Center_frame, bd=2, bg="white", relief=RIDGE)
        Table_frame.place(x=10, y=160, width=380, height=490)

        scroll_x=ttk.Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Table_frame, orient=VERTICAL)

        self.product_table=ttk.Treeview(Table_frame,column=("Name", "ProductID",  "Category", "Supplier", "Price","Quantity","Status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.product_table.xview)
        scroll_y.config(command=self.product_table.yview)

        self.product_table.heading("Name", text="Product Name")
        self.product_table.heading("ProductID", text="Product ID")
        self.product_table.heading("Category", text="Category")
        self.product_table.heading("Supplier", text="Supplier")
        self.product_table.heading("Price", text="Price")
        self.product_table.heading("Quantity",text="Quantity")
        self.product_table.heading("Status", text="Status")

        self.product_table["show"]="headings"
        self.product_table.column("Name", width=100)

        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease>",self.get_cursor)
        self.fetch_data()
        self.show()


#========================================================================================================================================#####
    def add_data(self):
      if self.var_Category.get()=="Select" or self.var_Category.get()=="Empty" or self.var_Supplier.get()=="" or self.var_Name.get()=="Select Name":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
      else:
        try: 
          conn=sqlite3.connect('SQL Database/IMS.db')
          my_cursor = conn.cursor()
          my_cursor.execute("INSERT INTO product VALUES(?,?,?,?,?,?,?)", (
            self.var_Name.get(),
            self.var_ProductID.get(),
            self.var_Category.get(),
            self.var_Supplier.get(),
            self.var_Price.get(),
            self.var_Quantity.get(),
            self.var_Status.get()
      
            ))

          conn.commit()
          self.fetch_data()
          conn.close()
          messagebox.showinfo("Success", "Added Succesfully", parent=self.root)
        except Exception as es:
          messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)

    # ==============Fetch Data========================
    def fetch_data(self):
        self.Category_list.append("Empty")
        self.Supplier_list.append("Empty")
        conn=sqlite3.connect('SQL Database/IMS.db')
        cur = conn.cursor()
        try:
            cur.execute("select ItemName  from category")
            cat=cur.fetchall()
            if len(cat)>0:
               del self.Category_list[:]
               self.Category_list.append("Select")
               for i in cat:
                  self.Category_list.append(i[0])
                     
               

            cur.execute("select EmployeeName  from supplier")
            sup=cur.fetchall()
            if len(sup)>0:
               del self.Supplier_list[:]
               self.Supplier_list.append("Select")
               for i in sup:
                  self.Supplier_list.append(i[0])
            

        except Exception as Exe:
           messagebox.showerror("Erro",f"Erro due to : {str(Exe)}",parent=self.root)

    #===================get cursor==============
    def get_cursor(self, event=""):
        cursor_focus = self.product_table.focus()  # Get selected row
        if not cursor_focus:  # Check if a row is selected
            messagebox.showerror("Error", "No product selected!", parent=self.root)
            return
    
        content = self.product_table.item(cursor_focus)
        data = content.get("values", [])  # Get row data safely
    
        print("Debug: data =", data)  # Print data for debugging
    
        if not data:  # If no data is available
            messagebox.showerror("Error", "Selected row has no data!", parent=self.root)
            return
    
        if len(data) < 7:  # Ensure at least 7 elements exist
            messagebox.showerror("Error", f"Data is incomplete! Expected 7 values, got {len(data)}", parent=self.root)
            return
    
        # Assign values safely
        self.var_Name.set(data[0])
        self.var_ProductID.set(data[1])
        self.var_Category.set(data[2])
        self.var_Supplier.set(data[3])
        self.var_Price.set(data[4])
        self.var_Quantity.set(data[5])
        self.var_Status.set(data[6])

    
      
    #=======================update================
    
    def update_data(self):
        if self.var_Name.get() == "" or self.var_ProductID.get() == "" or self.var_Name.get() == "Select Name":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                update = messagebox.askyesno("Update", "Do you want to update this Product details?", parent=self.root)
                if update:
                    conn = sqlite3.connect('SQL Database/IMS.db')
                    my_cursor = conn.cursor()
    
                    my_cursor.execute(
                        "UPDATE product SET Name=?, Category=?, Supplier=?, Price=?,Quantity=?,Status=? WHERE ProductID=?",
                        (
                            self.var_Name.get(),
                            self.var_Category.get(),
                            self.var_Supplier.get(),
                            self.var_Price.get(),
                            self.var_Quantity.get(),
                            self.var_Status.get(),
                            self.var_ProductID.get()  # Ensure ProductID is in the WHERE condition
                        )
                    )
    
                    conn.commit()
                    conn.close()
    
                    messagebox.showinfo("Success", "Product details updated", parent=self.root)
                    self.fetch_data()
    
            except Exception as es:
                messagebox.showerror("Error", f"Due to: {str(es)}", parent=self.root)


    #============================delete=============
    def delete_data(self):
      if self.var_ProductID.get()=="":
        messagebox.showerror("Error", "Product Id must be required", parent=self.root)
      else:
        try:
            delete=messagebox.askyesno("Product Delete Page", "Do you want to delete this Product", parent=self.root)
            if delete>0:
              conn=sqlite3.connect('SQL Database/IMS.db')
              my_cursor = conn.cursor()
              sql="DELETE FROM product WHERE ProductID=?"
              val=(self.var_ProductID.get(),)
              my_cursor.execute(sql,val)
            else:
              if not delete:
                return
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Product details deleted", parent=self.root)
        except Exception as es:
          messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root) 
    
    def reset_data(self):
      self.var_Name.set("")
      self.var_ProductID.set("")
      self.var_Category.set("")
      self.var_Supplier.set("")
      self.var_Price.set("")
      self.var_Quantity.set("")
      self.var_Status.set("")
      self.var_searchby.set("")
      self.var_searchtext.set("")

    #======================================Generate Data====================
    def generate_dataset(self):
      if self.var_Name.get()=="" or self.var_ProductID.get()=="" or self.var_Name.get()=="Select Employee Name":
        messagebox.showerror("Error", "All fields are required", parent=self.root)
      else:
        try: 
          conn=sqlite3.connect('SQL Database/IMS.db')
          my_cursor = conn.cursor()
          my_cursor.execute("SELECT * FROM product")
          myresult=my_cursor.fetchall()
          
          my_cursor.execute("UPDATE product SET Name=?,  Category=?, Supplier=?, Price=?,Quantity=?,Status=? where ProductID=?", (
            self.var_Name.get(),
            self.var_ProductID.get(),
            self.var_Category.get(),
            self.var_Supplier.get(),
            self.var_Price.get(),
            self.var_Quantity.get(),
            self.var_Status.get(),
      
            ))
          messagebox.showinfo("Result", "Generating dataset completed")
        except Exception as es:
          messagebox.showerror("Error",f"Due to:{str(es)}", parent=self.root) 



    def search(self):
        con = sqlite3.connect(database=r'SQL Database/IMS.db')
        cur = con.cursor()
        try:
            if self.var_searchby.get() == "Select":
                messagebox.showerror("Error", "Search By Option", parent=self.root)
            elif self.var_searchtext.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                query = f"SELECT * FROM product WHERE {self.var_searchby.get()} LIKE ?"
                cur.execute(query, ('%' + self.var_searchtext.get() + '%',))
                rows = cur.fetchall()
                
                if len(rows) != 0:
                    self.product_table.delete(*self.product_table.get_children())
                    for row in rows:
                        self.product_table.insert('', 'end', values=row)
                else:
                    messagebox.showerror("Error", "No Record found!!!", parent=self.root)
        
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to: {str(ex)}", parent=self.root)

    
    


#===================================show alll


    def show(self):
      con=sqlite3.connect(database=r'SQL Database/IMS.db')
      cur=con.cursor()
      try:
          cur.execute("select * from product")
          rows = cur.fetchall()
          self.product_table.delete(*self.product_table.get_children())
          for row in rows:
              self.product_table.insert('',END,values=row)
      except Exception as exs:
        messagebox.showerror("Error",f"Error due to : {str(exs)}",parent=self.root)   






if __name__ == "__main__":
    root=Tk()
    obj=prod(root)
    root.mainloop() 