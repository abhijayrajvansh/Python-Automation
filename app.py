import pyautogui as bobby
import time
import os

def openTerminal():
    print("Launching Terminal ...")
    
    bobby.keyDown('command')
    bobby.keyDown('space')

    bobby.keyUp('space')
    bobby.keyUp('command')

    bobby.write("iterm", interval = 0.1)
    bobby.press('return')



openTerminal()
