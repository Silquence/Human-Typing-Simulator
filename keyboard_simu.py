import pyautogui
import time
import random
import sys

def cursor_initializer():
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width*3/4,screen_height*1/2)
    pyautogui.click()

def typo_generator(frequency): #0-100 5 is best
    if random.randint(0,100)<frequency:
        err_length = random.randint(1,4)
        for i in range(0,err_length):
            pyautogui.write(chr(random.randint(97,122)))
        for i in range(0,err_length):
            pyautogui.press('backspace')

def pause(frequency):
    if random.randint(0,500)<frequency:
        time.sleep(random.randint(1,3))

def type(file):
    original_x, original_y = pyautogui.position()
    for line in file:
        word = line.split()
        for i in word:
            for j in i:
                typo_generator(2.8)
                pause(2)
                pyautogui.write(j)


                axis = pyautogui.position()
                if axis[0] > original_x + 30 or axis[0] < original_x - 30 or axis[1] > original_y + 30 or axis[
                    1] < original_y - 30:
                    if pyautogui.confirm("Stop?", buttons=["Yes", "No"]) == "Yes":
                        sys.exit()
                    else:
                        original_x, original_y = pyautogui.position()


            pyautogui.write(" ")
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')




#below is the execution code
cursor_initializer()
with open("doc.docx", "r") as f:
     type(f)

