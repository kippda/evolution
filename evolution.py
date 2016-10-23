from random import *

def mating(mom, dad):
    """
    takes two lists, averages the values in them and adds slight random element
    """
    child = [int((mom[val]+dad[val])/2)+randint(-2,2) for val in range(len(mom))]
    return child

def mixup(lst):
    """
    mixes up lst
    """
    newList = []
    ct = len(lst)-1
    for num in range(len(lst)):
        newList.append(lst.pop(randint(0,ct)))
        ct -= 1
    return newList

def pairOff(lst):
    """
    mixes up lst then uses mating to make newList
    """
    lst = mixup(lst)
    newList = []
    for creature in range(0, len(lst), 2):
        newList.append(mating(lst[creature],lst[creature+1]))
        newList.append(mating(lst[creature],lst[creature+1]))
    return newList
        

#create 10 'creatures' with midrange RGB values
#edenList = [[randint(120,135) for num in range(3)] for num in range(10)]

#simpler version with only 1 value for test purposes
edenList = [[randint(120,135)] for num in range(10)]

print(edenList)
nextGen = pairOff(edenList)
