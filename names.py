NameComponents = ["FantasyMainTitles", "FirstNames", "FantasyNickNames", "LastNames", "FantasyEndTitles"]
FirstNames = NULL
LastNames = NULL
FantasyEndTitles = NULL
FantasyNickNames = NULL
FantasyMainTitles = NULL


def InitializeData():
  InputFirstNamesFromCSV()
  InputLastNamesFromCSV()
  InputFantasyNickNamesFromCSV()
  InputMainTitlesFromCSV()
  InputEndTitlesFromCSV()
  InputFantasyFirstNamesFromCSV()
  InputFantasyLastNamesFromCSV()

def OutputData():
  OutputFirstNamesToCSV()
  OutputLastNamesToCSV()
  OutputFantasyNickNamesToCSV()
  OutputMainTitlesToCSV()
  OutputEndTitlesToCSV()

def InitializeData2():
  NameComponents = matrix(length)
  NameComponents = read.csv(file = "data\\NameLists.csv")

def OutputData2():
  write.table(NameComponents
  , file = "data\\NameLists.csv")

def GenerateName(Genre = "Fantasy"):
  if (Genre == "Fantasy"):
    CharFullname = gsub("  ", " ", trimws(paste(PickMainTitle("Fantasy")
    , PickFirstName("Fantasy")
    , PickNickName("Fantasy")
    , PickLastName("Fantasy")
    , PickEndTitle("Fantasy"))), fixed = TRUE)

def OutputMainTitlesToCSV():
  write.table(unlist(FantasyMainTitles)
  , file = "data\\FantasyMainTitles.csv")

def OutputEndTitlesToCSV():
  write.table(unlist(FantasyEndTitles)
  , file = "data\\FantasyEndTitles.csv")

def OutputFantasyNickNamesToCSV():
  write.table(unlist(FantasyNickNames)
  , file = "data\\FantasyNickNames.csv")

def OutputFantasyLastNamesToCSV():
  write.table(unlist(FantasyLastNames)
  , file = "data\\FantasyLastNames.csv")

def OutputFirstNamesToCSV():
  write.table(unlist(FirstNames)
  , file = "data\\FirstNames.csv")

def OutputLastNamesToCSV():
  write.table(unlist(LastNames)
  , file = "data\\LastNames.csv")

def PickFantasyFirstName():
  CharFirstName = FantasyFirstNames[(sample(seq_along(FantasyFirstNames), 1))]

def PickFantasyLastName():
  CharLastName = FantasyLastNames[(sample(seq_along(FantasyLastNames), 1))]

def PickEndTitle(Genre = "Fantasy"):
  if (Genre == "Fantasy"):
    (PickFantasyEndTitle())

def PickFantasyMainTitle(CharMainTitle = ""):
  if (RollDice(10) == 1):
    CharMainTitle = FantasyMainTitles[(sample(seq_along(FantasyMainTitles), 1))]
  else:
    CharMainTitle = NULL

def PickFantasyNickName():
  if (RollDice(10) == 1):
    CharNickName = trimws(paste("'"
    , (FantasyNickNames[(sample(seq_along(FantasyNickNames), 1))])
    , "'"
    , sep = ""))

def PickFantasyEndTitle():
  if (RollDice(10) == 1):
    CharEndTitle = trimws(paste("'"
    , (FantasyEndTitles[(sample(seq_along(FantasyEndTitles), 1))])
    , "'"
    , sep = ""))

def PickFirstName(Genre = "Fantasy"):
  if (Genre == "Fantasy"):
    PickFantasyFirstName()

def PickLastName(Genre = "Fantasy"):
  if (Genre == "Fantasy"):
    PickFantasyLastName()

def PickMainTitle(Genre = "Fantasy"):
  if (Genre == "Fantasy"):
    PickFantasyMainTitle()

def PickNickName(Genre = "Fantasy"):
  if (Genre == "Fantasy"):
    PickFantasyNickName()