import sqlite3

def add_store(med,stock):
	conn=sqlite3.connect('HMS.db')
	c=conn.cursor()
	c.execute("INSERT INTO store VALUES(?,?,?,?,?)",(med.name,med.company,med.expiry,stock,med.price))
	conn.commit()
	conn.close()

def add_pharma(med,stock):
	conn=sqlite3.connect('HMS.db')
	c=conn.cursor()
	c.execute("INSERT INTO store VALUES(?,?,?,?,?)",(med.name,med.company,med.expiry,stock,med.price))
	conn.commit()
	conn.close()

def rem_store(med,st):
    conn=sqlite3.connect('HMS.db')
    c=conn.cursor()
    c.execute("SELECT rowid,* FROM store WHERE name=(?)",med.name)
    m=c.fetchall()
    stock=0
    for i in m:
    	stock+=i[3]
    if stock == st:
    	c.execute("DELETE FROM store WHERE name=(?)",med.name)
    elif stock<st:
    	print('Not enough stock')
    else:
    	c.execute("UPDATE store SET stock=stock-st")

    conn.commit()
    conn.close()

def pharma_issue(med,st):
	conn=sqlite3.connect('HMS.db')
	c=conn.cursor()
	c.execute("SELECT rowid,* FROM pharmacy WHERE name=(?)",med.name)
	m=c.fetchall()
	stock=0
	for i in m:
		stock+=i[3]
    
	if stock == st:

		c.execute("DELETE FROM pharmacy WHERE name=(?)",med.name)
	elif stock<st:
		print('stock is not enough')
    
	else:
		c.execute("UPDATE pharmacy SET stock=stock-st")
    
	conn.commit()
	conn.close()

def add_pt(pat):
	conn=sqlite3.connect('HMS.db')
    
	c=conn.cursor()
	c.execute("INSERT INTO patients VALUES(?,?,?,?,?)",(pat.name,pat.age,pat.place,pat.phone,pat.visit))
	conn.commit()
	conn.close()


#
def view_store():
	conn=sqlite3.connect('HMS.db')
	c=conn.cursor()
	c.execute("SELECT * FROM store")
	st=c.fetchall()
	conn.commit()
	conn.close()
	s='Name:\tCompany:\tExpiryDate:\tStock:\tPrice:\n'
	for i in st:
		s+=f'{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\n'
	return s
	


def view_pharma():
	conn=sqlite3.connect('HMS.db')
	c=conn.cursor()
	c.execute("SELECT * FROM pharmacy")
	st=c.fetchall()
	conn.commit()
	conn.close()
	s='Name:\tCompany:\tExpiryDate:\tStock:\tPrice:\n'
	for i in st:
		s+=f'{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\n'
	return s
	
def reg_no(regno):
	conn=sqlite3.connect('HMS.db')
	c=conn.cursor()
	c.execute("UPDATE patients SET visit=visit+1 WHERE rowid=(?)",regno)
	c.execute("SELECT rowid,* FROM patients WHERE rowid= (?)",regno)
	pat=c.fetchall()
	conn.commit()
	conn.close()
	s='Regno:\tName:\tAge:\tPlace:\tPhone:\tVisit:\n'
	for i in pat:
		s+=f'{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\n'
	return s
	

def pat_list():
	conn=sqlite3.connect('HMS.db')
	c=conn.cursor()
	
	c.execute("SELECT rowid,* FROM patients")
	p=c.fetchall()
	conn.commit()
	conn.close()
	s='Regno:\tName:\tAge:\tPlace:\tPhone:\tVisit:\n'
	for i in p:
		s+=f'{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\n'
	return s
	
def med_search(n):
	conn=sqlite3.connect('HMS.db')
	c=conn.cursor()
    
	c.execute("SELECT * FROM store WHERE name = (?)",n)
   
    
	m=c.fetchall()
	
	conn.commit()
	conn.close()
	Name =''     
	Company=''
	ExpiryDate=''
	Price=0
	for i in m:
		Name+=i[0]
		Company+=i[1]
		ExpiryDate+=i[2]
		Price+=i[4]
	med=Medicine(Company,ExpiryDate,Name,Price)
	return med
