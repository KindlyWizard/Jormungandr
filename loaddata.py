def LoadAllCSVs():
    InputBaseStatsFromCSV()
    InputSpeciesListFromCSV()
    InputClassListFromCSV()
    InputBaseComputedStatListFromCSV()
    InputComputedStatListFromCSV()
    InputSkillListFromCSV()
    InputSkillMatrixFromCSV()
    InputFeatListFromCSV()
    InputFirstNamesFromCSV()
    InputLastNamesFromCSV()
    InputFantasyFirstNamesFromCSV()
    InputFantasyLastNamesFromCSV()
    InputFantasyNickNamesFromCSV()
    InputMainTitlesFromCSV()
    InputEndTitlesFromCSV()
    InputDescriptionMatrixFromCSV()
    InputCharacterDataFromCSV()
    InputBaseStatsMatrixFromCSV()
    InputClassMatrixFromCSV()

def InputSpecifiedCSV(modulecsv, headers): #does not work yet, do not use
    modulecsv = read.csv(file = paste("data\\", Module, ".csv", sep = "", header = headers))

def InputDescriptionMatrixFromCSV():
    DescriptionMatrix = read.csv(file = "data\\DescriptionMatrix.csv", header = FALSE)

def InputCharacterDataFromCSV():
    CharacterData = read.csv(file = "data\\CharacterData.csv", header = FALSE)

def InputBaseStatsMatrixFromCSV():
    BaseStatsMatrix = read.csv(file = "data\\BaseStatsMatrix.csv", header = FALSE)

def InputFantasyLastNamesFromCSV():
  FantasyLastNames = read.csv(file = "data\\FantasyLastNames.csv")

def InputFantasyNickNamesFromCSV():
  FantasyNickNames = read.csv(file = "data\\FantasyNickNames.csv", header = FALSE)

def InputFirstNamesFromCSV():
  FirstNames = read.csv(file = "data\\FirstNames.csv", header = FALSE)

def InputLastNamesFromCSV():
  LastNames = read.csv(file = "data\\LastNames.csv", header = FALSE)

def InputFantasyFirstNamesFromCSV():
  FantasyFirstNames = read.csv(file = "data\\FantasyFirstNames.csv")

def InputMainTitlesFromCSV():
  FantasyMainTitles = read.csv(file = "data\\FantasyMainTitles.csv", header = FALSE)

def InputEndTitlesFromCSV():
  FantasyEndTitles = read.csv(file = "data\\FantasyEndTitles.csv", header = FALSE)

def InputBaseStatsFromCSV():
    StatList = read.csv(file = "data\\BaseStats.csv", header = TRUE)

def InputSpeciesListFromCSV():
    SpeciesList = read.csv(file = "data\\SpeciesList.csv")

def InputClassListFromCSV():
    ClassList = read.csv(file = "data\\ClassList.csv", header = FALSE)

def InputClassMatrixFromCSV():
  ClassMatrix = read.csv(file = "data\\ClassMatrix.csv")

def InputComputedStatListFromCSV():
    ComputedStatList = read.csv(file = "data\\ComputedStatList.csv")

def InputBaseComputedStatListFromCSV():
    BaseComputedStatList = read.csv(file = "data\\BaseComputedStatList.csv")

def InputSkillListFromCSV():
    SkillList = read.csv(file = "data\\SkillList.csv")

def InputSkillMatrixFromCSV():
      SkillMatrix = read.csv(file = "data\\SkillMatrix.csv")

def InputFeatListFromCSV():
    FeatList = read.csv(file = "data\\FeatList.csv", header = FALSE)