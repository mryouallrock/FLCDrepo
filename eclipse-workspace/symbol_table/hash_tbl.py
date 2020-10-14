'''
Created on Oct 14, 2020

@author: Andrei
'''
from random import randint
from symbol import Symbol

class Hash_table:
    def __init__(self):
        self.__size = 10
        self.__container = {}
        for i in range(0, self.__size):
            self.__container[i] = Symbol("", "")
            
    def hash(self, number):
        return number % self.__size
    
    def is_full(self):
        for i in range(0, self.__size):
            if self.__container[i] == Symbol("", ""):
                return False
        return True
    
    def populated(self, index):
        return self.__container[index] != Symbol("", "")
    
    def exists(self, value):
        for i in range(0, self.__size):
            if self.__container[i].get_name() == value.get_name():
                return True
        return False
    
    def get_position(self, value):
        if self.exists(value):
            for i in self.__container.keys():
                if self.__container[i] == value:
                    return i
        return False
    
    def add(self, elem):
        if self.exists(elem):
            return False
        if self.is_full():
            self.expand_table()
        index = self.hash(randint(0, self.__size))
        while self.__container[index] != Symbol("", ""):
            index = self.hash(randint(0, self.__size))
        self.__container[index] = elem
        
    def set_value(self, symbol, value):
        if self.exists(symbol):
            self.look_up(self.get_position(symbol)).set_value(value)
        return False
        
    def remove(self, index):
        if self.populated(index):
            self.__container[index] = Symbol("", "")
            return True
        return False
    
    def look_up(self, index):
        if self.populated(index):
            return self.__container[index]
        return False
    
    def __str__(self):
        message = ""
        for i in self.__container.keys():
            if self.__container[i] != Symbol("", ""):
                message += "Symbol ID: " + str(i) + "\n" + str(self.__container[i]) + "\n"
        return message
    
    def expand_table(self):
        new_dic = {}
        self.__size *= 2
        for i in range(0, self.__size):
            new_dic[i] = Symbol("", "")
        for i in self.__container.keys():
            self.add(self.__container[i])
        self.__container = new_dic