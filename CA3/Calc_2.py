# -*- coding: utf-8 -*-
"""
Created on Fri May 9 14:34:13 2020

@author: quinn
"""

from Calc_Def import function_calculator

 #Display banner   
def __show_banner():
        print('#'*52)
        print('Welcome to the sequence calculator with 10 functions')
        print('#'*52, '\n')
          
#Defining operator menu         
def operator_menu():
    print('1  to Sum values in a list ')
    print('2 to find maximum value in list')
    print('3 to find minimum value in list')
    print('4 to Sum 2 lists')
    print('5  get even numbers from in list')
    print('6 list numbers to cube')
    print('7 to convert Miles to Kilometers')
    print('8 to convert Deg C to Deg F')
    print('9 find values greater than the mean value')
    print('0 Generate fibonacci sequence')
    
#Defining operations per menu choice    
def process_operation():
        operator_menu()
        
        #User definded opeator input
        operation = input ('\nWhat calculation would you like to do?\n')
        
        #Bypass for fibonacci
        if operation not in ['0']:
            x = list(map(float, input("Enter xlist of numbers (space separated): ").split())) 
            print(x)
    
        #Bypass all but option 4 sum list 
        if operation not in ['0','1','2','3','5','6','7','8','9']:
            y = list(map(float, input("Enter ylist of numbers (space separated): ").split())) 
            print(y)

        #Bypass fibonacci
        if operation not in ['1','2','3','4','5','6','7','8','9']:
            low = int(input('\nEnter low'))
            high = int(input('\nEnter high'))
            print (low, high)

        #Sum List operatin
        if operation in  ['1']:
            print('Answer:', function_calculator().sum_list(x))
            
        #Max value in list
        if operation in['2']:
            print('Answer:', function_calculator().max(x))
        
        #Min value in list
        if operation in['3']:
            print('Answer:', function_calculator().min(x))
        
        #Sum 2 lists
        if operation in  ['4']:
            print('Answer:', function_calculator().add(x, y))
        
        #Get even numbers from list
        if operation in  ['5']:
            print('Answer:', function_calculator().is_even(x))
            
        #Cube numbers in a list
        if operation in ['6']:
           print ('Answer:', function_calculator().cube(x))
        
        #Mi to Km converter
        if operation in ['7']:
            print ('Answer:', function_calculator().mi_km(x))
       
        #Deg C to Deg F converter
        if operation in ['8']:
            print ('Answer:', function_calculator().C_to_F(x))
        
        #Find values greater that mean in a list
        if operation in ['9']:
            print ('Answer:', function_calculator().greater_than_mean(x))
        
        #Generate fibonacci seq
        if operation in ['0']:
            print ('answer:', function_calculator().fibonacci(low, high))
            
    #Loop to cycle calculator operation
def process():
    go_again = ''
    while go_again != 'n':
        process_operation()
            #Loop break-out option
        go_again = input('Would you like to continue (Y/N)?\n') 

process()

    

