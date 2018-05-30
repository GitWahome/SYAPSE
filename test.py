from waterLevelGenerator import totalWater
#Pass in the topography samples as a list which contains all the possible topographies.
#I have added one that has a negative elevation to simulate below sea level
#Replace the listed with your set of cases.
myTestCases = [[5,3,2,4,1,2],[5,3,2,4,5,6,1,2,5,6,7,1,2], [0,0,0,0,0], [5,5,5,5,5], [50,0,0,0,50], [1,2,3,4,5], [10, -10, 10]]

for topography in myTestCases:
    totalWater(topography)