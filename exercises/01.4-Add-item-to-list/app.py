import random

#Remember import random function here:

my_list = [4,5,734,43,45]

#The magic is here:
arr = []

def addItems():
    for _ in range(10):
        my_list.append(random.randint(0,100))
    print(my_list)
    
addItems()