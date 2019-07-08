# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 15:35:52 2019
Prompts user to enter values for all the horses racing or load an existing data set.
@author: mzamp
"""

import tkinter as tk

window = tk.Tk()

window.title("GUI INTRO")

# pack is used to show the object in the window with the size it requires
label = tk.Label(window, text = "Hello World!").pack()

#mainloop will display the window until you close it
window.mainloop()

#you are instantiating the Application class by creating a class object called app.
#
#By passing Tk() in, your class inherits the methods from the Tk class, 
#which gives your class the same functionality of the Tk() class (buttons, labels, check boxes, etc.). 
#app = Application(master=Tk())

#class Window(tk.Tk):
#    def __init__(self):
#        super().__init__()
#        self.title("Hello Tkinter")
#
#        self.label = tk.Label(self, text="Choose One")
#        self.label.pack(fill=tk.BOTH, expand=1, padx=100, pady=30)
#
#        hello_button = tk.Button(self, text="Say Hello", command=self.say_hello)
#        hello_button.pack(side=tk.LEFT, padx=(20, 0), pady=(0, 20))
#
#        goodbye_button = tk.Button(self, text="Say Goodbye", command=self.say_goodbye)
#        goodbye_button.pack(side=tk.RIGHT, padx=(0, 20), pady=(0, 20))
#
#    def say_hello(self):
#        self.label.configure(text="Hello World!")
#
#    def say_goodbye(self):
#        self.label.configure(text="Goodbye! \n (Closing in 2 seconds)")
#        self.after(2000, self.destroy)
#
#
#if __name__ == "__main__":
#    window = Window()
#window.mainloop()