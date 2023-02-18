def GenerateStats(Game, Method = "3d6"):
    if (Method == "3d6"):
        for y in len(StatList):
            CharStats[y] = RollDice(6, 3)
            print(paste(StatList[y], CharStats[y]))
    elif (Method == "4d6droplow"):
        for y in seq_along(StatList):
            for x in 4:
                TempDice[x] = RollDice(6, 1)
                TempDice[which.min(TempDice)] = 0
                CharStats[y] = Reduce("+", TempDice)
    else:
        if (Method == "PointBuy"):
            for x in StatList:
                CharStats[x]  = 12

def ValidateStatSwap(FirstStat, SecondStat):
    if (FirstStat == SecondStat & (FirstStat not in StatList) & (SecondStat not in StatList)):
        False
    else:
        True

def SwapStats(FirstStat, SecondStat):
    if (ValidateStatSwap(FirstStat, SecondStat)):
        replace(CharStats
        , c(ReturnStatIndex(FirstStat)
        , ReturnStatIndex(SecondStat))
        , CharStats = CharStats[c(ReturnStatIndex(SecondStat)
        , ReturnStatIndex(FirstStat))])
        DisplayChar()
        RecommendClass(CharStats)

def GenerateBaseStatList():
 StatList = unlist(read.csv(file = "data\\BaseStats.csv", header = FALSE))