import pyautogui
import time

f = open('lirik', 'r')
time.sleep(3)

for word in f :
    pyautogui.typewrite(word)
    pyautogui.press("enter")