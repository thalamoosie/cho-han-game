"""
Chō-Han Bakuchi
Thalamoosie (Britt Pezzillo)
thalamoosie@protonmail.com

Adapted from Al Sweigart's project in The Big Book of Small Python Projects. 
Many thanks to Al for being a huge part of my Python development journey.

Roll 2D6 and bet if the resulting sum of the two dice is odd or even.
House gets a 10% cut.
Snake-Eyes (12) and Seven (7) sums are lucky and will pay out an additional 15% bonus
Four (4) is an unlucky sum and should result in a -5% payout
"""

import random, sys
from textstyling import movingText
import chalk
from dice import drawDice, checkEvenRoll

japaneseNumbers = {1:"ICHI", 2:"NI", 3:"SAN", 4:"SHI", 5:"GO", 6:"ROKU", 7:"SHICHI", 8:"HACHI", 9:"KYU", 10:"JUU", 11:"JUU ICHI", 12:"JUU NI"}
affirmativeResponses = ["Y", "N"]
difficultyResponses = ["A", "B", "C"]
evenOrOddResponses = ["CHO", "HAN"]
insults = ["YARO", "BAKA", "DINGUS", "STUPID", "MANBABY", "FUCK YOU", "DUMB"]

# Different purse difficulties
purse = 0
pauperPurse = random.randint(1000,3050)
salaryPurse = random.randint(3500, 5200)
royalPurse = random.randint(5650, 8200)
game = True
insultCounter = 0

#ASCII Title Format
print("""    
   ______ __                   __  __                 
  / ____// /_   ____          / / / /____ _ ____      
 / /    / __ \ / __ \ ______ / /_/ // __ `// __ \     
/ /___ / / / // /_/ //_____// __  // /_/ // / / /     
\____//_/_/_/ \____/   __  /_/ /_/ \__,_//_/ /_/ _    
        / __ ) ____ _ / /__ __  __ _____ / /_   (_)   
       / __  |/ __ `// //_// / / // ___// __ \ / /    
      / /_/ // /_/ // ,<  / /_/ // /__ / / / // /     
     /_____/ \__,_//_/|_| \__,_/ \___//_/ /_//_/   \n""")
print("An exciting game of dice and chance.\n")


#=============================================
# Main Game Loop
#=============================================
while game:
# ==============================================
# Game Introduction & Explanation of Rules
#===============================================
# CHOOSE DIFFICULTY
    difficultyChoice = True

    while difficultyChoice:
        movingText("Before we begin, what size purse would you like to play with?\n")
        print("(A) Pauper (Hardest)")
        print("(B) Salaryman (Normal) ")
        print("(C) Royalty (You're Loaded Already!) ")
        print("..or Q to QUIT!")
        difficultyResponse = input('> ')
        if difficultyResponse.upper() == "Q":
            movingText("Your choice! See you later.")
            sys.exit()
        elif difficultyResponse.upper() not in difficultyResponses:
            movingText("Please choose from the list of difficulties (A/B/C) or press Q to quit.\n")
        elif difficultyResponse.upper() == "A":
            purse = pauperPurse
            movingText(f"You scan our pockets and find a measly {purse} mon to gamble.\n")
            break
        elif difficultyResponse.upper() == "B":
            purse = salaryPurse
            movingText(f"Your salary fills your coinpurse with {purse} mon.\n")
            break
        elif difficultyResponse.upper() == "C":
            purse = royalPurse
            movingText(f"Your princely purse contains {purse} mon.\n")
            break

#Test output of purse based on user selection

# Begin opening dialogue
    print("""You part a curtain and duck, entering a humble gaming house. There is a tatami and a table before you
    and a shirtless dealer sitting seiza welcoming you to the game.\n""")
    movingText('>> Dealer: The game is Chō-Han, have you played before? (Y or N, Q to Quit)\n')

    playingChoice = True

    while playingChoice:
        playingResponse = input('> ')
        if playingResponse.upper() == "Q":
            movingText("Perhaps some other time, Nakama. Arigato!\n")
            sys.exit()
        elif playingResponse.upper() not in affirmativeResponses:
            print("Please answer the question using Y / N / Q.")
        elif playingResponse.upper() == "N":
            print("The game is Chō-Han. I will roll 2 6-sided dice and conceal the result. You must bet whether they tally to an even (CHO) or odd (HAN) sum.")
            print("You will get bonuses for lucky numbers like double 6s and the number 7 (SHICHI). ")
            print("Unlucky numbers such as 4 (SHI) will result in a weaker reward. That said..")
            movingText("GANBATTE!!\n")
            break
        else:
            break

    while True:
        print(f"You have {purse} coins to wager. How much would you like to bet? (Q to Quit)\n")
        pot = input("> ")
        if pot.upper() == "Q":
            print("Ason de kure te, arigato!")
            sys.exit()
        elif pot.upper() in insults:
            insultCounter += 1
            movingText("NANI!\n")
            if insultCounter >= 3:
                movingText("I think you've had enough sake for one night. Get out!\n")
                print(""" 
 _______  _______  __   __  _______   _______  __   __  _______  ______    __  
|       ||   _   ||  |_|  ||       | |       ||  | |  ||       ||    _ |  |  | 
|    ___||  |_|  ||       ||    ___| |   _   ||  |_|  ||    ___||   | ||  |  | 
|   | __ |       ||       ||   |___  |  | |  ||       ||   |___ |   |_||_ |  | 
|   ||  ||       ||       ||    ___| |  |_|  ||       ||    ___||    __  ||__| 
|   |_| ||   _   || ||_|| ||   |___  |       | |     | |   |___ |   |  | | __  
|_______||__| |__||_|   |_||_______| |_______|  |___|  |_______||___|  |_||__| 
""")
                sys.exit()
        elif not pot.isdecimal():
            print("Please enter a numeric value for your mon wager.")
        elif int(pot) > purse:
            movingText("Do not try to pull one over on me. You do not have enough money to make that bet.")
        else:
            pot = int(pot)
            break

    die1 = random.randint(1,6)
    die2 = random.randint(1,6)

    print(""" The dealer grabs a bamboo cup and begins to shake the dice around inside for what feels like an eternity.
There is a slight thud as he slams the cup on to the table before you. His hand is still gripping the cup, keeping the results covered. It is time for you to bet.\n
""")
    movingText("What is your guess, nakama?")
    movingText("    CHO (Even) -or- HAN (Odd)?\n")

    while True:
        playerBet = input("> ").upper()
        if playerBet not in evenOrOddResponses:
            movingText("You must decide: CHO or HAN. Which will it be?")
            continue
        else:
            break
    
    #Calculate the score and display the die rolls
    print("The dealer smirks as he curls his fingers around the cup. He lifts it up to reveal...")
    print(f"    {japaneseNumbers[die1]} - {japaneseNumbers[die2]} ")
    print(f"     {die1}  -  {die2} ")

    even = checkEvenRoll(die1, die2)
    if even:
        correctBet = "CHO"
    else:
        correctBet = "HAN"

    playerWon = playerBet == correctBet

    if playerWon:
        movingText(f"You won! You take {pot} mon")
        purse += pot


    drawDice(die1, die2)

    print(f"Total: {die1 + die2}")










