from random import *



#create 10 'creatures' with midrange RGB values
edenList = [[randint(120,135) for num in range(3)] for num in range(10)]

print(edenList)
for creature in range(0,len(edenList),2):
    print(edenList[creature])
