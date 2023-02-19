def InitializeData():
    pass
ValidDieSize = list(4, 6, 8, 10, 12, 20, 100)
CharStats = list(0, 0, 0, 0, 0, 0)
ColorList = list("", "", "", "", "", "")
TargetDummyAC = 10
TempDice = 0
TotalRolled = 0
CharClass = "Monk"
AttackLog = list(0, 0)
ComputedStatValue =- list(0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)
HitPoints = 0
CharacterLevel = 1
UnusedSkillPoints = 0
CharSpecies = "Human"
CharFullName = "Jane Doe"
FirstNames = NULL
FantasyFirstNames = NULL
LastNames = NULL
FantasyEndTitles = NULL
FantasyNickNames = NULL
FantasyMainTitles = NULL
NameComponents = ["FantasyMainTitles", "FirstNames", "FantasyNickNames", "LastNames", "FantasyEndTitles"]
BaseSkillPoints = list(4, 6, 2, 4, 2, 4, 2, 6, 8, 2, 2)
CharSkills = list(0)
CharFeats = list(0)
UnassignedFeatPoints = 0
StartingWealthList = list(3, 3, 4, 2, 5, 1, 5, 5, 4, 2, 2)
CharMoney = 0
CharStatHook = NULL
CharDescription = NULL
ClassList = list("")
ClassMatrix = matrix()

import csv
source("loaddata.r")
LoadAllCSVs()
InitializeData()
source("names.r")
source("classes.r")
source("species.r")
source("output.r")
source("basestats.r")
source("computedstats.r")
source("attack.r")
source("defaults.r")
source("diceroller.r")
source("skills.r")
source("feats.r")
source("vitalstats.r")
source("money.r")
source("description.r")
source("AIDescription.r")
InitializeData()


ClassHitDice = (12, 8, 8, 8, 10, 8, 10, 10, 8, 6, 6)

def AddHitDie(CharClass):
    HitPoints = AddClassHitDie(CharClass) + ComputedStatValue.ConstitutionBonus

def ClearData():
  UnassignedFeatPoints = 0

def CharGen(Genre = "Fantasy", Game = "DandD", Method = "4d6droplow"):
  ClearData()
  GenerateName()
  AssignSpecies()
  GenerateStats(Game, Method)
  CharClass = RecommendClass()
  ComputeStats(CharStats)
  AssignClass(CharClass)
  AddSkillPoints(CharClass)
  AddFeatPoints()
  AssignVitalStats(CharSpecies, CharClass)
  GenerateWealth(CharClass)
  FindDescriptionHooks(CharSpecies, CharClass, CharStats, ComputedStatValue)
  #GenerateAIDescription(CharSpecies, CharClass, CharFullName)
  DisplayChar()
  Attack(Swings = 100)
  #DisplayAttackLog()
  #SaveChar()

def FindMaxStat(CharStats):
    max(unlist(CharStats))

def FindNthBestStat(): #not working, do not use until fixed.
    maxN = function(CharStats, N = 5)
    len = length(CharStats)
    if (N > len):
        warning("N greater than length(x).  Setting N=length(x)")
        N = length(CharStats)
        sort(CharStats, partial = len - N + 1)[len - N + 1]
        #maxN(1:10)

def FindMinStat():
    min(unlist(CharStats))

# LoadSkillsFromCSV = function() {
#}

#GenerateSkills = function(CharStats) {
#}

def LoadChar(CharFile):
  load(CharFile)
  DisplayChar()

def ReturnComputedStatIndex(ComputedStat):
    which(ComputedStatList == ComputedStat)

def ReturnComputedStatValue(ComputedStat):
    ComputedStatValue[which(ComputedStatList == ComputedStat)]

def ReturnComputedStatDescription(ComputedStat):
    return(ComputedStatList[which(ComputedStatList == ComputedStat)])

def ReturnStatDescription(StatIndex):
    return(StatList[StatIndex])

def ReturnStatIndex(StatToIndex):
    which(StatToIndex == ComputedStatList)

def ReturnStatValue(StatIndex):
    return(CharStats[StatIndex])

def SaveChar():
    save(CharacterData, file = paste(CharFullName, ".rds", sep = ""))

def OutputData():
    pass