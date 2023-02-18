def Attack(Weapon = "Stick", Swings = 1):
    for x in Swings:
        if RollDice(20,1,SwingBonus()) >= TargetDummyAC:
            RollDice(4, 1, DamageBonus())
        else:
            AttackLog[x] = 0

def DisplayAttackLog():
  barplot(table(unlist(AttackLog[seq_along(AttackLog)])))

def SwingBonus():
  ComputedStatValue.BaseAttackBonus