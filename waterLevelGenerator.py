#This goes through the troughs that are generated and  finds the amount of water that they can hold.
#I observed a formula where given that the bounds of the troughs are the maximums, water cant be above the minimum of the two heights:
#I then go through the height difference of the rocks and the tallest rock we have. This gives me the maximum water table it can hold.
# I also subtract the bound difference water to ensure I get that off since it cant be held.
#This can also be achieved by just subtrscting the rock height from the minimum of the bounds but getting
# the boundDifference feels more intuitive.
def waterInTroughs(troughs):
    waterLevel = 0
    for trough in troughs:
        boundDifferences = abs(trough[0]-trough[-1])
        for rocks in trough:
            water = max(trough)-rocks - boundDifferences
            if water>0:
                waterLevel += water
    return waterLevel
#I used this to generate 'trough' which can trap water. This basically looks for down gradients appending them to a list.
#Should an up gradient be found, another invariant takes over and keeps track of whether a drop is detected.
#The values keep getting appended and this creates a trough. When a drop is detected the trough is done, a new one is initiated
def troughsGenerator(topography):
    i = 1
    trough = [topography[0]]
    allTroughs =[]
    while i< len(topography)-1:
        if topography[i]<topography[i-1]:
            trough.append(topography[i])
        elif topography[i + 1] >= topography[i]:
            trough.append(topography[i])
        else:
            trough.append(topography[i])
            allTroughs.append(trough)
            trough=[topography[i]]
        i += 1
    trough.append(topography[-1])
    allTroughs.append(trough)
    return allTroughs
def totalWater(testCase):
    print("Topography: {} \n water levels: {} \n\n".format(testCase, waterInTroughs(troughsGenerator(testCase))))
