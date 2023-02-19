def AddBaseAttackBonus(CharClass):
  if (CharClass in ["Barbarian", "Fighter", "Paladin", "Ranger"]):
    ComputedStatValue.BaseAttackBonus = ComputedStatValue.BaseAttackBonus + 1

def AddSaves(CharClass):
    if (CharClass == "Barbarian"):
        ComputedStatValue.ReflexSave = (ComputedStatValue.ReflexSave + 2)
    if (CharClass == "Bard"):
        ComputedStatValue.ReflexSave = (ComputedStatValue.ReflexSave + 2)
        ComputedStatValue.WillSave = (ComputedStatValue.WillSave + 2)
    elif (CharClass == "Cleric"):
        ComputedStatValue.ChildProcessErrorFortitudeSave = (ComputedStatValue.FortitudeSave + 2)
        ComputedStatValue.WillSave = (ComputedStatValue.WillSave + 2)
    elif (CharClass == "Druid"):
        ComputedStatValue.FortitudeSave = (ComputedStatValue.FortitudeSave + 2)
        ComputedStatValue.WillSave = (ComputedStatValue.WillSave + 2)
    elif (CharClass == "Fighter"):
        ComputedStatValue.FortitudeSave = (ComputedStatValue.FortitudeSave + 2)
    elif (CharClass == "Monk"):
      ComputedStatValue.ReflexSave = (ComputedStatValue.ReflexSave + 2)
      ComputedStatValue.FortitudeSave = (ComputedStatValue.FortitudeSave + 2)
      ComputedStatValue.WillSave = (ComputedStatValue.WillSave + 2)
    else:
      if (CharClass == "Paladin"):
        ComputedStatValue.FortitudeSave = (ComputedStatValue.FortitudeSave + 2)
        ComputedStatValue.WillSave = (ComputedStatValue.WillSave + 2)
      else:
        if (CharClass == "Ranger"):
          ComputedStatValue.FortitudeSave = (ComputedStatValue.FortitudeSave + 2)
          ComputedStatValue.ReflexSave = (ComputedStatValue.ReflexSave + 2)
        else:
          if (CharClass == "Rogue"):
            ComputedStatValue.ReflexSave = (ComputedStatValue.ReflexSave + 2)
          else:
            if (CharClass == "Sorceror"):
              ComputedStatValue.WillSave = (ComputedStatValue.WillSave + 2)
            else:
              if (CharClass == "Wizard"):
                ComputedStatValue.WillSave = (ComputedStatValue.WillSave + 2)

def CalculateBaseAttackBonus():
  ComputedStatValue.BaseAttackBonus = ComputedStatValue.StrengthBonus

def CalculateFortitudeSave():
  ComputedStatValue.FortitudeSave = ComputedStatValue.ConstitutionBonus

def CalculateInitiativeBonus():
  ComputedStatValue.InitiativeBonus = ComputedStatValue.DexerityBonus

def CalculateReflexSave():
  ComputedStatValue.ReflexSave = ComputedStatValue.DexterityBonus

def CalculateWillSave():
  ComputedStatValue.WillSave = ComputedStatValue.WisdomBonus

def ComputeBaseStatBonus(CharStat):
  floor(((ReturnStatValue(ReturnStatIndex(CharStat))) / 2) - 5)

def ComputeOtherStats(ComputedStat):
  if (ComputedStat == "FortitudeSave"):
    CalculateFortitudeSave()
  elif (ComputedStat == "ReflexSave"):
    CalculateReflexSave()
  elif (ComputedStat == "WillSave"):
    CalculateWillSave()
  elif (ComputedStat == "InitiativeBonus"):
    CalculateInitiativeBonus()
  elif (ComputedStat == "BaseAttackBonus"):
    CalculateBaseAttackBonus()

def ComputeStat(ComputedStat):
  if (ComputedStat in BaseComputedStatList):
    ComputedStatValue.ComputedStat = ComputeBaseStatBonus(ComputedStat)
  else:
    ComputeOtherStats(ComputedStat)

def ComputeStats(CharStats):
  for x in ComputedStatList:
    ComputedStatValue[x] = ComputeStat(unlist(ComputedStatList[x]))

def DamageBonus():
  ReturnComputedStatValue("StrengthBonus")

def DisplayComputedStats():
  for x in ComputedStatList:
    print(ComputedStatList[x], ComputedStatValue[x], sep = " ")

def DisplayStats():
  for x in StatList:
    print(StatList[x], CharStats[x])

def RemoveBaseAttackBonus(CharClass):
  if CharClass in ["Barbarian", "Fighter", "Paladin", "Ranger"]:
    ComputedStatValue.BaseAttackBonus = ComputedStatValue.BaseAttackBonus - 1

def RemoveSaves(CharClass):
  if (CharClass == "Barbarian"):
    ComputedStatValue.ReflexSave = (ComputedStatValue.ReflexSave - 2)
  elif (CharClass == "Bard"):
      ComputedStatValue.ReflexSave = (ComputedStatValue.ReflexSave - 2)
      ComputedStatValue.WillSave = (ComputedStatValue.WillSave - 2)
  elif (CharClass == "Cleric"):
    ComputedStatValue.FortitudeSave = (ComputedStatValue.FortitudeSave - 2)
    ComputedStatValue.WillSave = (ComputedStatValue.WillSave - 2)
  elif (CharClass == "Druid"):
    ComputedStatValue.FortitudeSave = (ComputedStatValue.FortitudeSave - 2)
    ComputedStatValue.WillSave = (ComputedStatValue.WillSave - 2)
  elif (CharClass == "Fighter"):
    ComputedStatValue.FortitudeSave = (ComputedStatValue.FortitudeSave - 2)
  elif (CharClass == "Monk"):
    ComputedStatValue.ReflexSave = (ComputedStatValue.ReflexSave - 2)
    ComputedStatValue.FortitudeSave = (ComputedStatValue.FortitudeSave - 2)
    ComputedStatValue.WillSave = (ComputedStatValue.WillSave - 2)
  elif (CharClass == "Paladin"):
    ComputedStatValue.FortitudeSave = (ComputedStatValue.FortitudeSave - 2)
    ComputedStatValue.WillSave = (ComputedStatValue.WillSave - 2)
  elif (CharClass == "Ranger"):
    ComputedStatValue.FortitudeSave = (ComputedStatValue.FortitudeSave - 2)
    ComputedStatValue.ReflexSave = (ComputedStatValue.ReflexSave - 2)
  elif (CharClass == "Rogue"):
    ComputedStatValue.ReflexSave = (ComputedStatValue.ReflexSave - 2)
  elif (CharClass == "Sorceror"):
    ComputedStatValue.WillSave = (ComputedStatValue.WillSave - 2)
  elif (CharClass == "Wizard"):
    ComputedStatValue.WillSave = (ComputedStatValue.WillSave - 2)