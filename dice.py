def drawDice(firstroll, secondroll):
    if firstroll == 1 or secondroll == 1:
        return """ 
        ===========
        |         |
        |    O    |
        |         |
        ===========""".split("\n")
    if firstroll == 2 or secondroll == 2:
        return """
        ===========
        | O       |
        |         |
        |       O |
        ===========""".split("\n")
    if firstroll == 3 or secondroll == 3:
        return """
        ===========
        | O       |
        |    O    |
        |       O |
        ===========""".split("\n")
    if firstroll == 4 or secondroll == 4:
        return """
        ===========
        | O     O |
        |         |
        | O     O |
        ===========""".split("\n")
    if firstroll == 5 or secondroll == 5:
        return """
        ===========
        | O     O |
        |    O    |
        | O     O |
        ===========""".split("\n")
    if firstroll == 6 or secondroll == 6:
        return """
        ===========
        | O     O |
        | O     O |
        | O     O |
        ===========""".split("\n")

    
def checkEvenRoll(roll1, roll2):
    if (roll1 + roll2) % 2 == 0:
        return True
    else:
        return False
