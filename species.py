def AddSpeciesBonus(Stat, Bonus = 0):
    for x in StatList:
        if (Stat == (StatList[x])):
            CharStats[x] = CharStats[x] + Bonus

def AdjustStatsSpecies(CharSpecies = "Human"):
    if CharSpecies == "Dwarf":
        AddSpeciesBonus("Constitution", 2)
        AddSpeciesBonus("Wisdom", 2)
        AddSpeciesBonus("Charisma", -2)

    if (CharSpecies == "Elf"):
        AddSpeciesBonus("Dexterity", 2)
        AddSpeciesBonus("Intelligence", 2)
        AddSpeciesBonus("Constitution", -2)

    if (CharSpecies == "Gnome"):
        AddSpeciesBonus("Constitution", 2)
        AddSpeciesBonus("Charisma", 2)
        AddSpeciesBonus("Strength", -2)

    if (CharSpecies == "Half-Elf"):
        AddSpeciesBonus(StatList[which.max(CharStats)], 2)

    if (CharSpecies == "Half-Orc"):
        AddSpeciesBonus(StatList[which.max(CharStats)], 2)

    if (CharSpecies == "Halfling"):
        AddSpeciesBonus("Dexterity", 2)
        AddSpeciesBonus("Charisma", 2)
        AddSpeciesBonus("Strength", -2)

    if (CharSpecies == "Human"):
        AddSpeciesBonus(StatList[which.max(CharStats)], 2)

def AssignSpecies(Game = "Pathfinder"):
    if (Game == "Pathfinder"):
        CharSpecies = sample(SpeciesList, 1)
        AdjustStatsSpecies(CharSpecies)

def RemoveStatsSpecies(CharSpecies = "Human"):
    if (CharSpecies == "Dwarf"):
        AddSpeciesBonus("Constitution", -2)
        AddSpeciesBonus("Wisdom", -2)
        AddSpeciesBonus("Charisma", 2)

    if (CharSpecies == "Elf"):
        AddSpeciesBonus("Dexterity", -2)
        AddSpeciesBonus("Intelligence", -2)
        AddSpeciesBonus("Constitution", 2)

    if (CharSpecies == "Gnome"):
        AddSpeciesBonus("Constitution", -2)
        AddSpeciesBonus("Charisma", -2)
        AddSpeciesBonus("Strength", 2)

    if (CharSpecies == "Half-Elf"):
        AddSpeciesBonus(StatList[which.max(CharStats)], -2)

    if (CharSpecies == "Half-Orc"):
        AddSpeciesBonus(StatList[which.max(CharStats)], -2)

    if (CharSpecies == "Halfling"):
        AddSpeciesBonus("Dexterity", -2)
        AddSpeciesBonus("Charisma", -2)
        AddSpeciesBonus("Strength", 2)

    if (CharSpecies == "Human"):
        AddSpeciesBonus(StatList[which.max(CharStats)], -2)