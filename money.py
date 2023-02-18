def GenerateWealth(CharClass) :
    CharMoney <<- RollDice(6, ClassMatrix[CharClass, "StartingWealth"]) * 100000
    return(CharMoney)

def GenerateMoneyString(CharMoney, CharMainTitle, FirstName) :
    CharMainTitle + CharFirstName + "has" + (CharMoney / 10000) + "gold," + "0" + "silver, and" + "0" + "copper"