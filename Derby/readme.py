#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 20 11:35:24 2019

@author: mica
"""

""" PROJECT OVERVIEW
KENTUCKY DERBY WEIGHTED HORSE PICKER
This is a simple console program designed to allow the user to
generate various Kentucky derby bets, with random choice, based 
on how they would rate each horse.

The layout of the project should include the following features.

1.  User should be presented with two choices,  the input should
    be an int either 1 or 2.
    *QUIT SHOULD BE A GLOBALLY RECOGNIZED COMMAND DURING ANY INPUT LINE WITH 'q'.
    
        1. New
        2. Load
        
    
2a. 'New' Branch
    Steps: 1. Ask for total number of horses 
            2. Populate Data (Dictionary) Key = Unique Number 
                Minimum of two Values ([Name, Rating])
             3. Direct user to  'picking' interface
                
2b. 'Load' Branch 
    Steps: 1. Load saved dictionary from local storage
            2. Direct user to 'picking' interface

3.  'Picking' interface, should have the user select from the menu
    with a choice from the following menu the input should be an int:
        
    (1. Save), (2. pick 2), (3. pick 3), 
    (4. pick 4.), (5. Change horse rating), (6. Scratch Horse), 
    (7. Print Lineup), (8. OPTIONAL ADD ON), (9. OPTIONAL ADD ON)
    
    3.1 Save Method should save the user's input from the dictionary into local storage
    
    3.2, 3.3, 3.4 Pick Methods should ask for a quantity of picks and return a list
                    of however many picks the user wants
                
    3.5 Ask which horse they would like to reweigh and change the value
    
    3.6 Remove a horse from being in the dictionary
    
    3.7 Return the lineup.
    
    Note: After each input call the user should be returned to the 'picking' menu
    
    

"""