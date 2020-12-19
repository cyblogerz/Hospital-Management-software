from Subpackage import funcs
from Subpackage.funcs import *
import Subpackage.database

print('*'*100+'\n'+'Welcome to hospital management System'.center(100, '*')+'\n'+'*'*100)

on = True
while on:
    select = input("Enter 'o' Outpatient\nEnter 's' for Managing store\nEnter 'p' for managing pharmacy\nEnter 'r' for viewing patient records Enter 'b' for billing\n::")
    if select.lower() == 'o':
        register()
    elif select.lower() == 's':
        s = input("Press 'v' to view current medicine stock\nPress 'e' to execute stock exchange\nPress 'a' to add medicine to store\n::")
        if s.lower() == 'v':
            vstore_prompt()
        elif s.lower() == 'e':
            ex_prompt()
        elif s.lower() == 'a':
            add_prompt()

    elif select.lower() == 'p':
        s = input(
            "Press 'v' to see current stock in pharmacy\nPress 'i' to issue medicine from pharmacy\n::")
        if s.lower() == 'v':
            vpharm_prompt()
        elif s.lower() == 'i':
            ipharm_prompt()

    elif select.lower() == 'r':
        pr_prompt()

    elif select.lower() == 'b':
        bill_prompt()
