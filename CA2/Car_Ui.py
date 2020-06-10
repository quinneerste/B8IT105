# -*- coding: utf-8 -*-
"""
Created on Thu May 28 15:22:35 2020

@author: quinn

"""


from Car import CarRental
    
rental = CarRental()
rental.store_csv() 
def mainMenu():
    print('#'*26)
    print('Welcome to DBS Car Rental')
    print('#'*26, '\n')     
    rental.check_stock_current()
    Car = None
    user_options = ('Would you like to Rent or Return a car ? \n Options: \n R - Rent \n U - Return \n C - Check current stock \n Any key to quit:  ')
    answer = input(user_options)
    while answer == 'R' or answer == 'U' or answer =='C':
        if answer == 'R':
            type = input('Select a category your rental choice ? -\n P for Petrol;\n D for Diesel;\n H for Hybrid;\n E for electric\n Please make a selection:  ')
            amount = int(input('How many cars would you like to Rent ?:  '))
            total = 0
            if rental.check_stock_rent(type) < amount:
                print('No cars available')
                break
            else:
                while total < amount:
                    rental.rent(type)
                    total = total + 1
                rental.store_csv()
        elif answer == 'U':
            type = input('Select the category you wish to Return -\n P for petrol;\n D for Diesel;\n H for Hybrid;\n E for electric\n please enter one of the above letters:  ')
            amount = int(input('How many cars would you like to Return ?:  '))
            total = 0
            if rental.check_stock_ret(type) < amount:
                print('Invalid return amount - please start again')
                break
                while total < amount:
                    rental.ret(type, Car)
                    total = total + 1
                rental.stock_csv()
        elif answer == 'C':
            rental.check_stock_current()            
        answer = input(user_options)


mainMenu()
