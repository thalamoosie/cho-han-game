import time, sys, os

def movingText(text):
    for char in text:
        print(char, end='', flush=True)
        if char != "\n":
            time.sleep(0.03)
        else:
            time.sleep(0.1)
            
def movingInput(message):
    for char in message:
        print(char, end='', flush=True)
        time.sleep(0.03)
    playerValue = input()
    return playerValue