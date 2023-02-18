def FindDescriptionHooks(CharSpecies, CharClass, CharStats, ComputedStatValue):
    if (CharSpecies == "Human"):
        CharacterHooks = AddHook(CharSpecies)

def AddHook(CharSpecies):
    pass

def AddCharStatHook(Stat, SelectedBackgroundNumber):
    CharDescription[SelectedBackgroundNumber] = CharStatHooks[[Stat]][[SelectedBackgroundNumber]]

def InputCharStatHooksFromCSV():
    CharStatHooks = (read.csv(file = "data\\DescriptionMatrix.csv"))
