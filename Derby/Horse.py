# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 12:19:03 2019

@author: mzamp
"""

class Horse:
    """Horse class object to hold a horse's information"""
    def __init__(self, name, number, rating):
        """Each horse must be given a name number and rating to start."""
        self.name = name
        self.number = number
        self.rating = rating
    def GetName(self):
        return self.name
    def GetNumber(self):
        return self.number
    def GetRating(self):
        return self.rating
    def SetRating(self, x):
        self.rating = x
    
    
    
    def __str__(self):
        horseinfo = ("Name: {name} \nNumber: {number} \nRating: {rating}".format(name = self.GetName(), number = self.GetNumber(), rating = self.GetRating()))
        return horseinfo