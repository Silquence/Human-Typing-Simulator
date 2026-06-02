import pyautogui
import time
import random
import subprocess

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
def applescript(cmd):
    subprocess.run(["osascript", "-e", cmd])

def probability(probability):
    if random.uniform(0,100)<probability:
        return True
    else:
        return False

def cursor_initializer():
    screen_width, screen_height = pyautogui.size()

    pyautogui.moveTo(screen_width * 3 / 4,screen_height * 0.8,duration=0.1)
    pyautogui.click()
    # 等待窗口获取焦点
    time.sleep(0.2)
    applescript(
        '''
        tell application "System Events"
            key code 125 using {command down}
        end tell
        '''
    )
    time.sleep(0.2)

cursor_pos = 0
word:list[str]
with open ("cache.txt","r") as f:
    word = f.read().split()
def type(word_to_print):
    global typo_map
    typo_cursor = 0
    location:list[int]
    numTypos = random.randint(1,int(len(word_to_print)/2))
    location = random.sample(range(0,len(word_to_print)),numTypos)
    location.sort()
    for i in range(0,len(word_to_print)):
        if typo_cursor<len(location) and i == location[typo_cursor]:
            typo_cursor += 1
            pyautogui.write(random.choice(typo_map[word_to_print[i]]))

        else:
            pyautogui.write(word_to_print[i])

    #percise correction starts here
    for i in range(0,(len(word_to_print)-location[0])-1):
        applescript( #left
            '''
            tell application "System Events"
                key code 123
            end tell
            '''
        )
    count = 0
    while count < len(location):
        time.sleep(0.5)
        applescript( #backspace
            '''
            tell application "System Events"
                key code 51
            end tell
            '''
        )
        time.sleep(0.1)
        pyautogui.write(word_to_print[location[count]])

        if count == len(location)-1:
            count += 1
            continue

        for i in range(location[count+1]-location[count]):
            applescript( #right
                '''
                tell application "System Events"
                    key code 124
                end tell
                '''
            )
        count += 1

    for i in range(len(word_to_print)-location[len(location)-1]-1):
        applescript(
            '''
            tell application "System Events"
                key code 124
            end tell
            '''
        )
        time.sleep(0.1)
#below are the execution lines
cursor_initializer()
type("abcdefghijk")











