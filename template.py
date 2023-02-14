import pyautogui as tanya
import time
import os

def openTerminal():
    print()
    tanya.hotkey('cmd', 'space')


# Specify the directory path
path = r'/Users/abhijayrajvansh/Desktop'
file_name = 'tanya.txt'

open(os.path.join(path, file_name), 'w')

os.system("open tanya.txt")

time.sleep(3)


tanya.write('Hello There', interval = 0.07)
tanya.press('enter')
tanya.write('How is the Weather?', interval = 0.07)

