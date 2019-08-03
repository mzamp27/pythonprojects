# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 20:51:08 2019
Main loop starts the program
@author: mzamp
"""
from inputsanitizer import *
from Horse import *
import pprint
from pickermethods import *
from pickerinterface import *

#The next 3 methods are for getting the number of horses racing
def GetNumHorses():
    numHorses = Sanitized_Number_Min_Max_Range("How many horses are running this year? ", int, 3, 30)
    return numHorses

def CheckNumHorses(numHorses):
    n = numHorses
    prompt = ("You have entered {numHorses} for the number of horses racing this year.\nIf this is correct enter 'y' for YES, if not enter 'n' for NO: ".format(numHorses=n))    
    return ValidateNumber(prompt, n)

def VerifiedNumHorses():    
    while True: 
        numHorses = GetNumHorses()
        if (CheckNumHorses(numHorses) == True):
            print ("You successfully asked for a number and confirmed it")
            return numHorses
        else:
            continue


#once number of horses is determined allow user to enter the data of each horse
def PopHorseDict(n):
    horseDict = {}
    numHorses = n
    #add horse to list if 
    for i in range (numHorses):
        uniqueNum = Sanitized_Number_Min_Max_Range("Please enter the horse's position number? ", int, 1, 30)
        while True:
            if uniqueNum in horseDict.keys():
                print ("That horse number already exists")
                uniqueNum = Sanitized_Number_Min_Max_Range("Please enter the horse's position number? ", int, 1, 30)
                continue    
            else:
                break
        horseName = input("Please enter the horse's name")
        horseRating = Sanitized_Number_Min_Max_Range("Please enter the horse's rating betwee 1 and 10? ", int, 1, 10)
        
        #At this point we create an instance of the horse class and add it to the dictionary?
        #H1 = Horse(horseName, uniqueNum, horseRating)
        #D1 = {H1.GetNumber: [H1.GetName, H1.GetRating]}
        D1 = {uniqueNum: [horseName, horseRating]}
        horseDict.update(D1)
    return horseDict

#after dict is populated give user a chance to review it and make changes keeping original
#dict stored in a variable in main loop
def ReviewDict(racerDict_in):
    tempDict = racerDict_in
    print ("Here is your lineup!")
    print (Color.UNDERLINE + "#" + Color.END + " - " + Color.UNDERLINE + "[Name, Rating]" + Color.END)
    for k, v in tempDict.items():
        print (k, " - " , v)

    #not yet implemented make changes to dict then return it
    return tempDict


def WeightedList(racerDict_in):
    racers = racerDict_in
    weightlist = []
    
    for key in racers:
        weight = racers[key][1]
        for i in range(weight):
            weightlist.append(key)
    return weightlist

def DisplayPickerInterface():
    print ("Lets Pick Some Winners!")
    PI = PickingInterface()
    while True:
        print ("Please choose from the following menu:")
        print ("""(1. Save), (2. pick 2), (3. pick 3), 
        (4. pick 4.), (5. Change horse rating), (6. Scratch Horse), 
        (7. Print Lineup), (8. OPTIONAL ADD ON), (9. OPTIONAL ADD ON)""")
        userChoice = Sanitized_Number_Min_Max_Range(": ", int, 1, 10)
        if userChoice == 9:
            break
        PI.numbersToMethods(userChoice)

def Main():
    #numHorses = VerifiedNumHorses()
    #racerDictUNV = PopHorseDict(numHorses)
    #reviewedVER = ReviewDict(racerDictUNV)
    #weightlist = WeightedList(reviewedVER)
    DisplayPickerInterface()
    #exactapick = Exacta(weightlist)
    #print (exactapick)
    

testDict = {1: ["Jim", 5], 2: ["Tim", 4], 3: ["Mike", 8]}

Main()


