"""
this application manage a diamonds
"""
from enum import Enum 
import csv

diamond =[]

class Menu(Enum): #wich q to answer
    QA =1
    QB =2
    QC =3
    QD =4
    QE =5
    QF =6
    QG =7
    EXIT=0

def display_menu():
    for action in Menu:
        print(f'{action.value} -  {action.name}')
    return Menu(int( input("your selection?")))    
    

def read_csv_and_split(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
        return [line.split(',') for line in lines]




def qa():
     csv_data = read_csv_and_split('filename.csv')
      maxprice = 0 

    for line in csv_data:
        row = line.split(',')
        dimondPrice = float(row[6])  # Assuming price is the 7th column
        if dimondPrice > maxprice:
            maxprice = dimondPrice

    return maxprice


def qb():
     csv_data = read_csv_and_split('filename.csv')

    total_sum = sum(prices)
    num_prices = len(prices)

    if num_prices == 0:
        return 0.0  # Avoid division by zero

    average_price = total_sum / num_prices
    return average_price

def qc():
     csv_data = read_csv_and_split('filename.csv')




if __name__ =='__main__':
    while True:
        user_selection =display_menu()
        if user_selection == Menu.EXIT: exit()
        if user_selection == Menu.QA : qa()
        if user_selection == Menu.QB : qb() 
        if user_selection == Menu.QC : qc()
        if user_selection == Menu.QD : 
        if user_selection == Menu.QE : 
        if user_selection == Menu.QF : 
        if user_selection == Menu.QG :        


    

