import tkinter as tk
from tkinter import ttk
import programming_assignment_2 as pa

def crypto():
    lst = pa.crypto_companies()
    lst.insert(0, ('COMPANY NAME',))
    list_to_table(lst)
    

def age():
    lst = pa.avg_age_sector()
    lst.insert(0, ('SECTOR', 'AVERAGE AGE'))
    list_to_table(lst)

def email():
    """
    Callback for 'email' button 
    """
    global lb
    root = tk.Tk()
    root.title('Products')

    lb = tk.Listbox(root, selectmode='browse')
    lb.size
    lb.place(relx=0.5, rely=0.5, anchor='center')
    lb.bind('<<ListboxSelect>>', listbox_cb)

    for i in pa.get_products():
        lb.insert('end', i[0])

def list_to_table(lst):
    """
    Takes a list and presents it in a table in a new window
    """
    root = tk.Tk()
    root.title("")

    tree = ttk.Treeview(root, selectmode='browse')
    tree.pack(side='left')

    scrlbar = ttk.Scrollbar(root, orient='vertical',command=tree.yview)
    scrlbar.pack(side='right', fill='x')

    tree.configure(xscrollcommand= scrlbar.set)

    l = []
    for i in range(len(lst[0])):
        l.append(str(i + 1))
    tree['columns'] = tuple(l)

    tree['show'] = 'headings'

    for i in range(len(lst[0])):
        tree.column(str(i + 1), width=250, anchor='sw')

    for i in range(len(lst[0])):
        tree.heading(str(i + 1), text =lst[0][i]) 
    lst.pop(0)
    
    for i in lst:
        tree.insert("", 'end', values =i) 

    root.mainloop()

def listbox_cb(var):
    lst = pa.get_products()
    lst = pa.email_product(lst[lb.curselection()[0]][0])
    lst.insert(0, ('EMAIL', ))
    list_to_table(lst)

def companies():
    lst = pa.companies_info()
    lst.insert(0, ('ID', 'NAME', 'MARKET CAP (million)', 'SECTOR', 'COUNTRY', 'SLOGAN'))
    list_to_table(lst)

def products():
    lst = pa.products_info()
    lst.insert(0, ('ID', 'NAME', 'SECTOR'))
    list_to_table(lst)

def employees():
    lst = pa.employees_info()
    lst.insert(0, ('ID', 'NAME', 'JOB TITLE', 'GENDER', 'AGE', 'EMAIL'))
    list_to_table(lst)


window = tk.Tk()
window.title("Assignment 2")
window.geometry("1000x700")

btn_companies = tk.Button(text="Show information about companies", command=companies)
btn_companies.place(relx=0.5, rely=0.1, anchor='center')

btn_employees = tk.Button(text="Show information about employees", command=employees)
btn_employees.place(relx=0.5, rely=0.2, anchor='center')

btn_products = tk.Button(text="Show information about products", command=products)
btn_products.place(relx=0.5, rely=0.3, anchor='center')

btn_crypto = tk.Button(text="Get Company name of all companies that has Crypto exchange as a product", command=crypto)
btn_crypto.place(relx=0.5, rely=0.4, anchor='center')

btn_age = tk.Button(text="Get average age for every sector", command=age)
btn_age.place(relx=0.5, rely=0.5, anchor='center')

btn_email = tk.Button(text="Get every email for employees that works for a company that makes a certain product", command=email)
btn_email.place(relx=0.5, rely=0.6, anchor='center')

window.mainloop()
