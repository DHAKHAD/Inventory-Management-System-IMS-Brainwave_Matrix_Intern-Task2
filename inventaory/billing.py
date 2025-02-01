import os
import sqlite3
import tempfile
import time
from tkinter import BOTH, BOTTOM, END, HORIZONTAL, LEFT, RIDGE, RIGHT, TOP, VERTICAL, X, Y, Entry, Frame, LabelFrame, Scrollbar, StringVar, Text, Tk, Label, Button, Toplevel, messagebox, ttk
from PIL import Image, ImageTk


class bills:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")

        
        self.var_Name=StringVar()
        self.var_ProductID=StringVar()
        self.var_contect=StringVar()
        self.var_pname=StringVar()
        self.var_Price=StringVar()
        self.var_Quantity=StringVar()
        self.var_stock=StringVar()
        self.var_clear=StringVar()
        self.var_calculate=StringVar()
        self.cart_list=[]
        self.print=0
        self.var_searchtext=StringVar()

        # ===== TITLE ===== #
        TopMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        TopMenu.place(x=0, y=0, width=1350, height=70)

        img = Image.open(r"img/logo.jpg")  # Load the logo image
        img = img.resize((130, 70), Image.LANCZOS)  # Resize to fit header
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(TopMenu, image=self.photoimg , bg="white")  # Create label with image
        bg_img.place(x=0, y=1, width=130, height=70)  # Place image at top-left corner
        

        title_lbl = Label(TopMenu, text="Inventory Management System",anchor="w", font=("Times New Roman", 40, "bold"), bg="#87ceeb", fg="black")
        title_lbl.place(x=130, y=1, width=1070, height=70)  # Title label next to logo

        # ===== LOGOUT BUTTON ===== #
        btn_logout = Button(TopMenu, text="Logout",command=self.logout, font=("times new roman", 20, "bold"), bg="#87ceeb", cursor="hand2")
        btn_logout.place(x=1200, y=0, height=70, width=150)  # Button on top-right corner
        

        self.clock_lbl = Label(self.root, text=f"Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time:HH:MM:SS", font=("times new roman", 20, "bold"), bg="#4d636d", fg="black")
        self.clock_lbl.place(x=0, y=70, relwidth=1, height=30)  
    
     #===================================================================================================================================#
     # FRAMES
        #Left_frame
        Left_frame=LabelFrame(self.root,bd=2,bg="white", relief=RIDGE, text="All Product Details", font=("Times New Roman",15, "bold"))
        Left_frame.place(x=1, y=100, width=400, height=570)
        title_lbl = Label(Left_frame,bd=3,bg="white", relief=RIDGE,)
        title_lbl.place(x=0, y=0, width=390, height=100)
        ibl_produt= Label(title_lbl,text="Product Name",font=("Times New Roman",15,"bold"),bg="white" )
        ibl_produt.place(x=5,y=15)
        tex_product=Entry(title_lbl,textvariable=self.var_searchtext,font=("times new roman",15),bg="light yellow")
        tex_product.place(x=170,y=15,width=180,height=30)  
        search_btn=Button(title_lbl,text="Search", command=self.search ,width=12,font=("Times New Roman", 12, "bold"), bg="green", fg="white")
        search_btn.place(x=10,y=60,width=120,height=28)
        Showall_btn=Button(title_lbl,text="Show All",command=self.show, width=12,font=("Times New Roman", 12, "bold"), bg="blue", fg="white")
        Showall_btn.place(x=170,y=60,width=120,height=28)
        Prod_frame=Frame(Left_frame, bd=2, bg="white", relief=RIDGE)
        Prod_frame.place(x=0, y=100, width=390, height=420)
        scroll_x=ttk.Scrollbar(Prod_frame, orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(Prod_frame, orient=VERTICAL)
        self.product_table=ttk.Treeview(Prod_frame,column=("Name", "ProductID", "Price","Quantity","Status"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.product_table.xview)
        scroll_y.config(command=self.product_table.yview)
        self.product_table.heading("ProductID", text="Product ID")
        self.product_table.heading("Name", text=" Name")
        self.product_table.heading("Price", text="Price")
        self.product_table.heading("Quantity", text="Quantity") 
        self.product_table.heading("Status", text="Status")
        self.product_table["show"]="headings"
        self.product_table.column("ProductID", width=50)
        self.product_table.column("Name", width=50)
        self.product_table.column("Price", width=50)
        self.product_table.column("Quantity", width=50)
        self.product_table.column("Status", width=50)
        self.product_table.pack(fill=BOTH, expand=1)
        self.product_table.bind("<ButtonRelease>",self.get_cursor)
       
        pd_footer = Label(Left_frame, text="Note: 'Enter 0 Quantity to remove product from the Cart'",anchor="center", font=("Times New Roman", 10, "bold"), bg="red", fg="black")
        pd_footer.pack(side=BOTTOM,fill=X)   
        title_footer = Label(self.root, text="IMS-Inventory Management System\n developed by Sunil Nagar",anchor="center", font=("Times New Roman", 10, "bold"), bg="#87ceeb", fg="black")
        title_footer.place(x=0, y=670, width=1350, height=30)

         
        self.show()
        self.update_time()


#=================================================================================================#
    def search(self):
        con = sqlite3.connect(database=r'SQL Database/IMS.db')
        cur = con.cursor()
        try:
            if self.var_searchtext.get() == "":
                messagebox.showerror("Error", "Search input should be required", parent=self.root)
            else:
                query = f"SELECT Name,ProductID,Price,Quantity,Status FROM product WHERE Name LIKE ?"
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
            cur.execute("select Name,ProductID,Price,Quantity,Status from product")
            rows = cur.fetchall()
            self.product_table.delete(*self.product_table.get_children())
            for row in rows:
                self.product_table.insert('',END,values=row)
        except Exception as exs:
          messagebox.showerror("Error",f"Error due to : {str(exs)}",parent=self.root)

    #===========     #Right Frame====================================================#
        Right_frame=LabelFrame(self.root,bd=2,bg="white", relief=RIDGE, text="Customer Bill Area", font=("Times New Roman",15, "bold"))
        Right_frame.place(x=810, y=100, width=540, height=570)
        Right1_frame = Frame(Right_frame, bd=2, bg="white", relief=RIDGE)
        Right1_frame.place(x=0, y=10, width=530, height=420)

        scroll_y=Scrollbar(Right1_frame, orient=VERTICAL)
        scroll_y.pack(side=RIGHT, fill=Y)
        self.txt_bill_area=Text(Right1_frame, yscrollcommand=scroll_y.set)
        self.txt_bill_area.pack(fill=BOTH,expand=1)
        scroll_y.config(command=self.txt_bill_area.yview)


        self.bill_amnt=Label(Right_frame,text="Bill Amount ", width=40,font=("Times New Roman", 15, "bold"), bg="red", fg="white")
        self.bill_amnt.place(x=0,y=430,width=120,height=50)
        self.diss_btn=Label(Right_frame,text="Discount \n 5%", width=40,font=("Times New Roman", 15, "bold"), bg="blue", fg="white")
        self.diss_btn.place(x=120,y=430,width=130,height=50)
        self.net_amnt = Label(Right_frame, text="Net Pay", font=("Times New Roman", 15, "bold"), bg="gray", fg="white")
        self.net_amnt.place(x=250, y=430, width=120, height=50)
        self.clear_all=Button(Right_frame,text="Clear All",command=self.Clear_All, width=30,font=("Times New Roman", 17, "bold"), bg="skyblue", fg="white")
        self.clear_all.place(x=370,y=430,width=160,height=50)
        self.print=Button(Right_frame,text="Print Bill ",command=self.print_bill, width=40,font=("Times New Roman", 17, "bold"), bg="green", fg="white")
        self.print.place(x=0,y=480,width=269,height=65)
        self.save_btn=Button(Right_frame,text="Generate & Save \nBill",command=self.generate_bill, width=40,font=("Times New Roman", 17, "bold"), bg="lime", fg="white")
        self.save_btn.place(x=270,y=480,width=260,height=65)


 #=================================       #centert Frame=================================#
        center_frame=LabelFrame(self.root,bd=2,bg="white", relief=RIDGE, text="Customer Details", font=("Times New Roman",15, "bold"))
        center_frame.place(x=405, y=100, width=400, height=570)
        cust_frame = Label(center_frame,bd=3,bg="white", relief=RIDGE,)
        cust_frame.place(x=0, y=0, width=390, height=100)
        ibl_produt= Label(cust_frame,text="Name",font=("Times New Roman",15,"bold"),bg="white" )
        ibl_produt.place(x=5,y=15)
        tex_product=Entry(cust_frame,textvariable=self.var_pname,font=("times new roman",15),bg="light yellow")
        tex_product.place(x=170,y=15,width=180,height=30)
        ibl_produt= Label(cust_frame,text="Contect No.",font=("Times New Roman",15,"bold"),bg="white" )
        ibl_produt.place(x=5,y=60)
        tex_product=Entry(cust_frame,textvariable=self.var_contect,font=("times new roman",15),bg="light yellow")
        tex_product.place(x=170,y=60,width=180,height=30)

     
        Cust_frame=LabelFrame(center_frame,text="Total Add Product", font=("Times New Roman",15, "bold"), bd=2, bg="white", relief=RIDGE)
        Cust_frame.place(x=200, y=100, width=190, height=320)
  
        scroll_x=Scrollbar(Cust_frame, orient=HORIZONTAL)
        scroll_y=Scrollbar(Cust_frame, orient=VERTICAL)
        self.cart_table=ttk.Treeview(Cust_frame,column=("Name", "ProductID", "Price","Quantity"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.cart_table.xview)
        scroll_y.config(command=self.cart_table.yview)
        
        self.cart_table.heading("Name", text=" Name")
        self.cart_table.heading("ProductID", text="Product ID")   
        self.cart_table.heading("Price", text="Price")
        self.cart_table.heading("Quantity", text="Quantity")    
        self.cart_table["show"]="headings"
        self.cart_table.column("Name", width=90)
        self.cart_table.column("ProductID", width=70)
        self.cart_table.column("Price", width=80)
        self.cart_table.column("Quantity", width=60) 
        self.cart_table.pack(fill=BOTH, expand=1)
        self.cart_table.bind("<ButtonRelease>",self.get_data_cart)

        ibl_p=Label(center_frame,text="Product Name",font=("Times New Roman",15,"bold"),bg="white" )
        ibl_p.place(x=5,y=420)
        tex_p=Entry(center_frame,textvariable=self.var_Name,font=("times new roman",15),bg="light yellow")
        tex_p.place(x=5,y=450,width=150,height=30)

        ibl_qut=Label(center_frame,text="Quantity",font=("Times New Roman",15,"bold"),bg="white" )
        ibl_qut.place(x=170,y=420)
        tex_qut=Entry(center_frame,textvariable=self.var_Quantity,font=("times new roman",15),bg="light yellow")
        tex_qut.place(x=170,y=450,width=70,height=30)

        ibl_pri=Label(center_frame,text="Price Per Qty",font=("Times New Roman",15,"bold"),bg="white" )
        ibl_pri.place(x=260,y=420)
        tex_pri=Entry(center_frame,textvariable=self.var_Price,font=("times new roman",15),bg="light yellow")
        tex_pri.place(x=260,y=450,width=130,height=30)

        self.ibl_st= Label(center_frame,text="In Stock  ",font=("Times New Roman",15,"bold"),bg="white" )
        self.ibl_st.place(x=5,y=500)
        
        clear_btn=Button(center_frame,text="Clear",command=self.clear_cart, width=20,font=("Times New Roman", 20, "bold"), bg="green", fg="white")
        clear_btn.place(x=140,y=500,width=120,height=40)
        add_btn=Button(center_frame,text="Add Cart",command=self.add_update_cart, width=20,font=("Times New Roman", 20, "bold"), bg="blue", fg="white")
        add_btn.place(x=260,y=500,width=130,height=40)

       
        
         # Frame for calculator
        self.Cal_frame = LabelFrame(center_frame,text="Calculator", font=("Times New Roman",15, "bold"), bd=2, bg="white", relief=RIDGE)
        self.Cal_frame.place(x=0, y=100, width=200, height=320)

        # Display entry
        self.cal_tex = Entry(self.Cal_frame, font=("Times New Roman", 15), bg="light yellow", bd=4)
        self.cal_tex.grid(row=0, column=0, columnspan=4, pady=0, padx=0, ipady=15)

        # Button layout
        buttons = [
            ('7', '8', '9'),
            ('4', '5', '6'),
            ('1', '2', '3'),
            ('-', '0', '+'),
            ('/', '*', '='),
            ( ',','C', '.' )
            
        ]

        for i, row in enumerate(buttons):
            for j, char in enumerate(row):
                if char == "C":
                    btn = Button(self.Cal_frame, text=char, width=6, font=("Times New Roman", 10, "bold"), 
                                 bg="red", fg="white", command=self.clear)
                elif char == "=":
                    btn = Button(self.Cal_frame, text=char, width=6, font=("Times New Roman", 10, "bold"), 
                                 bg="blue", fg="white", command=self.calculate)
                else:
                    btn = Button(self.Cal_frame, text=char, width=6, font=("Times New Roman", 10, "bold"), 
                                 bg="green", fg="white", command=lambda ch=char: self.on_button_click(ch))
                btn.grid(row=i+1, column=j, padx=5, pady=5)

    # Function to handle button click
    def on_button_click(self, value):
        current_text = self.cal_tex.get()
        self.cal_tex.delete(0, END)
        self.cal_tex.insert(END, current_text + str(value))

    # Function to clear the entry field
    def clear(self):
        self.cal_tex.delete(0, END)

    # Function to evaluate the expression
    def calculate(self):
        try:
            result = eval(self.cal_tex.get())
            self.cal_tex.delete(0, END)
            self.cal_tex.insert(END, result)
        except:
            self.cal_tex.delete(0, END)
            self.cal_tex.insert(END, "Error")
    
        
 #========================================================================================================================================#
   
    def get_cursor(self, event=""):
        f= self.product_table.focus()  # Get selected row
        content=(self.product_table.item(f))
        row=content['values']
        # Assign values safely
        self.var_Name.set(row[0])
        self.var_ProductID.set(row[1])
        self.var_Price.set(row[2])
        self.ibl_st.config( text=f"In Stock [{str(row[3])}] ")
        self.var_stock.set(row[3])
        self.var_Quantity.set('1')


    def get_data_cart(self, event=""):
        f= self.cart_table.focus()  # Get selected row
        content=(self.cart_table.item(f))
        row=content['values']
        # Assign values safely
        self.var_Name.set(row[0])
        self.var_ProductID.set(row[1])
        self.var_Price.set(row[2])
        self.var_Quantity.set(row[3])
        self.ibl_st.config( text=f"In Stock [{str(row[4])}] ")
        self.var_stock.set(row[4])
            
#=====================================================================================================#
    def add_update_cart(self):
        if self.var_ProductID.get() == '':
            messagebox.showerror("Error", "Please select a Product", parent=self.root)
            return  # Exit function if no product is selected
    
        if self.var_Quantity.get() == '':
            messagebox.showerror("Error", "Quantity is Required", parent=self.root)
            return  # Exit function if no quantity is entered

        elif int(self.var_Quantity.get())>int(self.var_stock.get()) :
            messagebox.showerror("Error", "Invalid Quantity ", parent=self.root)
            return  # Exit function if no quantity is entered
        
    
        try:
            quantity = int(self.var_Quantity.get())  # Ensure it's an integer
            price_cal = float(self.var_Price.get())
              # Calculate total price
        except ValueError:
            messagebox.showerror("Error", "Invalid Quantity or Price", parent=self.root)
            return  # Exit if input is invalid
    
        cart_data = [self.var_Name.get(), self.var_ProductID.get(), price_cal, quantity ,self.var_stock.get()]
    
        # Check if product is already in cart
        present = False
        index_ = -1  # Default value if not found
    
        for i, row in enumerate(self.cart_list):
            if self.var_ProductID.get() == row[1]:  # Compare ProductID, not row[0]
                present = True
                index_ = i
                break
    
        if present:
            # Ask user whether to update or remove
            op = messagebox.askyesno(
                'Confirm', 
                "Product already present\nDo you want to Update or Remove from the Cart list?",
                parent=self.root
            )
            if op:  # If user clicks Yes
                if quantity == 0:  
                    self.cart_list.pop(index_)  # Remove product from cart if quantity is 0
                else:
                    self.cart_list[index_][2] = price_cal  # Update price
                    self.cart_list[index_][3] = quantity  # Update quantity
        else:
            self.cart_list.append(cart_data)  # Add new item if not in cart
    
        self.show_cart()  # Refresh cart display
        self.bill_update()

    def show_cart(self):
        try:
            self.cart_table.delete(*self.cart_table.get_children())
            for row in self.cart_list:
                self.cart_table.insert('',END,values=row)
        except Exception as exs:
            messagebox.showerror("Error",f"Error due to : {str(exs)}",parent=self.root) 
       
#================================================

    def bill_update(self):
        self.bill_amt=0
        self.net_pay=0
        self.discount=0
        for row in self.cart_list:
            self.bill_amt=self.bill_amt+(float(row[2])*int(row[3]))
        self.discount=(self.bill_amt*5)/100
        self.net_pay=self.bill_amt-self.discount   
        self.bill_amnt.config(text=f"Bill Amount\n{str(self.bill_amt)}")
        self.net_amnt.config(text=f"Net Pay\n{str(self.net_pay)}")
        #self.cart_table.config(text=f"Cart \t Total Product:[{str(len(self.cart_list))}]")

#####====================================================================================================================##

    def generate_bill(self):
        if self.var_pname.get()=='' or self.var_contect.get()=='':
            messagebox.showerror("Error",f"Customer Details are required",parent=self.root)
        elif len (self.cart_list)==0:
            messagebox.showerror("Error",f"Please Add Product to the Cart!!!",parent=self.root)

        else:
            #======Top bill=====#
            self.Bill_Top()
            self.Bill_mid()
            self.Bill_Bottom()
            fp=open(f'bill/{str(self.invoice)}.txt','w')
            fp.write(self.txt_bill_area.get('1.0',END))
            fp.close()
            messagebox.showerror("Saved","Bill has been  generated !!!",parent=self.root)
            self.print=1

    def Bill_Top(self):
        self.invoice=int(time.strftime("%H%M%S"))+int(time.strftime("%d%m%Y"))
        Bill_Top_temp=f'''
\t\tXYZ-Invatory-Bill
\t Phome No. 97979*****  , Kota-325201
{str("="*60)}
Customer Name :{self.var_pname.get()}
Ph No.: {self.var_contect.get()}
Bill No. : {str(self.invoice)}\t\t\tDate: {str(time.strftime("%d/%m/%Y"))}
{str("="*60)}
Product Name:\t\t\tQuantity\t\tPrice
{str("="*60)}
        '''    
        self.txt_bill_area.delete('1.0',END)
        self.txt_bill_area.insert('1.0',Bill_Top_temp)



    def Bill_Bottom(self):
        Bill_Bottom_temp=f''' 
Bill Amount\t\t\t\t\tRs.{self.bill_amt}
Discoubt\t\t\t\t\tRs.{self.discount}
Net Pay\t\t\t\t\tRs.{self.net_pay}
{str("="*60)}\n       

        '''    
        self.txt_bill_area.insert(END,Bill_Bottom_temp)



    def Bill_mid(self):
        conn=sqlite3.connect('SQL Database/IMS.db')
        can = conn.cursor()
        try:
            for row in self.cart_list:
                Name=row[0]
                ProductID=row[1]
                Price=float(row[2])*int(row[3]) 
                Quantity = int(row[4]) - int(row[3])  # Subtract purchased quantity from stock
            
            # Ensure Status is assigned correctly
                Status = 'Active'  # Default status
                if Quantity == 0:
                    Status = 'InActive'    
                self.txt_bill_area.insert(END, f"\n{Name}\t\t\t{row[3]}\t\tRs. {Price:.2f}")
                can.execute('Update product set Quantity=?,Status=? WHERE ProductID=?',(
                    Quantity,
                    Status,
                    ProductID
                    
                ))
                conn.commit()
            conn.close()    
        except Exception as ex:
             messagebox.showerror("Error", f"Due to :{str(ex)}", parent=self.root)



    def clear_cart(self):

        self.var_Name.set('')
        self.var_ProductID.set('')
        self.var_Price.set('')
        self.var_Quantity.set('')
        self.ibl_st.config( text=f"In Stock [{str('')}] ")
        self.var_stock.set('')


    def Clear_All(self):
            del self.cart_list[:]
            self.var_pname.set('')
            self.var_searchtext.set('')
            self.var_contect.set('')
            self.txt_bill_area.delete('1.0',END)
            self.clear_cart()
            self.show()
            self.show_cart()
    def update_time(self):
        current_time = time.strftime("%I:%M:%S") 
        current_date = time.strftime("%d-%m-%Y")  
        self.clock_lbl.config(text=f"Welcome to Inventory Management System\t\t Date: {current_date}\t\t Time: {current_time}")
        self.clock_lbl.after(200, self.update_time)
    
    def print_bill(self):
        if self.print==1:
            messagebox.showerror("Print", " please wait while printing", parent=self.root)
            new_file=tempfile.mktemp(' .txt')
            open(new_file,'w').write(self.txt_bill_area.get('1.0',END))
            os.startfile(new_file,'print')
        else:
            messagebox.showerror("Error", "Please generate bill , To print the receipt", parent=self.root)
        
    def logout(self):
        self.root.destroy()
        os.system("python login.py")

if __name__ == "__main__":
    root = Tk()
    obj = bills(root)  # Create object of IMS class
    root.mainloop()
