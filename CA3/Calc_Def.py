# -*- coding: utf-8 -*-
"""
Created on Thu May 8 13:40:47 2020

@author: quinn
"""
from functools import reduce

class function_calculator():
    
    def __init__(self):
        self.x = []
        self.y = []
        
    def set_x(self,x):
        self.x =x
        
    def set_y(self,y):
        self.y =y 
        
    def set_low(self,low):
        self.low = int(low)
        
    def set_high(self,high):
        self.high = int(high)
#Function_1    
    def sum_list(self, x):
        return reduce(lambda x, y: x+y,x)

#Function_2
    def max(self, values):
        return reduce(lambda x,y: x if (x>y) else y, values) 

#Function_3
    def min(self, values):
        return reduce(lambda a,b: a if (a<b) else b, values) 

#Function_4
    def add(self, x,y):
        return list(map(lambda x, y: x+y, x,y))

#Function_5
    def is_even(self, values):
        return list(filter(lambda x: x % 2 == 0, values))

#Function_10
    def greater_than_mean(self, values):
        mean = sum(values)/len(values)
        return list(filter(lambda x: x>mean, values))
    
#Function_6
    def cube(self, values):
        return list(map(lambda x: x ** 3, values))
#Function_7
    def mi_km(self, values):
        return list(map(lambda x: x * 1.6093, values))
    
#Function_8
    def C_to_F(self, values):
        return [ ((float(9)/5)*x + 32) for x in values ]
                   
#Function_9
    def fibonacci(self, low, high):                
        a = 0
        if a == low: 
            yield a
        b = 1
        if low <= b <= high: 
            yield b
        counter = 1
        next_in_series = lambda m, n: m + n
        n = next_in_series(a, b)
        while n <= high:
            if low <= n: 
                yield n
            a = b
            b = n
            counter += 1
            n = next_in_series(a, b)
            print(n)
            
                    
