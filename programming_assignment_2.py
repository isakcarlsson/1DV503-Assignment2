import mysql.connector
import csv
from random import randint

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
        for i in range(5):
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

def generate_products(sect):
    '''
    Returns a list of 1 - 3 unique product_id 
    '''
    lst = []
    prod = []

    for i in sect:
        lst.append(i[0])

    for i in range(randint(1, 4)):
        rdm = randint(0, len(lst) - 1)
        prod.append(lst[rdm])
        lst.pop(rdm)

    return prod

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
        age TINYINT,
        email VARCHAR(70),
        PRIMARY KEY(id));""")

        for employee in data_employees:
            if employee[0] != 'NULL':
                mycursor.execute(f'''INSERT INTO Employees
                (name, job_title, gender, age, email)
                VALUES
                ({employee[0]},{employee[1]},{employee[2]},{employee[3]},{employee[4]})''')
    
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

        for employee in range(1, 1001):
            rdm = randint(1, 3)
            s = set()
            while len(s) <= rdm:
                s.add(randint(1, 50))        
            for i in s:
                mycursor.execute(f"""INSERT INTO WorksFor
                (company_id, employee_id)
                VALUES
                ({i}, {employee})""")

    cnx.commit()

    if not has_table('Produces'):
        mycursor.execute("""CREATE TABLE Produces (company_id INT NOT NULL,
        product_id INT NOT NULL,
        PRIMARY KEY(company_id, product_id));""")
    
        mycursor.execute("""SELECT id FROM Products WHERE sector = 'Health Care'""")
        health_care = mycursor.fetchall()
        mycursor.execute("""SELECT id FROM Products WHERE sector = 'Consumer'""")
        consumer = mycursor.fetchall()
        mycursor.execute("""SELECT id FROM Products WHERE sector = 'Technology'""")
        technology = mycursor.fetchall()
        mycursor.execute("""SELECT id FROM Products WHERE sector = 'Finance'""")
        finance = mycursor.fetchall()
        mycursor.execute("""SELECT id FROM Products WHERE sector = 'Transport'""")
        transport = mycursor.fetchall()
        mycursor.execute("""SELECT id FROM Products WHERE sector = 'Energy'""")
        energy = mycursor.fetchall()
        mycursor.execute("""SELECT id FROM Products WHERE sector = 'Agriculture'""")
        agriculture = mycursor.fetchall()
            
        mycursor.execute("""SELECT id FROM Companies WHERE sector = 'Health Care'""")
        comp_health = mycursor.fetchall()
        mycursor.execute("""SELECT id FROM Companies WHERE sector = 'Consumer'""")
        comp_consumer = mycursor.fetchall()
        mycursor.execute("""SELECT id FROM Companies WHERE sector = 'Technology'""")
        comp_tech = mycursor.fetchall()
        mycursor.execute("""SELECT id FROM Companies WHERE sector = 'Finance'""")
        comp_finance = mycursor.fetchall()
        mycursor.execute("""SELECT id FROM Companies WHERE sector = 'Transportation'""")
        comp_trans = mycursor.fetchall()
        mycursor.execute("""SELECT id FROM Companies WHERE sector = 'Energy'""")
        comp_energy = mycursor.fetchall()
        mycursor.execute("""SELECT id FROM Companies WHERE sector = 'Agriculture'""")
        comp_agri = mycursor.fetchall()

        for comp in comp_health:
            products = generate_products(health_care)
            for i in products:
                mycursor.execute(f"""INSERT INTO Produces
                (company_id, product_id)
                VALUES
                ({comp[0]}, {i})""")
        
        for comp in comp_consumer:
            products = generate_products(consumer)
            for i in products:
                mycursor.execute(f"""INSERT INTO Produces
                (company_id, product_id)
                VALUES
                ({comp[0]}, {i})""")
        
        for comp in comp_tech:
            products = generate_products(technology)
            for i in products:
                mycursor.execute(f"""INSERT INTO Produces
                (company_id, product_id)
                VALUES
                ({comp[0]}, {i})""")

        for comp in comp_finance:
            products = generate_products(finance)
            for i in products:
                mycursor.execute(f"""INSERT INTO Produces
                (company_id, product_id)
                VALUES
                ({comp[0]}, {i})""")
        
        for comp in comp_trans:
            products = generate_products(transport)
            for i in products:
                mycursor.execute(f"""INSERT INTO Produces
                (company_id, product_id)
                VALUES
                ({comp[0]}, {i})""")

        for comp in comp_energy:
            products = generate_products(energy)
            for i in products:
                mycursor.execute(f"""INSERT INTO Produces
                (company_id, product_id)
                VALUES
                ({comp[0]}, {i})""")

        for comp in comp_agri:
            products = generate_products(agriculture)
            for i in products:
                mycursor.execute(f"""INSERT INTO Produces
                (company_id, product_id)
                VALUES
                ({comp[0]}, {i})""")

    if not has_table('CompanyRelations'):
        create_view()

    cnx.commit()

def create_view():
    mycursor.execute("""CREATE VIEW CompanyRelations AS
    SELECT id, name, market_cap, sector, country, slogan, product_id, employee_id
    FROM Companies 
    JOIN Produces ON Companies.id = Produces.company_id
    JOIN WorksFor ON Companies.id = WorksFor.company_id""")

def crypto_companies():
    """
    Returns a list of companies that has an Crypto exchange as product
    """
    mycursor.execute("""SELECT CompanyRelations.name FROM CompanyRelations
    JOIN Products ON CompanyRelations.product_id = Products.id
    WHERE Products.name = 'Crypto exchange'
    GROUP BY CompanyRelations.name""")

    return mycursor.fetchall()

def avg_age_sector():
    mycursor.execute("""SELECT CompanyRelations.sector, AVG(Employees.age) 
    FROM CompanyRelations
    JOIN Employees ON Employees.id = CompanyRelations.employee_id
    WHERE sector IS NOT NULL 
    GROUP BY sector""")
    
    return mycursor.fetchall()

def email_product(inp):
    mycursor.execute("""SELECT email FROM Employees
    JOIN CompanyRelations ON CompanyRelations.employee_id = Employees.id
    JOIN Products ON CompanyRelations.product_id = Products.id
    WHERE Products.name = %s""", (inp,))

    return mycursor.fetchall()
    
def get_products():
    mycursor.execute("""SELECT name FROM Products""")
    return mycursor.fetchall()

mycursor = cnx.cursor()

#Create database
if not has_database(DB_NAME):
    mycursor.execute("CREATE DATABASE " + DB_NAME)

mycursor.execute("USE " + DB_NAME)

data = read_files_to_lists(path_companies, path_employees, path_products)
create_tables(data[0], data[1], data[2])

