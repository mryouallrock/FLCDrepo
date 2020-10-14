'''
Created on Oct 14, 2020

@author: Andrei
'''
from symbol import Symbol

class Symbol_table:
    def __init__(self, hash_t):
        self.__hash_t = hash_t
        
    def add_symbol(self, name, taipu):
        new_sym = Symbol(name, taipu)
        if self.__hash_t.exists(new_sym):
            return False
        self.__hash_t.add(new_sym)
        return True
    
    def assign_value(self, name, value):
        find_sym = Symbol(name, "")
        if self.__hash_t.exists(find_sym):
            return False
        self.__hash_t.set_value(find_sym, value)
        return True
    
    def remove_symbol(self, name):
        sym = Symbol(name, "")
        if self.__hash_t.exists(sym):
            self.__hash_t.remove(self.__hash_t.get_position(sym))
            return True
        return False
    
    def look_up(self, name):
        sym = Symbol(name, "")
        if self.__hash_t.exists(sym):
            return [self.__hash_t.look_up(self.__hash_t.get_position(sym)).get_type(), self.__hash_t.look_up(self.__hash_t.get_position(sym)).get_value()]
        return False
    
    def __str__(self):
        return str(self.__hash_t)