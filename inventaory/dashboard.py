import os
import sqlite3
import time
from tkinter import LEFT, RIDGE, TOP, X, Frame, Tk, Label, Button, Toplevel, messagebox
from PIL import Image, ImageTk

from Supplier import sup
from billing import bills
from category import cat
from employee import Emp
from product import prod
from sales import sal

class IMS:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1350x700+0+0")
        self.root.title("Inventory Management System")
        self.update_time()

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





        self.clock_lbl = Label(self.root, font=("times new roman", 20, "bold"), bg="#4d636d", fg="black")
        self.clock_lbl.place(x=0, y=70, relwidth=1, height=30)  # Position the clock on top-right

        # Call the function to update time every second

   
        # ===== LEFT MENU FRAME ===== #
        leftMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        leftMenu.place(x=0, y=100, width=250, height=550) 
         # Position of left menu
        rightMenu = Frame(self.root, bd=2, relief=RIDGE, bg="white")
        rightMenu.place(x=251, y=100, width=1097, height=550)



        selfimg3 =Image.open(r"C:\Users\sunil\OneDrive\Desktop\inventaory\img\imagesbg.jpeg")  # Load image for left menu
        selfimg3 =selfimg3.resize((1096, 545), Image.LANCZOS)  # Resize image for appropriate display size
        self.photoselfimg3 = ImageTk.PhotoImage(selfimg3) 
         # Convert image to PhotoImage object
        bg_img1 =Label(rightMenu, image=self.photoselfimg3)  # Label with image
        bg_img1.pack(side=TOP,fill=X)

        selfimg =Image.open(r"img/leftm.jpg")  # Load image for left menu
        selfimg =selfimg.resize((250, 150), Image.LANCZOS)  # Resize image for appropriate display size
        self.photoselfimg = ImageTk.PhotoImage(selfimg) 
         # Convert image to PhotoImage object
        bg_img1 =Label(leftMenu, image=self.photoselfimg)  # Label with image
        bg_img1.pack(side=TOP,fill=X)

        selfimg1 = Image.open(r"img/arrow.jpg")
        selfimg1 = selfimg1.resize((30, 30), Image.LANCZOS)
        self.photoselfimg1 = ImageTk.PhotoImage(selfimg1)

        # Define btn_Manu using the PhotoImage directly
        btn_Manu = Label(leftMenu, text="Menu",font=("times new roman", 30), bg="#87ceeb", cursor="hand2")
        btn_Manu.pack(side=TOP, fill=X)

        # Optional: Create another Label with the same image
       

        btn_Emp =Button(leftMenu, text="Employee",command=self.employee,image=self.photoselfimg1, compound=LEFT,padx=5,anchor="w", font=("times new roman", 20,"bold"), bg="white",bd=3, cursor="hand2")
        btn_Emp.pack(side=TOP,fill=X)
        
        btn_Emp1 =Button(leftMenu, text="Supplier",command=self.Supplier,image=self.photoselfimg1, compound=LEFT,padx=5,anchor="w", font=("times new roman", 20,"bold"), bg="white",bd=3, cursor="hand2")
        btn_Emp1.pack(side=TOP,fill=X)

        btn_Emp2 =Button(leftMenu, text="Category",command=self.category,image=self.photoselfimg1, compound=LEFT,padx=5,anchor="w", font=("times new roman", 20,"bold"), bg="white",bd=3, cursor="hand2")
        btn_Emp2.pack(side=TOP,fill=X)
        


        btn_Emp3 =Button(leftMenu, text="Products",command=self.product,image=self.photoselfimg1, compound=LEFT,padx=5,anchor="w", font=("times new roman", 20,"bold"), bg="white",bd=3, cursor="hand2")
        btn_Emp3.pack(side=TOP,fill=X)


        btn_Emp4 =Button(leftMenu, text="Sales",command=self.sales,image=self.photoselfimg1, compound=LEFT,padx=5,anchor="w", font=("times new roman", 20,"bold"), bg="white",bd=3, cursor="hand2")
        btn_Emp4.pack(side=TOP,fill=X)


        btn_Ex =Button(leftMenu, text="Billing",command=self.billing, font=("times new roman", 25,"bold"), bg="white",bd=3, cursor="hand2")
        btn_Ex.pack(side=TOP,fill=X)

        title_footer = Label(self.root, text="IMS-Inventory Management System\n developed by Sunil Nagar",anchor="center", font=("Times New Roman", 10, "bold"), bg="#87ceeb", fg="black")
        title_footer.place(x=0, y=650, width=1350, height=50)

        self.ibl_empl=Label(rightMenu,text="Total Employee\n[0]",bd=5,relief=RIDGE,bg="#33bbf9",fg="white",font=("times new roman",20,"bold"))
        self.ibl_empl.place(x=100,y=20,height=150,width=300)


        self.ibl_sup=Label(rightMenu,text="Total Supplier\n[0]",bd=5,relief=RIDGE,bg="#ff5722",fg="white",font=("times new roman",20,"bold"))
        self.ibl_sup.place(x=700,y=20,height=150,width=300)

        self.ibl_cat=Label(rightMenu,text="Total Category\n[0]",bd=5,relief=RIDGE,bg="#ffc107",fg="white",font=("times new roman",20,"bold"))
        self.ibl_cat.place(x=400,y=170,height=150,width=300)


        self.ibl_prod=Label(rightMenu,text="Total Products\n[0]",bd=5,relief=RIDGE,bg="#009688",fg="white",font=("times new roman",20,"bold"))
        self.ibl_prod.place(x=100,y=320,height=150,width=300)



        self.ibl_sale=Label(rightMenu,text="Total Sales\n[0]",bd=5,relief=RIDGE,bg="#607d8b",fg="white",font=("times new roman",20,"bold"))
        self.ibl_sale.place(x=700,y=320,height=150,width=300)


        self.update_content()
 #=============================================================================================================#
    def employee(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=Emp(self.new_win)
    def Supplier(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=sup(self.new_win)
    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=cat(self.new_win)
    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=prod(self.new_win)
    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=sal(self.new_win)
    def billing(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=bills(self.new_win)    

    def update_content(self):
        conn=sqlite3.connect('SQL Database/IMS.db')
        cur = conn.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.ibl_prod.config(text=f"Total Product\n[{str(len(product))}]")
            

            cur.execute("select * from product")
            product=cur.fetchall()
            self.ibl_prod.config(text=f"Total Product\n[{str(len(product))}]")

            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.ibl_sup.config(text=f"Total Supplier\n[{str(len(supplier))}]")

            cur.execute("select * from category")
            category=cur.fetchall()
            self.ibl_cat.config(text=f"Total Category\n[{str(len(category))}]")

            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.ibl_empl.config(text=f"Total Employee\n[{str(len(employee))}]")
            

            bill=len(os.listdir('bill'))
            self.ibl_sale.config(text=f"Total Sales\n [{str(bill)}]")

        except Exception as es:
            messagebox.showerror("Error", f"Due to :{str(es)}", parent=self.root)


      # Ensure time is properly imported

    def update_time(self):
        current_time = time.strftime("%I:%M:%S %p")  # Added AM/PM format
        current_date = time.strftime("%d-%m-%Y")
        
        if hasattr(self, "clock_lbl"):  # Ensure clock_lbl exists before updating
            self.clock_lbl.config(text=f"Welcome to Inventory Management System\t\t Date: {current_date}\t\t Time: {current_time}")
        self.root.after(1000, self.update_time)         
    def logout(self):
        self.root.destroy()
        os.system("python login.py")      

        
# ===== RUN THE APPLICATION ===== #
if __name__ == "__main__":
    root = Tk()
    obj = IMS(root)  # Create object of IMS class
    root.mainloop()  # Start the main loop to run the application
