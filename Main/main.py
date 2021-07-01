"""
CHANGE LOG:
>> 30th June 2021
>> Removed redundant Code
>> Restructured Code
>> Shifted 2 Class(es) to database.py
    - Medicine
    - Patient
>> Added few Functions
>> Added Type Hinting
>> Refactored Functions
>> Optimised import statements
>> Reduced Code size
"""

from typing import Callable, Union

from database import Patient, Medicine, add_paient, patient_list
from database import med_search, issue, reg_no, addvalue, view


def register() -> int:
    pat_stat = input("Press 'n' for registering new patient\nPress 'r' for re-visit\n").lower()
    if pat_stat == 'n':
        add_paient(Patient(input('Name: '), input('Place: '), input('Phone: '), int(input('Age: ')), 1))
        print('Patient registered')

    elif pat_stat == 'r':
        print(reg_no(input('Enter the registration number: ')))

    return 1 if input("Do you want to continue? ") else 0


def manage_store() -> int:
    choice = input("""
Press 'v' to view current medicine stock
Press 'e' to execute stock exchange
Press 'a' to add medicine to store
        """).lower()
    while choice not in ('v', 'e', 'a'):
        choice = input("INVALID CHOICE TRY AGAIN: ")
    return vstore_prompt() if choice == 'v' else ex_prompt() if choice == 'e' else add_prompt()


def manage_pharmacy() -> int:
    choice = input("""
Press 'v' to see current stock in pharmacy
Press 'i' to issue medicine from pharmacy
        """).lower()
    while choice not in ('v', 'i'):
        choice = input("INVALID CHOICE TRY AGAIN: ")
    return vpharm_prompt() if choice == 'v' else ipharm_prompt()


def pr_prompt() -> int:
    return prompt(pr_prompt, patient_list())


def bill_prompt() -> int:
    print('This feature is yet to come')
    return 0


def stock_ex(med: Medicine, stock: int) -> None:
    issue(med, stock, "store")
    addvalue(med, stock)
    print('Medicine issued successfully!!')


def billing(med: Union[list, Medicine], cons_fee: int) -> str:
    mrp = 0
    if type(med) == type(list):
        for item in med:
            mrp += item.price
    else:
        mrp = med.price
    return f'Name:\tPrice:\tConsultation Fee\tOverall:\n{med.name}\t{mrp}\t{cons_fee}\t{mrp + cons_fee}'


def prompt(func: Callable, string=None) -> int:
    if string:
        print(string)
    choice = input("Press 't' to do again\nPress 'p' to go back\nPress 'x' to exit\n").lower()
    if choice == 't':
        func()
    elif choice == 'p':  # return 1 to continue
        return 1
    elif choice == 'x':  # return 0 to break
        print("exiting...")
    return 0


def ex_prompt() -> int:
    stock_ex(med_search(input('Enter name of the medicine: ')), int(input('Enter stock quantity: ')))
    return prompt(ex_prompt)


def add_prompt() -> int:
    addvalue(med_store(), int(input('Enter stock quantity\n::')))
    return prompt(add_prompt)


def ipharm_prompt() -> int:
    issue(med_search(input('Enter medicine name\n::')), int(input('Enter amount::')), "pharmacy")
    return prompt(ipharm_prompt)


def vstore_prompt() -> int:
    return prompt(vstore_prompt, view("store"))


def vpharm_prompt() -> int:
    return prompt(vpharm_prompt, view("pharma"))


def med_store() -> Medicine:
    n = input('Enter name of medicine: ').lower()
    c = input('Enter company: ')
    e = input('Enter Expiry date (DD/MM/YY): ')
    p = int(input('Enter price: '))
    return Medicine(c, e, n, p)


#########################################################################################################
print(f"{'*' * 100}\n{'Welcome to hospital management System'.center(100, '*')}\n{'*' * 100}")

while 1:
    select = input("""
Enter 'o' for Outpatient
Enter 's' for Managing Store
Enter 'p' for Managing Pharmacy
Enter 'r' for viewing Patient Records
Enter 'b' for Billing
""").lower()
    result: int = 0
    if select == 'o':
        result = register()
    elif select == 's':
        result = manage_store()
    elif select == 'p':
        result = manage_pharmacy()
    elif select == 'r':
        result = pr_prompt()
    elif select == 'b':
        result = bill_prompt()
    if result:
        continue
    else:
        break
