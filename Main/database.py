from sqlite3 import connect
from sqlite3.dbapi2 import Connection, Cursor


class Medicine:
    def __init__(self, company: str, expiry: str, name: str, price: int) -> None:
        self.company = company
        self.expiry = expiry
        self.name = name
        self.price = price

    def __str__(self) -> str:
        return f'Name:{self.name}\nCompany:{self.company}\nExpiry:{self.expiry}'


class Patient:
    def __init__(self, name: str, place: str, phone: str, age: int, visit: int) -> None:
        self.name = name
        self.place = place
        self.age = age
        self.phone = phone
        self.visit = visit


def connect_cursor() -> tuple[Connection, Cursor]:
    con: Connection = connect("HMS.db")
    cur: Cursor = con.cursor()
    return con, cur


def commit_close(con: Connection) -> None:
    con.commit()
    con.close()


def addvalue(med: Medicine, stock: int) -> None:
    con, cur = connect_cursor()
    value = med.name, med.company, med.expiry, stock, med.price
    cur.execute(f"INSERT INTO store VALUES{value}")
    commit_close(con)


def issue(med: Medicine, st: int, place: str) -> None:
    con, cur = connect_cursor()
    cur.execute(f"SELECT rowid,* FROM {place} WHERE name = {med.name}")
    stock = 0
    for i in cur.fetchall():
        stock += i[3]
    if stock == st:
        con.execute(f"DELETE FROM {place} WHERE name = {med.name}")
    elif stock < st:
        print("Not enough stock")
    else:
        con.execute(f"UPDATE {place} SET stock = {stock - st}")
    commit_close(con)


def add_paient(pat: Patient) -> None:
    con, cur = connect_cursor()
    values = pat.name, pat.age, pat.place, pat.phone, pat.visit
    cur.execute(f"INSERT INTO patients VALUES{values}")
    commit_close(con)


def view(place: str) -> str:
    con, cur = connect_cursor()
    cur.execute(f"SELECT * FROM {place}")
    s = "Name:\tCompany:\tExpiryDate:\tStock:\tPrice:\n"
    for i in cur.fetchall():
        s += f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\n"
    commit_close(con)
    return s


def patient_list() -> str:
    con, cur = connect_cursor()
    cur.execute("SELECT rowid,* FROM patients")
    s = "Regno:\tName:\tAge:\tPlace:\tPhone:\tVisit:\n"
    for i in cur.fetchall():
        s += f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\n"
    commit_close(con)
    return s


def reg_no(regno: str) -> str:
    con, cur = connect_cursor()
    cur.execute(f"UPDATE patients SET visit=visit+1 WHERE rowid = {regno}")
    cur.execute(f"SELECT rowid,* FROM patients WHERE rowid = {regno}")
    s = "Regno:\tName:\tAge:\tPlace:\tPhone:\tVisit:\n"
    for i in cur.fetchall():
        s += f"{i[0]}\t{i[1]}\t{i[2]}\t{i[3]}\t{i[4]}\t{i[5]}\n"
    commit_close(con)
    return s


def med_search(med_name: str) -> Medicine:
    con, cur = connect_cursor()
    cur.execute(f"SELECT * FROM store WHERE name = {med_name}")
    m = cur.fetchall()
    name = ""
    company = ""
    expiry_date = ""
    price = 0
    for i in m:
        name += i[0]
        company += i[1]
        expiry_date += i[2]
        price += i[4]
    commit_close(con)
    return Medicine(company, expiry_date, name, price)
