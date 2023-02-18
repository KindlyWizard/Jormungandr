def RollDice(DieSize = 6, DiceNumber = 1, Bonus = 0): 
    if ValidateDieRoll(DieSize, DiceNumber, Bonus):
        for x in DiceNumber:
            TotalRolled = TotalRolled + randint(1, DieSize)
        TotalRolled = TotalRolled + Bonus
    else: print("Invalid Entry")

def ValidateDieRoll(DieSize, DiceNumber, Bonus=0):
    if DieSize in ValidDieSize & DiceNumber >= 1 & Bonus == Bonus:
        return(True)
    else: return(False)
    