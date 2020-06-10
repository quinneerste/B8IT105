# -*- coding: utf-8 -*-

"""
Created on Wed May 27 10:12:49 2020

@author: quinn

"""
class Car(object):
    
    def __init__(self):
        self.__make = ''
        self.__model = ''
        self.__colour = ''
        self.__mileage = 0
        self.__engineSize = ''

    def set_make(self, make):
        self.__make = make

    def get_make(self):
        return self.__make

    def set_model(self, model):
        self.__model = model

    def get_model(self):
        return self.__model

    def set_colour(self, colour):
        self.__colour = colour

    def get_colour(self):
        return self.__colour

    def set_mileage(self, mileage):
        self.__mileage = mileage

    def get_mileage(self):
        return self.__mileage
    
    def distance(self, distance):
        print('Distance ' + str(distance) + 'kms')
        self.__mileage = self.__mileage + distance


class diesel_car(Car):
    # The class definition for a diesel car.
    def __init__(self):
        # Initialise the properties on creation
        Car.__init__(self)
        self.__engine_size = ''

    def get_engine_size(self):
        return self.__engine_size
    
    def set_engine_size(self, engine_size):
        return self.__engine_size
    

class electric_car(Car):
    # The class definition for an electric car.
    def __init__(self):
        # Initialise the properties on creation
        Car.__init__(self)
        self.__number_fuel_cells = 1
    
    def get_number_fuel_cells(self):
        return self.__number_fuel_cells
    
    def set_number_fuel_cells(self, number_fuel_cells):
        self.__number_fuel_cells = number_fuel_cells
#
   
class hybrid_car(Car):
    # The class definition for a hybrid car.
    def __init__(self):
        # Initialise the properties on creation
        Car.__init__(self)
        self.__engine_size = ''
        self.__hybrid_type = ''

    def get_engine_size(self):
        return self.__engine_size
    
    def set_engine_size(self, engine_size):
       self.__engine_size = engine_size

    def get_hybrid_type(self):
        return self.__hybrid_type
    
    def set_hybrid_type(self, hybrid_type):
        self.__hybrid_type = ''
    


class petrol_car(Car):
    # The class definition for a petrol car.
    def __init__(self):#, make, model, colour, asset_tag, engine_size):
        # Initialise the properties on creation
        Car.__init__(self)#, make, model, colour, asset_tag)
        self.__engine_size = ''

    def get_engine_size(self):
        return self.__engine_size
    
    def set_engine_size(self, engine_size):
       self.__engine_size = engine_size

#################################################################
import pandas as pd        
class CarRental(object):

    def __init__(self):
        self.__petrol_cars = []
        self.__electric_cars = []
        self.__diesel_cars = []
        self.__hybrid_cars = []
        for i in range(1,21):
            self.__petrol_cars.append(petrol_car())
        for i in range(1, 7):
            self.__electric_cars.append(electric_car())
        for i in range(1, 11):
            self.__diesel_cars.append(diesel_car())
        for i in range(1, 5):
            self.__hybrid_cars.append(hybrid_car())            

    def get_petrol_cars(self):
        return self.__petrol_cars

    def get_electric_cars(self):
        return self.__electric_cars
    
    def get_hybrid_cars(self):
        return self.__hybrid_cars
    
    def get_diesel_cars(self):
        return self.__diesel_cars
    
    def read_initial_stock_petrol(self):
        stock = pd.read_csv('Car_Stock.csv')
        return stock.at[0,'Initial Stock']
    
    def stock_petrol(self):
        return len(self.get_petrol_cars())
    
    def read_initial_stock_diesel(self):
        stock = pd.read_csv('car_stock.csv')
        return stock.at[1,'Initial Stock']
    
    def stock_diesel(self):
        return len(self.get_diesel_cars())
    
    def read_initial_stock_hybrid(self):
        stock = pd.read_csv('car_stock.csv')
        return stock.at[2,'Initial Stock']
    
    def stock_hybrid(self):
        return len(self.get_hybrid_cars())    

    def read_initial_stock_electric(self):
        stock = pd.read_csv('car_stock.csv')
        return stock.at[3,'Initial Stock']
    
    def stock_electric(self):
        return len(self.get_electric_cars())
    
    def check_stock_rent(self,type):
        if type == 'P':
            return  self.stock_petrol()
        elif type == 'D':
            return  self.stock_diesel()
        elif type == 'H':
            return  self.stock_hybrid()   
        elif type == 'E':
            return  self.stock_electric()
        
    def check_stock_ret(self,type):
        if type == 'P':
            return self.read_initial_stock_petrol() - self.stock_petrol()
        elif type == 'D':
            return self.read_initial_stock_diesel() - self.stock_diesel()
        elif type == 'H':
            return self.read_initial_stock_hybrid() - self.stock_hybrid()   
        elif type == 'E':
            return self.read_initial_stock_electric() - self.stock_electric()        
        
    def check_stock_current(self):
        stock = pd.read_csv('Car_Stock.csv')
        print('Petrol Cars : ', stock.at[0,'Current Stock'])
        print('Diesel Cars : ', stock.at[1,'Current Stock'])
        print('Hybrid Cars : ', stock.at[2,'Current Stock'])
        print('Electric Cars : ', stock.at[3,'Current Stock'])
        
    def store_csv(self):
        df = pd.DataFrame({'Type of car':['Petrol', 'Diesel', 'Hybrid', 'Electric'],
                           'Initial Stock':[20,10,4,6],
                           'Current Stock': [str(len(self.get_petrol_cars())),
                                              str(len(self.get_diesel_cars())),
                                              str(len(self.get_hybrid_cars())),
                                              str(len(self.get_electric_cars()))]})
        df.to_csv('Car_Stock.csv', index = False)
        
    def rent(self, type):
        if type == 'P':
            return self.__petrol_cars.pop()
        elif type == 'D':
            return self.__diesel_cars.pop()
        elif type == 'H':
            return self.__hybrid_cars.pop()        
        elif type == 'E':
            return self.__electric_cars.pop()

    def ret (self, type, Car):
        if type == 'P':
            self.__petrol_cars.append(Car)
        elif type == 'D':
            self.__diesel_cars.append(Car)
        elif type == 'H':
            self.__hybrid_cars.append(Car)
        elif type == 'E':
            self.__electric_cars.append(Car)  

    
    
    
    
    
    
    
    
    
    
    
    
    
