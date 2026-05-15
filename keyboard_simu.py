import pyautogui
import time
import random
import sys

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
        #special characters
        " ": [" "],
        ",": ["."],
        ".": [","],
        "?": ["/"]
    }

def cursor_initializer():
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width*3/4,screen_height*1/2)
    pyautogui.click()

def probability(probability):
    if random.uniform(0,100)<probability:
        return True
    else:
        return False

def typo_writer(typo_map, total_count, current_count, last_chr):
    if current_count<total_count:
        possible_typo = typo_map[last_chr]
        if probability(90):
            try:
                typo = random.choice(possible_typo)
            except KeyError:
                typo = chr(random.randint(97,122))
        else:
            typo = chr(random.randint(97,122))
        pyautogui.write(typo)
        current_count += 1
        typo_writer(typo_map,total_count, current_count, typo)

def typo_eraser(total_count, pause_time):
    for i in range(0,total_count):
        pyautogui.press("backspace")
    time.sleep(pause_time)

def typo_generator(typo_map,total_count,last_chr,rate):
    if probability(rate):
        typo_writer(typo_map,total_count,0,last_chr)
        time.sleep(0.17)
        typo_eraser(total_count,0.17)

def speed_control(pause_time,pause_rate,last_chr): #0-10
    if probability(pause_rate):
        time.sleep(random.uniform(1,3))
    if last_chr in [",",".","?"]:
        time.sleep(random.uniform(pause_time/18,pause_time/2))

def type(file,dynamic_freq:bool,dynamic_typo:bool):
    original_x, original_y = pyautogui.position()
    count = 0
    pause_time = 3
    error_rate = 20
    for line in file:
        word = line.split()
        for i in word:
            for j in i:
                if dynamic_typo == True:
                    error_rate += count/1000000
                typo_generator(typo_map,random.randint(1,4),j,error_rate)
                pyautogui.write(j)
                count += 1
                if dynamic_freq == True:
                    pause_time += count/1000000
                speed_control(pause_time, 2, j)

                #this section is for debug only, delete before release======
                print(pause_time,error_rate, sep = " ")
                #===========================================================

                #exit logic
                axis = pyautogui.position()
                if (axis[0] > original_x + 30 or axis[0] < original_x - 30
                        or axis[1] > original_y + 30 or axis[1] < original_y - 30):
                    if pyautogui.confirm("stop?", buttons=["Yes", "No"]) == "Yes":
                        sys.exit()
                    else:
                        original_x, original_y = pyautogui.position()

            pyautogui.write(" ")
        pyautogui.press('enter')

#below is the execution code
cursor_initializer()
with open("doc.docx", "r") as f:
     type(f, False,False)

