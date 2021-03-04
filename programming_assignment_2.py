import mysql.connector
import csv

cnx = mysql.connector.connect(user='root', password='root', host='127.0.0.1')
DB_NAME='Assignment2'
path_companies = 'data/companies.csv'
path_employees = 'data/employees.csv'
path_products = 'data/products.csv'

def has_database(name):
    '''
    Return True if it has a databases with a certain name
    else return False
    '''
    mycursor.execute('SHOW DATABASES')
    dbs = mycursor.fetchall()
    for db in dbs:
        if str(db).strip(" ()',") == name:
            return True
    return False

def has_table(name):
    '''
    Return True if it has a table with a certain name
    else return False
    '''
    mycursor.execute('SHOW TABLES')
    tbls = mycursor.fetchall()
    for tbl in tbls:
        if str(tbl).strip(" ()',") == name:
            return True
    return False

def read_files_to_lists(path_companies, path_employees, path_products):
    with open(path_companies, mode='r') as f1, open(path_employees, mode='r') as f2, open(path_products, mode='r') as f3:
        r = csv.reader(f1)                  #Reads first file
        data_companies = [row for row in r]   #Puts every column in a row in a list and puts all lists in a list
        r = csv.reader(f2)                  #Read second file
        data_employees = [row for row in r]   #Put second file in list same way as first one
        r = csv.reader(f3)
        data_products = [row for row in r]

    data_companies.pop(0)                     #Deletes the first list, it only contains attribute name
    data_employees.pop(0)
    data_products.pop(0)

    #Loops through every row and column and change every invalid result to 'NULL'
    for company in data_companies:
        for i in range(5):
            if company[i] == 'n/a':
                company[i] = 'NULL'
            else:
               company[i] = '"' + company[i] + '"'

     #Loops through every row and column and change every invalid result to 'NULL'   
    for employee in data_employees:
        for i in range(4):
            if employee[i] == 'n/a':
                employee[i] = 'NULL'
            else:
                employee[i] = '"' + employee[i] + '"'
    
    for product in data_products:
        for i in range(2):
            if product[i] == 'n/a':
                product[i] = 'NULL'
            else:
                product[i] = '"' + product[i] + '"'

    return data_companies, data_employees, data_products

def create_tables(data_companies, data_employees, data_products):
    '''
    Creates all tables if there are no table with that name
    Then loops through the data lists and inserts data to table
    '''
    
    if not has_table('Companies'):
        mycursor.execute("""CREATE TABLE Companies (id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(45),
        market_cap INT,
        sector VARCHAR(45),
        country VARCHAR(45),
        slogan VARCHAR(200),
        PRIMARY KEY(id));""")

        for company in data_companies:
            if company[0] != 'NULL':
                mycursor.execute(f'''INSERT INTO Companies 
                (name, market_cap, sector, country, slogan) 
                VALUES 
                ({company[0]},{company[1]},{company[2]},{company[3]},{company[4]});''')


    if not has_table('Employees'):
        mycursor.execute("""CREATE TABLE Employees (id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(45),
        job_title VARCHAR(45),
        gender VARCHAR(6),
        email VARCHAR(70),
        PRIMARY KEY(id));""")

        for employee in data_employees:
            if employee[0] != 'NULL':
                mycursor.execute(f'''INSERT INTO Employees
                (name, job_title, gender, email)
                VALUES
                ({employee[0]},{employee[1]},{employee[2]},{employee[3]})''')
    
    if not has_table('Products'):
        mycursor.execute("""CREATE TABLE Products (id INT NOT NULL AUTO_INCREMENT,
        name VARCHAR(100),
        sector VARCHAR(45),
        PRIMARY KEY(id));""")

        for product in data_products:
            mycursor.execute(f'''INSERT INTO Products
            (name, sector)
            VALUES
            ({product[0]}, {product[1]})''')

    if not has_table('WorksFor'):
        mycursor.execute("""CREATE TABLE WorksFor (company_id INT NOT NULL,
        employee_id INT NOT NULL,
        PRIMARY KEY(company_id, employee_id));""")

        k = 0
        for i in range(1, 51):
            for j in range(1, 21):
                mycursor.execute(f"""INSERT INTO WorksFor
                (company_id, employee_id)
                VALUES
                ({i}, {j + k})""")
            k += 20


    if not has_table('Produces'):
        mycursor.execute("""CREATE TABLE Produces (company_id INT NOT NULL,
        product_id INT NOT NULL,
        PRIMARY KEY(company_id, product_id));""")
    
        
    cnx.commit()

def main_menu():
    pass

mycursor = cnx.cursor()

#Create database
if not has_database(DB_NAME):
    mycursor.execute("CREATE DATABASE " + DB_NAME)

mycursor.execute("USE " + DB_NAME)

data = read_files_to_lists(path_companies, path_employees, path_products)
create_tables(data[0], data[1], data[2])
main_menu()

cnx.close()
mycursor.close()