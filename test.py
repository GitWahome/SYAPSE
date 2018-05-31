import random
from waterLevelGenerator import totalWater
#Pass in the topography samples as a list which contains all the possible topographies.
#I have added one that has a negative elevation to simulate below sea level
#Replace the listed with your set of cases.
myTestCases = []
myTestCases = [[5,3,2,4,1,2],[5,3,2,4,5,6,1,2,5,6,7,1,2], [0,0,0,0,0], [5,5,5,5,5], [50,0,10,0,50], [50,0,0,0,50], [1,2,3,4,5], [10, -10, 10]]
#Lowest point on earth: Kola Superdeep borehole: 12262m
#Highest point on earth: Mt Everest: 8848m
#I limited the list size to a max of 100
#I generate 10 test cases
"""
for i in range(10):
    myTestCases.append(random.sample(range(-12262, 8849,1), random.randint(1, 100)))
"""
for topography in myTestCases:
    totalWater(topography)
