'''
Created on Oct 14, 2020

@author: Andrei
'''
class Symbol:
    def __init__(self, name, taipu):
        self.__name = name
        self.__type = taipu
        if self.__type == "char":
            self.__value = ""
        elif self.__type == "bool":
            self.__value = "false"
        else:
            self.__value = 0
        
    def get_name(self):
        return self.__name
    
    def get_type(self):
        return self.__type
    
    def get_value(self):
        return self.__value
    
    def set_value(self, new_value):
        self.__value = new_value
    
    def __eq__(self, other):
        return self.__name == other.get_name()
    
    def __str__(self):
        message = "Symbol name: " + self.__name + "\n"
        message += "Symbol type: " + self.__type + "\n"
        message += "Symbol value: " + str(self.__value) + "\n"
        return message