import os
from tkinter import BOTH, END, RIDGE, RIGHT, VERTICAL, X, Y, Button, Entry, Frame, Image, Label, Listbox, Scrollbar, StringVar, Text, Tk, messagebox
from PIL import Image, ImageTk

class sal:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1100x500+220+130")
        self.root.title("Inventory Management System")
        self.var_invoice=StringVar()
        self.bill_list=[]

        title_lbl = Label(self.root, text="View Customer Bills",anchor="center", font=("Times New Roman", 40, "bold"), bg="#87ceeb", fg="black")
        title_lbl.place(x=0, y=0, width=1100, height=70)

        ibl_invoice= Label(self.root,text="Invoice No.",font=("Times New Roman",15,"bold") )
        ibl_invoice.place(x=50,y=100)
        tex_invoice=Entry(self.root,textvariable=self.var_invoice,font=("times new roman",15),bg="light yellow")
        tex_invoice.place(x=160,y=100,width=180,height=30)
        
        search_btn=Button(self.root,text="Search",command=self.search, width=12,font=("Times New Roman", 12, "bold"), bg="green", fg="white")
        search_btn.place(x=360,y=100,width=120,height=28)
        Showall_btn=Button(self.root,text="Clear All",command=self.Clear, width=12,font=("Times New Roman", 12, "bold"), bg="blue", fg="white")
        Showall_btn.place(x=490,y=100,width=120,height=28)

        bill_Frame=Frame(self.root, bd=2, bg="white", relief=RIDGE)
        bill_Frame.place(x=10, y=150, width=200, height=330)
        scroll_y=Scrollbar(bill_Frame, orient=VERTICAL)  
        self.Sales_list=Listbox(bill_Frame, font=("times new roman",15), yscrollcommand=scroll_y.set)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_y.config(command=self.Sales_list.yview)
        self.Sales_list.pack(fill=BOTH,expand=1)
        self.Sales_list.bind("<ButtonRelease-1>",self.get_data)
 

        bill_Frame1=Frame(self.root, bd=2, bg="lightyellow", relief=RIDGE)
        bill_Frame1.place(x=210, y=150, width=400, height=330)
        title_bill = Label(bill_Frame1, text=" Customer Bills Area",anchor="center", font=("Times New Roman", 00, "bold"), bg="#87ceeb", fg="black")
        title_bill.place(x=0, y=0, width=400, height=40)
        scroll_y1=Scrollbar(bill_Frame1, orient=VERTICAL)
        self.bill_area=Text(bill_Frame1,  yscrollcommand=scroll_y1.set)
        scroll_y1.pack(side=RIGHT, fill=Y)
        scroll_y1.config(command=self.bill_area.yview)
        self.bill_area.pack(fill=BOTH,expand=1)

        

        img = Image.open(r"img/bill.png")  # Load the logo image
        img = img.resize((600, 410), Image.LANCZOS)  # Resize to fit header
        self.photoimg = ImageTk.PhotoImage(img)
        bg_img = Label(self.root, image=self.photoimg , bg="white")  # Create label with image
        bg_img.place(x=620, y=70, width=600, height=415)




        self.show()
    #===========================================================================================================#
    
    def show(self):
        self.bill_list[:]
        self.Sales_list.delete(0,END)
        #print(os.listdir('bill'))
        for i in os.listdir("bill"):
            if i.split('.')[-1]=='txt':
                self.Sales_list.insert(END,i)
                self.bill_list.append(i.split('.')[0])
        
    def get_data(self,ev):
        index_=self.Sales_list.curselection()
        file_name=self.Sales_list.get(index_)
        self.bill_area.delete('1.0',END)
        fp=open(f'bill/{file_name}','r')
        for i in fp:
            self.bill_area.insert(END,i)
        fp.close()    

    def search(self):
        if self.var_invoice.get()=="":
            messagebox.showerror("Error","Invoice No. should be required",parent=self.root)
        else:
            if self.var_invoice.get() in self.bill_list:
                fp=open(f'bill/{self.var_invoice.get()}.txt','r')
                self.bill_area.delete('1.0',END)
                for i in fp:
                   self.bill_area.insert(END,i)
                fp.close() 
            else:
                messagebox.showerror("Error","Invelid Invoice No.",parent=self.root)
                           
    def Clear(self):
        self.show()
        self.bill_area.delete('1.0',END)




if __name__ == "__main__":
    root=Tk()
    obj=sal(root)
    root.mainloop() 