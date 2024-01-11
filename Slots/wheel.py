import random
from tkinter import *

class Wheel:
    
    def spin(self):
    #returns a random number from the wheel
        num = random.randint(1, 3)
        if num == 1:
            return 1
        if num == 2 : 
            return 2
        if num == 3 :
            return 3     