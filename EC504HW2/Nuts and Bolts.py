# AUTHOR1: JacksonHsu jaxhsu@bu.edu

def TEST(x,y):
    if(x == y):
        return "nut fits perfectly"
    elif(x > y):
        return "nut is too big"
    elif(x < y):
        return "nut is too small"

def NutBoltSort(nuts, bolts):

    if(len(nuts) <= 0 or len(bolts) <= 0):
        return [],[]

    firstnut = nuts[0]
    smallerthan_firstnut = []
    nutequalbolt = None
    biggerthan_firstnut = []

    for bolt in bolts:
        if (TEST(firstnut,bolt) == "nut is too big"): #if bolt < firstnut
            smallerthan_firstnut.append(bolt)
        elif (TEST(firstnut,bolt) == "nut is too small"): #if bolt > firstnut
            biggerthan_firstnut.append(bolt)
        else: #if bolt == firstnut
            nutequalbolt = bolt

    firstbolt = nutequalbolt
    smallerthan_firstbolt = []
    biggerthan_firstbolt = []

    for nut in nuts:
        if (TEST(nut, firstbolt) == "nut is too big"): #if nut > firstbolt
            biggerthan_firstbolt.append(nut)
        elif (TEST(nut, firstbolt) == "nut is too small"): #if nut < firstbolt
            smallerthan_firstbolt.append(nut)

    sortednuts = []
    sortedbolts = []

    smaller_nuts, smaller_bolts = NutBoltSort(smallerthan_firstnut, smallerthan_firstbolt)
    if(len(smaller_nuts) > 0):
        for (nutz, boltz) in zip(smaller_nuts, smaller_bolts):
            sortednuts.append(nutz)
            sortedbolts.append(boltz)

    sortednuts.append(firstnut)
    sortedbolts.append(nutequalbolt)

    larger_nuts, larger_bolts = NutBoltSort(biggerthan_firstnut, biggerthan_firstbolt)
    if(len(larger_nuts) > 0):
        for (nutz, boltz) in zip(larger_nuts, larger_bolts):
            sortednuts.append(nutz)
            sortedbolts.append(boltz)

    return sortednuts, sortedbolts

#TEST CODING BELOW

def TESTCASE():
    testnuts = [3, 2, 1, 0, 5, 4]
    testbolts = {4, 3, 1, 2, 0, 5}

    sortednuts, sortedbolts = NutBoltSort(testnuts, testbolts)
    print(sortednuts)
    print(sortedbolts)

import random

def RANDOMTESTCASE():
    testnuts = []
    testbolts = []
    for i in range(0,25):
        testnuts.append(i)
        testbolts.append(i)

    random.shuffle(testnuts)
    random.shuffle(testbolts)

    sortednuts, sortedbolts = NutBoltSort(testnuts, testbolts)
    print(sortednuts)
    print(sortedbolts)


#TESTCASE()
#RANDOMTESTCASE()