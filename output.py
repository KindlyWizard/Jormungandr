def ColorStats():
    for x in StatList:
        if (FindMaxStat() == CharStats[x]):
            ColorList[x] = "blue"
        else:
            if (FindMinStat() == CharStats[x]):
                ColorList[x] = "red"
            else:
                ColorList[x] = "black"

def DisplayChar():
    print(CharFullName)
    OutputSpeciesAndClass()
    DisplayStats()
    print(paste("HP:", HitPoints, sep = " "))
    DisplayComputedStats()
    GraphStats()
    DisplaySkills()
    DisplayFeats()
    DisplayVitalStats(Age, Weight, Height)
    DisplayCharMoney(CharMoney, CharMainTitle, CharFirstName)
    #DisplayDescription()

def DisplayDescription():
    print(CharDescription)

def OutputSpecies():
    print(trimws(CharSpecies))

def OutputSpeciesAndClass():
    print(paste(CharSpecies, CharClass))

def GraphStats():
    ColorStats()
    barplot((CharStats)
    , names = substr(StatList, 1, 3)
    , col = unlist(ColorList))

def StatColors():
  MaxStats = max(unlist(CharStats))

def DisplayVitalStats(Age, Weight, Height):
    print("Age:" + (Age))
    print("Weight(lb):" + Weight)
    CalculateHeightInFeetAndInches(Height)
    print(paste("Height(in):", Feet, "feet,", Inches, "inches"))

def DisplayCharMoney(CharMoney, CharMainTitle, CharFirstName):
    print(GenerateMoneyString(CharMoney, CharMainTitle, CharFirstName))

def CalculateHeightInFeetAndInches(Height):
    Feet = floor(Height / 12)
    Inches = Height - (Feet * 12)