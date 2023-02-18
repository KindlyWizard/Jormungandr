def OutputFeatListToCSV():
    import csv
    with open('data\featlist.csv'):
        FeatList

def DisplayFeats():
    print(CharFeats)
    print(paste("Unassigned Feats:", UnassignedFeatPoints))


def AssignFeat(Feat):
    if (UnassignedFeatPoints > 0):
        UnassignedFeatPoints = UnassignedFeatPoints - 1
        CharFeats[[Feat]] = 1
    else:
        print("No unassigned feats!")

def UnassignFeat(Feat):
    CharFeats[[Feat]] = 0
    UnassignedFeatPoints = UnassignedFeatPoints + 1

def AddFeatPoints():
    UnassignedFeatPoints = UnassignedFeatPoints + 1
    if (CharSpecies == "Human"):
        UnassignedFeatPoints = UnassignedFeatPoints + 1
    if (CharClass == "Fighter"):
        UnassignedFeatPoints = UnassignedFeatPoints +1

def DisplayFeats():
    for x in CharFeats:
        if (CharFeats[x] > 0):
            print(unlist((CharFeats[x])))
    print(paste("Unused Feats:", UnassignedFeatPoints))

def RecommendFeats():
    pass