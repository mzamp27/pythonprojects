#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  3 10:44:16 2019
Picker Interface Switch Dictionary
@author: mica
"""
class PickingInterface(object):
    def number_1(self):
        print("save data")
        
    def number_2(self):
        print ("call exacta method")
   
        
    
    
    def numbersToMethods(self, argument):
        method_name = 'number_' + str(argument)
        method = getattr(self, method_name)        
        return method()
