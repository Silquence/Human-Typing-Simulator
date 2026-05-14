import pyautogui
import time
import random
import sys

pyautogui.moveTo(1000,450)
time.sleep(0.5)
pyautogui.click()
time.sleep(0.5)

def typo_generator(frequency): #0-100 5 is best
    if random.randint(0,100)<frequency:
        err_length = random.randint(1,10)
        for i in range(0,err_length):
            pyautogui.write(chr(random.randint(97,122)))
        for i in range(0,err_length):
            pyautogui.press('backspace')



def type(file):
    for line in file:
        word = line.split()
        for i in word:
            for j in i:
                typo_generator(5)
                pyautogui.write(j)
            pyautogui.write(" ")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')


#below is the execution code
with open("doc.docx", "r") as f:
    type(f)
