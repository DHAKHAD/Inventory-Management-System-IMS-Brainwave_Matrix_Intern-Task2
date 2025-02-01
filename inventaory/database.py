import sqlite3

# Connect to the SQLite database
conn = sqlite3.connect('SQL Database\IMS.db')  # Ensure this path is correct
c = conn.cursor()

# Create the Product table
c.execute("""CREATE TABLE IF NOT EXISTS product (
            Name TEXT,
            ProductID TEXT NOT NULL PRIMARY KEY,
            Category TEXT,
            Supplier TEXT,   
            Price TEXT,
            Quantity TEXT,
            Status TEXT
            )""")  # Removed the trailing comma and added IF NOT EXISTS

# Fetch all records
c.execute("SELECT * FROM product")

# Supplier table

c.execute("""CREATE TABLE IF NOT EXISTS supplier (
            EmployeeName TEXT,
            EmployeeID TEXT NOT NULL PRIMARY KEY,
            Date TEXT,
            Invoice TEXT,   
            Mobile TEXT,
            Address TEXT
            )""")  # Removed the trailing comma and added IF NOT EXISTS

# Fetch all records
c.execute("SELECT * FROM supplier")

#Employee table
c.execute("""CREATE TABLE IF NOT EXISTS employee (
            EmployeeName text,
            EmployeeID text NOT NULL PRIMARY KEY,
            Gender text,
            Date text,
            User text,
            Pass text,
            salery text,   
            Mobile text,
            Email text,
            Address text,
            Photo text
            )""")  # Removed the trailing comma and added IF NOT EXISTS

# Fetch all records
c.execute("SELECT * FROM employee")
    


#category table

c.execute("""CREATE TABLE IF NOT EXISTS category (
        
            ItemName TEXT,
            ItemID TEXT PRIMARY KEY
            )""")  # Removed the trailing comma and added IF NOT EXISTS

# Fetch all records
c.execute("SELECT * FROM category")  




items = c.fetchall()
print(items)

# Commit changes and close the connection
conn.commit()
conn.close()
