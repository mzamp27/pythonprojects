#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  1 18:07:04 2019
Picking number methods
@author: mica
"""
import random 

def Exacta(basket):
    #pick 2 numbers at random that aren't repeated from the basket
    pick = []
    
    for i in range(2):
        while True:
            temppick = random.choice(basket)
            if temppick in pick:
                continue
            else:
                pick.append(temppick)
                break
    return pick
    
    
def Trifecta(basket):
    #pick 3 numbers at random that aren't repeated from the basket
    pick = []
    
    for i in range(3):
        while True:
            temppick = random.choice(basket)
            if temppick in pick:
                continue
            else:
                pick.append(temppick)
                break
    return pick


def Superfecta(basket):
    #pick 4 numbers at random that aren't repeated from the basket
    pick = []
    
    for i in range(4):
        while True:
            temppick = random.choice(basket)
            if temppick in pick:
                continue
            else:
                pick.append(temppick)
                break
    return pick

def multiExacta(basket, n):
    #pick 2 numbers n times and return a list
    
    picklist = []
    
    for i in range(n):
        pick = []
        
        for i in range(2):
            while True:
                temppick = random.choice(basket)
                if temppick in pick:
                    continue
                else:
                    pick.append(temppick)
                    break
        picklist.append(pick)
    return picklist
    
    
def multiTrifecta(basket, n):
    #pick 2 numbers n times and return a list
    
    picklist = []
    
    for i in range(n):
        pick = []
        
        for i in range(3):
            while True:
                temppick = random.choice(basket)
                if temppick in pick:
                    continue
                else:
                    pick.append(temppick)
                    break
        picklist.append(pick)
    return picklist
    
def multiSuperfecta(basket, n):
    #pick 2 numbers n times and return a list
    
    picklist = []
    
    for i in range(n):
        pick = []
        
        for i in range(4):
            while True:
                temppick = random.choice(basket)
                if temppick in pick:
                    continue
                else:
                    pick.append(temppick)
                    break
        picklist.append(pick)
    return picklist
    