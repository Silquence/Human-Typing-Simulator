import pyautogui
import time
import random
import sys

def cursor_initializer():
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width*3/4,screen_height*1/2)
    pyautogui.click()

typo_map = {
        # Row 1
        "q": ["w", "a"],
        "w": ["q", "e", "s"],
        "e": ["w", "r", "d"],
        "r": ["e", "t", "f"],
        "t": ["r", "y", "g"],
        "y": ["t", "u", "h"],
        "u": ["y", "i", "j"],
        "i": ["u", "o", "k"],
        "o": ["i", "p", "l"],
        "p": ["o", "l"],
        # Row 2
        "a": ["q", "s", "z"],
        "s": ["a", "w", "d", "x"],
        "d": ["s", "e", "f", "c"],
        "f": ["d", "r", "g", "v"],
        "g": ["f", "t", "h", "b"],
        "h": ["g", "y", "j", "n"],
        "j": ["h", "u", "k", "m"],
        "k": ["j", "i", "l"],
        "l": ["k", "o", "p"],
        # Row 3
        "z": ["a", "x"],
        "x": ["z", "s", "c"],
        "c": ["x", "d", "v"],
        "v": ["c", "f", "b"],
        "b": ["v", "g", "n"],
        "n": ["b", "h", "m"],
        "m": ["n", "j"],
        # Uppercase
        "Q": ["W", "A"],
        "W": ["Q", "E", "S"],
        "E": ["W", "R", "D"],
        "R": ["E", "T", "F"],
        "T": ["R", "Y", "G"],
        "Y": ["T", "U", "H"],
        "U": ["Y", "I", "J"],
        "I": ["U", "O", "K"],
        "O": ["I", "P", "L"],
        "P": ["O", "L"],

        "A": ["Q", "S", "Z"],
        "S": ["A", "W", "D", "X"],
        "D": ["S", "E", "F", "C"],
        "F": ["D", "R", "G", "V"],
        "G": ["F", "T", "H", "B"],
        "H": ["G", "Y", "J", "N"],
        "J": ["H", "U", "K", "M"],
        "K": ["J", "I", "L"],
        "L": ["K", "O", "P"],

        "Z": ["A", "X"],
        "X": ["Z", "S", "C"],
        "C": ["X", "D", "V"],
        "V": ["C", "F", "B"],
        "B": ["V", "G", "N"],
        "N": ["B", "H", "M"],
        "M": ["N", "J"],
    }

def typo_writer(typo_map, total_count, current_count, last_chr):
    if current_count<total_count:
        possible_typo = typo_map[last_chr]
        if random.randint(0,100) < 90:
            typo = random.choice(possible_typo)
        else:
            typo = chr(random.randint(97,122))
        pyautogui.write(typo)
        current_count += 1
        typo_writer(typo_map,total_count, current_count, typo)

def typo_eraser(total_count, pause_time):
    for i in range(0,total_count):
        pyautogui.press("backspace")
    time.sleep(pause_time)

def typo_generator(typo_map,total_count,last_chr):
    typo_writer(typo_map,total_count,0,last_chr)
    time.sleep(0.5)
    typo_eraser(total_count,0.17)



def pause(frequency):
    if random.randint(0,500)<frequency:
        time.sleep(random.randint(1,3))

def type(file):
    original_x, original_y = pyautogui.position()
    for line in file:
        word = line.split()
        for i in word:
            for j in i:
                #error simualtion
                typo_generator(2.8) #best value 2.8
                pause(2)            #best value ?

                pyautogui.write(j)

                #exit logic
                axis = pyautogui.position()
                if axis[0] > original_x + 30 or axis[0] < original_x - 30 or axis[1] > original_y + 30 or axis[
                    1] < original_y - 30:
                    if pyautogui.confirm("stop?", buttons=["Yes", "No"]) == "Yes":
                        sys.exit()
                    else:
                        original_x, original_y = pyautogui.position()

            pyautogui.write(" ")
        pyautogui.keyDown('enter')
        pyautogui.keyUp=('enter')

#below is the execution code
# cursor_initializer()
# with open("doc.docx", "r") as f:
#      type(f)

cursor_initializer()
typo_generator(typo_map,5,"a")