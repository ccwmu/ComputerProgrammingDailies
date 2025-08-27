# imports randint function from random module, to generate random integers
from random import randint
# constant list of elements
FORTY_NINERS = ["abc", "xyz", "nmp", "agh", "diufh", "dahj", "dsf"]

def rando_list_elem(array): # function declaration
    index = randint(0, len(array) - 1) # determines random value, from the 1st index of list (0) to last index of list (len-1)
    return array[index] # returns the element at the index

print(rando_list_elem(FORTY_NINERS)) # print statement