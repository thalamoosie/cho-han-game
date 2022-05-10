def drawDice(roll):
    if roll == 1:
        return """ 
        ===========
        |         |
        |    O    |
        |         |
        ==========="""
    if roll == 2:
        return """
        ===========
        | O       |
        |         |
        |       O |
        ==========="""
    if roll == 3:
        return """
        ===========
        | O       |
        |    O    |
        |       O |
        ==========="""
    if roll == 4:
        return """
        ===========
        | O     O |
        |         |
        | O     O |
        ==========="""
    if roll == 5:
        return """
        ===========
        | O     O |
        |    O    |
        | O     O |
        ==========="""
    if roll == 6:
        return """
        ===========
        | O     O |
        | O     O |
        | O     O |
        ==========="""
    
def checkEvenRoll(roll1, roll2):
    if (roll1 + roll2) % 2 == 0:
        return True
    else:
        return False
