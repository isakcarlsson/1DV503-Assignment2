import tkinter as tk
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
    global lb
    root = tk.Tk()

    lb = tk.Listbox(root, selectmode='browse')
    lb.size
    lb.place(relx=0.5, rely=0.5, anchor='center')
    lb.bind('<<ListboxSelect>>', listbox_cb)

    for i in pa.get_products():
        lb.insert('end', i[0])

def list_to_table(lst):

    root = tk.Tk()
    root.title("")
    # find total number of rows and 
    # columns in list 
    total_rows = len(lst) 
    total_columns = len(lst[0]) 

    for i in range(total_rows): 
        for j in range(total_columns): 
                
            e = tk.Entry(root, width=20, fg='black', font=('Arial',16)) 
                
            e.grid(row=i, column=j) 
            e.insert(tk.END, lst[i][j]) 
    root.mainloop()

def listbox_cb(var):
    lst = pa.get_products()
    lst = pa.email_product(lst[lb.curselection()[0]][0])
    lst.insert(0, ('EMAIL', ))
    list_to_table(lst)

window = tk.Tk()
window.title("Assignment 2")
window.geometry("1000x700")


btn_crypto = tk.Button(text="Get Company name of all companies that has Crypto exchange as a product", command=crypto)
btn_crypto.place(relx=0.5, rely=0.4, anchor='center')

btn_age = tk.Button(text="Get average age for every sector", command=age)
btn_age.place(relx=0.5, rely=0.5, anchor='center')

btn_email = tk.Button(text="Get every email for employees that works for a company that makes a certain product", command=email)
btn_email.place(relx=0.5, rely=0.6, anchor='center')

window.mainloop()
