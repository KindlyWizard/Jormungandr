
def AssignClass(CharClass):
  if (CharClass in ClassList):
    CharacterLevel = 1
    AddHitDie(CharClass)
    AddSaves(CharClass)
    AddBaseAttackBonus(CharClass)

def AddClassSkills(CharClass):
   for x in (SkillList):
      if (SkillMatrix[CharClass])[x] == 1:
         CharClassSkills = c(CharSkills, SkillList[x])

def RemoveClass(CharClass):
  if (CharClass in ClassList):
    CharacterLevel = 0
    RemoveHitDie(CharClass)
    RemoveSaves(CharClass)
    RemoveBaseAttackBonus(CharClass)

def RecommendClass():
    if (StatList[which.max(CharStats)] == "Strength"):
        if (CharStats.Constitution >= CharStats.Wisdom):
            "Fighter"
        else: "Barbarian"
    elif (StatList[which.max(CharStats)] == "Dexterity"):
        if (CharStats.Strength >= CharStats.Intelligence):
            "Ranger"
        else:
            "Rogue"
    elif (StatList[which.max(CharStats)] == "Constitution"):
        if (CharStats.Strength >= CharStats.Wisdom):
            "Fighter"
        else:
            "Cleric"
    elif (StatList[which.max(CharStats)] == "Intelligence"):
        if (CharStats.Constitution >= CharStats.Wisdom):
            "Wizard"
        else:
            "Rogue"
    elif (StatList[which.max(CharStats)] == "Wisdom"):
        if (CharStats.Dexterity >= CharStats.Constitution):
            if (CharStats.Wisdom >= CharStats.Strength):
                "Druid"
            else:
                "Monk"
        else:
            "Cleric"
    elif (StatList[which.max(CharStats)] == "Charisma"):
        if (CharStats.Strength >= CharStats.Dexterity):
            "Paladin"
        elif (CharStats.Intelligence >= CharStats.Constitution):
            "Bard"
        else:
            "Sorceror"
    else: "Beats TF out of me!"
        
def AddClassHitDie(CharClass):
   return(ClassMatrix[CharClass, "HitDie"])

def RemoveClassHitDie(CharClass):
    if (CharClass == "Barbarian"):
        pass
    elif (CharClass in (list("Fighter", "Paladin", "Ranger"))):
        pass
    elif (CharClass in (list("Druid", "Cleric", "Bard", "Monk", "Rogue"))):
        pass
    elif (CharClass in (list("Sorceror", "Wizard"))):
        pass