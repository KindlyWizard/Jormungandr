def AddSkillPoints(CharClass):
    UnusedSkillPoints = ComputedStatValue.IntelligenceBonus + ClassMatrix[CharClass, "BaseSkillPoints"]
    if (CharSpecies == "Human"):
        UnusedSkillPoints = UnusedSkillPoints + 1

def AddSkillPoint(SelectedSkill):
    if (UnusedSkillPoints > 0):
        UnusedSkillPoints = UnusedSkillPoints - 1
        CharSkills[[SelectedSkill]] = CharSkills[[SelectedSkill]] + 1
    else:
        print("Error: No Unspent Skill Points Remaining")

def RemoveSkillPoints(SelectedSkill):
    if (CharSkills[[SelectedSkill]]) > 0:
        UnusedSkillPoints = UnusedSkillPoints + 1
        CharSkills[[SelectedSkill]] = CharSkills[[SelectedSkill]] - 1
    else:
        print("Error: No Skill Points Remaining In Skill")

def AssignCharSkills():
    for x in (SkillMatrix["Skill"]):
        #list(CharSkills) = c(CharSkills, SkillMatrix[x])
        pass

def OutputSkillListToCSV():
    import csv
    with open('data\SkillList.csv'):
        FeatList
  
def DisplaySkills():
        #print(CharSkills)
    print("Unused Skill Points:" + UnusedSkillPoints)

def RecommendSkills(CharSkills, CharClassSkills):
    pass
#sample(CharClassSkills, UnusedSkillPoints)

def GenerateSkillListFromMatrix():
    pass

def AssignSkillPoint():
    pass