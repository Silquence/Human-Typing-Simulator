import pyautogui
import time
import random
import sys
import customtkinter as ctk
import threading

Error_rate = 2
Speed = 10
Dynamic_err_rate = False
Dynamic_Speed = False
max_rate = 20

#below is the GUI code
def slider_color(value, max_rate):
    value = float(value)
    max_rate = float(max_rate)
    t = value / max_rate  # 0~1 归一化
    if t <= 0.3:
        ratio = t / 0.3
        r = int(0 + 255 * ratio)
        g = int(200 - 35 * ratio)
        b = 0
    else:
        ratio = (t - 0.3) / 0.7
        r = 255
        g = int(165 - 165 * ratio)
        b = 0
    return f"#{r:02x}{g:02x}{b:02x}"

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
root = ctk.CTk()
root.title("Human Typing Simulator")
root.geometry("800x400")
root.resizable(False, False)
main_frame = ctk.CTkFrame(root, corner_radius=20)
main_frame.pack(padx=20, pady=20, fill="both", expand=True)
title_label = ctk.CTkLabel(main_frame,text="Typing Configuration",font=("Segoe UI", 26, "bold"))
title_label.pack(pady=(20, 25))

# Error Rate Slider
err_rate_title = ctk.CTkLabel(main_frame,text="Error Rate",font=("Segoe UI", 16))
err_rate_title.pack(anchor="w", padx=30)

def get_err_rate(value):
    global Error_rate
    Error_rate = value
    err_rate_slider.configure(
        progress_color=slider_color(value,max_rate)
    )
    print(Error_rate)

err_rate_slider = ctk.CTkSlider(main_frame,from_=0,to=max_rate,command=get_err_rate)
err_rate_slider.set(Error_rate)
err_rate_slider.configure(progress_color=slider_color(Error_rate,max_rate))
err_rate_slider.pack(fill="x",padx=30,pady=(5, 20))

# Speed Slider
speed_title = ctk.CTkLabel(main_frame,text="Typing Speed",font=("Segoe UI", 16))
speed_title.pack(anchor="w", padx=30)

def get_speed(value):
    global Speed
    Speed = value
    speed_slider.configure(progress_color=slider_color(value,max_rate))
    print(Speed)

speed_slider = ctk.CTkSlider(main_frame,from_=0,to=max_rate,command=get_speed)
speed_slider.set(Speed)
speed_slider.configure(progress_color=slider_color(Speed,max_rate))
speed_slider.pack(fill="x",padx=30,pady=(5, 30))

# Confirm Configuration
def confirm_speed():
    speed_slider.configure(state="disabled")
    root.destroy()
confirm_speed_button = ctk.CTkButton(
    main_frame,
    text="confirm configuration",
    command=confirm_speed,
    width=100,
    height=40,
    corner_radius=20,
    fg_color="#678DC6",
)
confirm_speed_button.place(x=550, y=285)

# Dynamic Switches t1: dyna err, t2: dyna speed
def toggle_t1():
    global Dynamic_err_rate
    Dynamic_err_rate = not Dynamic_err_rate
    print(Dynamic_err_rate)

def toggle_t2():
    global Dynamic_Speed
    Dynamic_Speed = not Dynamic_Speed
    print(Dynamic_Speed)

toggle_t1_button = ctk.CTkSwitch(
    main_frame,
    text="Dynamic Error Rate",
    command=toggle_t1,
)
toggle_t1_button.place(x=30, y=270)

toggle_t2_button = ctk.CTkSwitch(
    main_frame,
    text="Dynamic Speed",
    command=toggle_t2,
)
toggle_t2_button.place(x=30, y=320)

#below is the backend code
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

def type(file,pause_time,error_rate,dynamic_freq:bool,dynamic_typo:bool):
    original_x, original_y = pyautogui.position()
    count = 0
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
root.mainloop()
# cursor_initializer()
# with open("doc.docx", "r") as f:
#      type(f,Speed,Error_rate, True,True)


