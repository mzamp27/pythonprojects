# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 20:51:08 2019
Main loop starts the program
@author: mzamp
"""
from inputsanitizer import *
from Horse import *

def GetNumHorses():
    numHorses = Sanitized_Number_Min_Max_Range("How many horses are running this year? ", int, 10, 30)
    return numHorses

def CheckNumHorses():
    n = GetNumHorses()
    prompt = ("You have entered {numHorses} for the number of horses racing this year.\nIf this is correct enter 'y' for YES, if not enter 'n' for NO: ".format(numHorses=n))    
    return ValidateNumber(prompt, n)


finalnum = CheckNumHorses()


if finalnum == True:
    print ("You successfully asked for a number and confirmed it")
else:
    print
