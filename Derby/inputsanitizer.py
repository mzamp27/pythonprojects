# -*- coding: utf-8 -*-
"""
Created on Sat Jul  6 15:14:46 2019
Input Sanitizer Methods
@author: mzamp
"""


#generalized number sanitization method
def Sanitized_Number_Min_Max_Range(prompt, type_ = None, min_ = None, max_ = None, range_= None):
    #CHECK INPUT PARAMETERS FIRST
    if type_ != None and type_ != int and type_ != float:
        raise ValueError("type parameter needs to be int or float")
    
    if min_ != None and max_ != None and max_ < min_:
        raise ValueError("min_ must be less than or equal to max_.")
    
    #range is trickier to check come back later
       
    #Get user input and test against parameters
    while True:
        userInput = input(prompt)
        
        #check type matches given type
        if type_ != None:
            try:
                userInput = type_(userInput)
            except ValueError:
                print ("Input type must be {0}.".format(type_.__name__))
                continue
            
        #check if input meets max and min requirements
        if max_ != None and userInput > max_:
            print("Input must be less than or equal to {0}.".format(max_))
        elif min_ != None and userInput < min_:
            print("Input must be greater than or equal to {0}.".format(min_))
        
        #check if input is in range not sure how this works yet
        elif range_ != None and userInput not in range_:
            if isinstance(range_, range):
                template = "Input must be between {0.start} and {0.stop}."
                print(template.format(range_))
            else:
                template = "Input must be {0}."
                if len(range_) == 1:
                    print(template.format(*range_))
                else:
                    print(template.format(" or ".join((", ".join(map(str,
                                                                     range_[:-1])),
                                                       str(range_[-1])))))
        else:
            return userInput   
        



def ValidateNumber(prompt, n):
    while True:
        try:
            confirm = input(prompt)
            if confirm == 'y':
                return True
            elif confirm == 'n':
                return False
            else:
                print ("Invalid entry please try again")
                continue
        except:
            print ("Something went wrong")
            continue
        
            
 

class Color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'



           



