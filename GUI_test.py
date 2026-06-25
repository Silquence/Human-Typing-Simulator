import pyautogui
import time
import random
import customtkinter as ctk
import threading
import subprocess
import os
import re
import sys

#cache file direction
cache_dir = os.path.join(
    os.path.expanduser("~"),
    "Library",
    "Caches",
    "Human Typing Simulator"
)
cache_file = os.path.join(cache_dir, "cache.txt")
if not os.path.exists(cache_dir):
    os.makedirs(cache_dir)
if not os.path.exists(cache_file):
    with open(cache_file, "w") as f:
        f.write("")
cache_file_dir = os.path.join(
    os.path.expanduser("~"),
    "Library",
    "Caches",
    "Human Typing Simulator",
    "cache.txt"
)

#configurations
Error_rate = 2
Speed = 10
Dynamic_err_rate = False
Dynamic_Speed = False
max_rate = 100
is_on = False #打字器状态
turn_off = False #程序状态
text = []
original_mouse_position = (0,0)
pause_triggered = False
hybrid = False
err_generator_model = "N/A"
awaiting_current_word_to_finish = False


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


ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Tahoe 标准现代浅色基调
TAHOE_BG = "#F3F3F3"
TAHOE_CARD_BG = "#FAFAFA"

root = ctk.CTk()
root.title("Human Typing Simulator")
root.geometry("640x640")
root.resizable(False, False)
root.configure(fg_color=TAHOE_BG)

# 字体设置
FONT_TITLE = ("SF Pro Display", 20, "bold")
FONT_LABEL = ("SF Pro Text", 13, "bold")
FONT_VALUE = ("SF Pro Text", 13, "normal")
FONT_WIDGET = ("SF Pro Text", 13)

# 主容器
main_frame = ctk.CTkFrame(root, corner_radius=0, fg_color=TAHOE_BG)
main_frame.pack(padx=30, pady=25, fill="both", expand=True)

# 顶部标题
title_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)
title_frame.pack(fill="x", pady=(5, 20))
title_label = ctk.CTkLabel(
    title_frame,
    text="Typing Configuration",
    font=FONT_TITLE,
    text_color="#1E1E1E"
)
title_label.pack(side="left")

#暂停指示灯
pause_mode = "Paused"

pause_label = ctk.CTkLabel(
    title_frame,
    text="Paused",
    font=("SF Pro Text", 12, "bold"),
    text_color="#007AFF"
)

def update_pause_indicator():
    global awaiting_current_word_to_finish, pause_mode
    if awaiting_current_word_to_finish == True:
        pause_mode = "● Pause After Finishing Current Word"
        pause_color = "#FF78A0"
    else:
        pause_mode = "● Paused"
        pause_color = "#7C0A02"

    if is_on and pause_triggered:
        if not model_label.winfo_ismapped():
            model_label.pack(
                side="right",
                padx=(0, 5)
            )
        model_label.configure(
            text=pause_mode,
            text_color=pause_color
        )
    else:
        if pause_label.winfo_ismapped():
            pause_label.pack_forget()
    root.after(1, update_pause_indicator)

update_pause_indicator()

#ready_label 指示灯
ready_label = ctk.CTkLabel(
    title_frame,
    text="● Ready",
    font=("SF Pro Text", 12, "bold"),
    text_color="#228B22"
)

def update_ready_indicator():
    if is_on == False and pause_triggered == False:
        if not ready_label.winfo_ismapped():
            ready_label.pack(
                side="right",
                padx=(0, 5)
            )
        ready_label.configure(
            text_color="#228B22"
        )
    else:
        if ready_label.winfo_ismapped():
            ready_label.pack_forget()
    root.after(100, update_ready_indicator)
update_ready_indicator()

#current model 指示灯
model_status = f"● Model: {err_generator_model}"
model_label = ctk.CTkLabel(
    title_frame,
    text=f"● Model: {err_generator_model}",
    font=("SF Pro Text", 12, "bold"),
    text_color="#007AFF"
)

def update_model_indicator():
    if is_on and pause_triggered == False and awaiting_current_word_to_finish == False:
        if not model_label.winfo_ismapped():
            model_label.pack(
                side="right",
                padx=(0, 5)
            )
        model_label.configure(
            text=f"● Model: {err_generator_model}",
            text_color="#007AFF"
        )
    else:
        if model_label.winfo_ismapped():
            model_label.pack_forget()
    root.after(100, update_model_indicator)
update_model_indicator()

# 卡片式分组框
group_box = ctk.CTkFrame(
    main_frame,
    corner_radius=14,
    fg_color=TAHOE_CARD_BG,
    border_width=0
)
group_box.pack(fill="both", expand=True, pady=(0, 15))

# 内部布局
group_box.grid_columnconfigure(0, weight=1)
group_box.grid_columnconfigure(1, weight=5)
group_box.grid_columnconfigure(2, weight=1)

# --- 1. ERROR RATE 控制行 ---
err_title = ctk.CTkLabel(
    group_box,
    text="Error Rate",
    font=FONT_LABEL,
    text_color="#2C2C2C"
)

err_title.grid(
    row=0,
    column=0,
    sticky="w",
    padx=(20, 10),
    pady=(25, 12)
)

def get_err_rate(value):
    global Error_rate
    Error_rate = value

    err_rate_slider.configure(
        progress_color=slider_color(value, max_rate)
    )

    err_value_label.configure(
        text=f"{value:.1f}"
    )


err_rate_slider = ctk.CTkSlider(
    group_box,
    from_=0,
    to=max_rate,
    number_of_steps=200,
    command=get_err_rate,
    fg_color="#E2E2E7",
    button_color="#FFFFFF",
    button_hover_color="#F5F5F7",
    height=5,
    border_width=1,
    border_color="#D8D8DC"
)

err_rate_slider.set(Error_rate)

err_rate_slider.configure(
    progress_color=slider_color(Error_rate, max_rate)
)

err_rate_slider.grid(
    row=0,
    column=1,
    sticky="ew",
    padx=10,
    pady=(25, 12)
)

err_value_label = ctk.CTkLabel(
    group_box,
    text=f"{Error_rate:.1f}",
    font=FONT_VALUE,
    text_color="#6E6E73",
    width=40,
    anchor="w"
)

err_value_label.grid(
    row=0,
    column=2,
    sticky="w",
    padx=(10, 20),
    pady=(25, 12)
)

# --- 2. TYPING SPEED 控制行 ---
speed_title = ctk.CTkLabel(
    group_box,
    text="Typing Speed",
    font=FONT_LABEL,
    text_color="#2C2C2C"
)

speed_title.grid(
    row=1,
    column=0,
    sticky="w",
    padx=(20, 10),
    pady=12
)

def get_speed(value):
    global Speed
    Speed = value

    speed_slider.configure(
        progress_color=slider_color(value, max_rate)
    )

    speed_value_label.configure(
        text=f"{value:.1f}"
    )

speed_slider = ctk.CTkSlider(
    group_box,
    from_=1,
    to=max_rate,
    number_of_steps=190,
    command=get_speed,
    fg_color="#E2E2E7",
    button_color="#FFFFFF",
    button_hover_color="#F5F5F7",
    height=5,
    border_width=1,
    border_color="#D8D8DC"
)

speed_slider.set(Speed)

speed_slider.configure(
    progress_color=slider_color(Speed, max_rate)
)

speed_slider.grid(
    row=1,
    column=1,
    sticky="ew",
    padx=10,
    pady=12
)

speed_value_label = ctk.CTkLabel(
    group_box,
    text=f"{Speed:.1f}",
    font=FONT_VALUE,
    text_color="#6E6E73",
    width=40,
    anchor="w"
)

speed_value_label.grid(
    row=1,
    column=2,
    sticky="w",
    padx=(10, 20),
    pady=12
)

# --- 3. DYNAMIC SWITCHES ---
def toggle_t1():
    global Dynamic_err_rate
    Dynamic_err_rate = not Dynamic_err_rate

def toggle_t2():
    global Dynamic_Speed
    Dynamic_Speed = not Dynamic_Speed

def toggle_t3():
    global hybrid
    hybrid = not hybrid

switch_frame = ctk.CTkFrame(
    group_box,
    fg_color="transparent"
)

switch_frame.grid(
    row=2,
    column=1,
    columnspan=2,
    sticky="w",
    padx=10,
    pady=(15, 25)
)

toggle_t1_button = ctk.CTkSwitch(
    switch_frame,
    text="Enable Dynamic Error Rate",
    command=toggle_t1,
    font=FONT_WIDGET,
    text_color="#2C2C2C",
    progress_color="#34C759",
    fg_color="#E2E2E7"
)
toggle_t1_button.pack(anchor="w", pady=6)

toggle_t2_button = ctk.CTkSwitch(
    switch_frame,
    text="Enable Dynamic Speed",
    command=toggle_t2,
    font=FONT_WIDGET,
    text_color="#2C2C2C",
    progress_color="#34C759",
    fg_color="#E2E2E7"
)
toggle_t2_button.pack(anchor="w", pady=6)

toggle_t3_button = ctk.CTkSwitch(
    switch_frame,
    text="Hybrid Mode",
    command=toggle_t3,
    font=FONT_WIDGET,
    text_color="#2C2C2C",
    progress_color="#34C759",
    fg_color="#E2E2E7"
)
toggle_t3_button.pack(anchor="w", pady=6)

# --- 底部动作栏 ---
bottom_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)

bottom_frame.pack(
    fill="x",
    side="bottom",
    pady=(5, 5)
)

def confirm_speed():
    global text, is_on,cursor_pos,count,pause_triggered,key_map
    cursor_pos = 0
    count = 0
    confirm_speed_button.configure(state="normal")
    pause_triggered = False
    with open (cache_file_dir,"w") as cache:
        content = textbox.get("1.0", "end-1c")
        cache.write(content)
    with open (cache_file_dir,"r") as cache:
        text = re.findall(
            r'\n|[ \t]+|\w+|[^\w\s]',
            cache.read()
        )


    error_flag = False
    for token in text:
        try:
            key_map[token]
        except KeyError:
            subprocess.run(
                ["osascript", "-e",
                 'button returned of (display dialog "Unexpected character detected" buttons {"Yes"} default button "Yes")'
                 ], capture_output=True, text=True).stdout.strip()
            error_flag = True
            print(error_flag)
            break

    if error_flag == False:
        textbox.configure(state="disabled")
        time.sleep(0.05)
        cursor_initializer()
        is_on = True
    else:
        Reset()


confirm_speed_button = ctk.CTkButton(
    bottom_frame,
    text="Go",
    command=confirm_speed,
    width=80,
    height=30,
    corner_radius=8,
    fg_color="#007AFF",
    hover_color="#0066CC",
    font=("SF Pro Text", 13, "bold")
)
confirm_speed_button.pack(side="right")

def Exit():
    global turn_off,is_on
    turn_off = True
    is_on = False
    time.sleep(0.23)
    root.destroy()

def Reset():
    global is_on, cursor_pos, chars, \
        resume, count, text_changed, \
        Speed, Error_rate, Dynamic_Speed, \
        Dynamic_err_rate,max_rate,pause_triggered, hybrid,\
        err_generator_model, awaiting_current_word_to_finish

    #reset the paras to default
    is_on = False
    confirm_speed_button.configure(state = "disabled")

    Error_rate = 2
    Speed = 10
    Dynamic_err_rate = False
    Dynamic_Speed = False
    speed_slider.set(Speed)
    err_rate_slider.set(Error_rate)
    speed_value_label.configure(text=f"{Speed:.1f}")
    err_value_label.configure(text=f"{Error_rate:.1f}")
    speed_slider.configure(progress_color=slider_color(Speed, max_rate))
    err_rate_slider.configure(progress_color=slider_color(Error_rate, max_rate))
    toggle_t1_button.deselect()
    toggle_t2_button.deselect()
    textbox.configure(state="normal")
    cursor_pos = 0
    count = 0
    confirm_speed_button.configure(state = "normal")
    pause_triggered = False
    hybrid  = False
    err_generator_model = "N/A"
    awaiting_current_word_to_finish = False

Reset_button = ctk.CTkButton(
    bottom_frame,
    text="Reset",
    command=Reset,
    width=80,
    height=30,
    corner_radius=8,
    fg_color="#FF3B30",
    hover_color="#C92A1F",
    font=("SF Pro Text", 13, "bold")
)

Reset_button.pack(side="right", padx=(0, 10))

# 文本框
textbox_title = ctk.CTkLabel(
    group_box,
    text="Input Text",
    font=FONT_LABEL,
    text_color="#2C2C2C"
)

textbox_title.grid(
    row=3,
    column=0,
    sticky="nw",
    padx=(20, 10),
    pady=(5, 25)
)

textbox = ctk.CTkTextbox(
    group_box,
    width=420,
    height=140,
    corner_radius=10,
    border_width=1,
    border_color="#D8D8DC",
    fg_color="#FFFFFF",
    text_color="#1E1E1E",
    font=FONT_WIDGET
)

textbox.grid(
    row=3,
    column=1,
    columnspan=2,
    sticky="ew",
    padx=(10, 20),
    pady=(5, 25)
)

textbox.insert(
    "1.0",
    "Paste your text here..."
)
#cycling tips
tips = [
    #load
    "Precision-driven simulation environment initialized.",
    "Swing the cursor to pause typing.",
    #commercial
    "Human Typing Simulator Ultra is powered by NT 2.0 Engine",
    "Human Typing Simulator is now available on Windows and MacOS",
    "Purchase Human Typing Simulator Ultra to unlock all features",
    "The latest model is embedded in the NT 2.0 Engine",
    #tips
    "Tip: Place the text box on the right of the screen before pressing go.",
    "Tip: Press Pause at any time to temporarily stop typing.",
    "Tip: Lower Error Rate produces cleaner and more consistent output.",
    "Tip: Dynamic Speed creates more natural typing deceleration.",
    "Tip: Dynamic Error Rate simulates gradual typing fatigue.",
    "Tip: Smaller speed values improve realism for long paragraphs.",
    "Tip: Higher typing speeds may reduce synchronization accuracy.",
    "Tip: Keep the target window visible during active typing.",
    "Tip: Avoid switching applications while typing is running.",
    "Tip: Very high error rates may appear unnatural.",
    "Tip: Most users achieve realistic results with low typo frequency.",
    "Tip: Dynamic systems produce less repetitive typing behavior.",
    "Tip: Input responsiveness may vary between applications.",
    "Tip: Browser-based editors may process keystrokes differently.",
    "Tip: Stable system performance improves timing consistency.",
    "Tip: Background applications may affect typing smoothness.",
    "Tip: Some applications filter synthetic keyboard events.",
    "Tip: Typing simulation works best on focused editable fields.",
    "Tip: Excessive multitasking may interrupt keyboard automation.",
    "Tip: Consistent cursor focus is required for accurate input.",
    "Tip: Realistic automation depends heavily on timing variation.",
    "Tip: Lower speeds generally appear more authentic.",
    "Tip: The simulator automatically handles punctuation delays.",
    "Tip: Small timing fluctuations greatly improve realism.",
    "Tip: Short bursts of speed variation mimic natural typing flow.",
]
# 灰色渐变序列（淡入淡出）
fade_colors = [
    "#D0D0D0",
    "#CACACA",
    "#C4C4C4",
    "#BEBEBE",
    "#B8B8B8",
    "#B2B2B2",
    "#ACACAC",
    "#A6A6A6",
    "#A0A0A0",
    "#9A9A9A",
    "#949494",
    "#8E8E8E",
    "#888888",
    "#828285",
    "#7C7C80",
    "#76767A",
    "#707075",
    "#6E6E73",

    "#707075",
    "#76767A",
    "#7C7C80",
    "#828285",
    "#888888",
    "#8E8E8E",
    "#949494",
    "#9A9A9A",
    "#A0A0A0",
    "#A6A6A6",
    "#ACACAC",
    "#B2B2B2",
    "#B8B8B8",
    "#BEBEBE",
    "#C4C4C4",
    "#CACACA",
    "#D0D0D0"
]
tip_label = ctk.CTkLabel(
    group_box,
    text=tips[0],
    font=("SF Pro Text", 12),
    text_color="#6E6E73"
)

tip_label.grid(row=5,
    column=0,
    columnspan=3,
    pady=(0, 15)
)

fade_index = 0
tip_index = 0

def tip_animation():
    global fade_index, tip_index
    if fade_index < len(fade_colors):
        tip_label.configure( text_color=fade_colors[fade_index])
        fade_index += 1
    else:
        fade_index = 0
        if tip_index < len(tips) - 1:
            tip_index += 1
        else:
            tip_index = 1
        tip_label.configure(text=tips[tip_index])
    root.after(200, tip_animation)
tip_animation()


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

key_map = {
    "a": 0,
    "s": 1,
    "d": 2,
    "f": 3,
    "h": 4,
    "g": 5,
    "z": 6,
    "x": 7,
    "c": 8,
    "v": 9,
    "b": 11,
    "q": 12,
    "w": 13,
    "e": 14,
    "r": 15,
    "y": 16,
    "t": 17,
    "1": 18,
    "2": 19,
    "3": 20,
    "4": 21,
    "6": 22,
    "5": 23,
    "=": 24,
    "9": 25,
    "7": 26,
    "-": 27,
    "8": 28,
    "0": 29,
    "]": 30,
    "o": 31,
    "u": 32,
    "[": 33,
    "i": 34,
    "p": 35,
    "l": 37,
    "j": 38,
    "'": 39,
    "k": 40,
    ";": 41,
    "\\": 42,
    ",": 43,
    "/": 44,
    "n": 45,
    "m": 46,
    ".": 47,
    "`": 50,
    "backspace":51,
    "left":123,
    "right":124,
    "space":49,
    " ":49,
    "down":125,

    #special character
    "?": 44,
    "<": 43,
    ">": 47,
    "+": 24,
    "_": 27,
    ":": 41,
    "\"": 39,
    "{": 33,
    "}": 30,
    "|": 42,
    "~": 50,
    "!": 18,
    "@": 19,
    "#": 20,
    "$": 21,
    "%": 23,
    "^": 22,
    "&": 26,
    "*": 28,
    "(": 25,
    ")": 29,
}

def press_button(char):
    code = key_map[char.lower()]
    if char.isupper() or (char in "!@#$%^&*()_+{}|\\:\"'<>?~`"):
        subprocess.run(["osascript","-e",
        f'''
        tell application "System Events"
            key code {code} using {{shift down}}
        end tell
        '''])
    else:
        subprocess.run(["osascript","-e",
        f'''
        tell application "System Events"
            key code {code}
        end tell
        '''])

def probability(probability):
    if random.uniform(0,100)<probability:
        return True
    else:
        return False

def cursor_initializer():
    global original_mouse_position
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width * 3 / 4,screen_height * 0.8,duration=0.1)
    pyautogui.click()

    subprocess.run(["osascript", "-e",
                    '''
                    tell application "System Events"
                        key code 125 using {command down}
                    end tell
                    '''
                    ])  # 文末定位

    original_mouse_position = pyautogui.position()

cursor_pos = 0
current_word_complete = False

def speed_control(stage,cursor_data_pkg = (0,0),sleep_time = 0):#time elapsed between every letter
    global Speed, Dynamic_Speed, cursor_pos, typo_cursor
    wait_time = 0.2 / Speed
    if stage == "typing":
        if Dynamic_Speed == True:
            wait_time += random.uniform(0,cursor_pos/2000)
        time.sleep(random.uniform(wait_time,wait_time+0.05))

    elif stage == "cursor_move":
        if Dynamic_Speed == True:
            wait_time += random.uniform(0,cursor_pos/2000)
        if cursor_data_pkg[1] - cursor_data_pkg[0] <3:
            wait_time += random.uniform(0.1,0.3)
        time.sleep(wait_time)

    elif stage == "NT20":
        wait_time = 0.05
        if Dynamic_Speed == True:
            wait_time += random.uniform(0,cursor_pos/2000)
        time.sleep(random.uniform(wait_time,wait_time+0.02))

    #debug option
    elif stage == "debug":
        time.sleep(sleep_time)

    #random pause
    if probability(random.uniform(1,1.5)):
        time.sleep(random.uniform(0.3,2))


def detect_break(action = None):
    global is_on, pause_triggered,original_mouse_position,awaiting_current_word_to_finish
    if action == None:
        if is_on == True:
            position = pyautogui.position()
            if (position[0] > original_mouse_position[0] + 30
                or position[1] > original_mouse_position[1] + 30
                or position[0] < original_mouse_position[0] - 30
                or position[1] < original_mouse_position[1] - 30):
                pause_triggered = True

                choice = subprocess.run(
                    ["osascript", "-e",
                     'button returned of (display dialog "Pause?" buttons {"No", "Yes"} default button "Yes")'
                     ], capture_output=True, text=True).stdout.strip()
                if choice == "Yes":

                    choice = subprocess.run(
                        ["osascript", "-e",
                         'button returned of (display dialog "Continue?" buttons {"Exit", "Continue"} default button "Continue")'
                         ], capture_output=True, text=True).stdout.strip()
                    if choice == "Continue":
                        pause_triggered = False
                        cursor_initializer()
                    else:
                        is_on = False
                        pause_triggered = False
                        cursor_initializer()
                        return 0

                else:
                    pause_triggered = False
                    cursor_initializer()

    elif action == "set flag":
        if is_on == True:
            position = pyautogui.position()
            if (position[0] > original_mouse_position[0] + 30
                    or position[1] > original_mouse_position[1] + 30
                    or position[0] < original_mouse_position[0] - 30
                    or position[1] < original_mouse_position[1] - 30):

                awaiting_current_word_to_finish = True
                pause_triggered = True




def type(word_to_print,next_is_char):
    #this block of code deals with non-letter characters including 'enter'
    if word_to_print ==  "\n":
        press_button("enter")
        return 1
    elif ord(word_to_print[0])<65 or ord(word_to_print[0])>122:#special chars
        for i in range(0,len(word_to_print)):
            signal = detect_break()
            if signal == 0:
                return 0
            press_button(word_to_print[i])
            speed_control("typing")
        # press_button("space")
        return 0

    global typo_map,cursor_pos,current_word_complete,\
        Error_rate,Dynamic_err_rate,pause_triggered, err_generator_model,count

    print(err_generator_model)
    current_word_complete = False
    typo_cursor = 0
    location:list[int]
    if Dynamic_err_rate == True:
        Error_rate += cursor_pos/500

    if probability(Error_rate) and len(word_to_print) > 1:

        if hybrid == True and probability(35):
            #NT2.0
            err_generator_model = "NT2.0G"
            def typo_writer(typo_map, total_count, current_count, last_chr):
                while current_count<total_count:
                    possible_typo = typo_map[last_chr]
                    if probability(90):
                        try:
                            typo = random.choice(possible_typo)
                        except KeyError:
                            typo = chr(random.randint(97, 122))
                    else:
                        typo = chr(random.randint(97, 122))

                    press_button(typo)
                    speed_control("NT20")
                    signal = detect_break()
                    if signal == 0:
                        return 0
                    current_count += 1
                    last_chr = typo

            def typo_eraser(total_count):
                for i in range(0, total_count):
                    press_button("backspace")
                    speed_control("NT20")
                    signal = detect_break()
                    if signal == 0:
                        return 0

            def typo_generator(typo_map, total_count, last_chr):
                signal = typo_writer(typo_map, total_count, 0, last_chr)
                if signal == 0:
                    return 0
                speed_control("NT20")
                signal = typo_eraser(total_count)
                if signal == 0:
                    return 0
            NT20cursor_pos = 0

            while NT20cursor_pos<len(word_to_print):
                chars = word_to_print
                if probability(Error_rate):
                    signal = typo_generator(typo_map, random.randint(1, 3), chars[NT20cursor_pos])
                    if signal == 0:
                        break
                    time.sleep(random.uniform(0.1,0.3))
                press_button(chars[NT20cursor_pos])
                NT20cursor_pos += 1
                count += 1

        else:
            #NT3.0
            err_generator_model = "NT3.0"
            numTypos = random.randint(1, int(len(word_to_print)/2))
            location = random.sample(range(0, len(word_to_print)), numTypos)
            location.sort()
            for i in range(0, len(word_to_print)):
                if typo_cursor < len(location) and i == location[typo_cursor]:
                    typo_cursor += 1
                    press_button(random.choice(typo_map[word_to_print[i]]))
                    signal = detect_break()
                    if signal == 0:
                        return 0
                else:
                    press_button(word_to_print[i])
                    signal = detect_break()
                    if signal == 0:
                        return 0
                speed_control("typing")

            # percise correction starts here

            for i in range(0, (len(word_to_print) - location[0]) - 1):
                press_button("left")
                speed_control("cursor_move", (i, (len(word_to_print) - location[0]) - 1))
                detect_break("set flag")
            count = 0
            while count < len(location):
                # erase and write
                press_button("backspace")
                time.sleep(random.uniform(0.1, 0.3))
                press_button(word_to_print[location[count]])
                detect_break("set flag")

                # skip cursor move for the last correction
                if count == len(location) - 1:
                    count += 1
                    continue

                # move to next error loc
                for i in range(location[count + 1] - location[count]):
                    press_button("right")
                    speed_control("cursor_move", (i, location[count + 1] - location[count]))
                    detect_break("set flag")
                count += 1

            # move to the end of the current word
            for i in range(len(word_to_print) - location[len(location) - 1] - 1):
                press_button("right")
                detect_break("set flag")
                speed_control("cursor_move", (i, len(word_to_print) - location[len(location) - 1] - 1))

            #pauses only after typing+erasing is complete
            global awaiting_current_word_to_finish

            choice = subprocess.run(
                ["osascript", "-e",
                 'button returned of (display dialog "Pause?" buttons {"No", "Yes"} default button "Yes")'
                 ], capture_output=True, text=True).stdout.strip()
            if choice == "Yes":

                choice = subprocess.run(
                    ["osascript", "-e",
                     'button returned of (display dialog "Continue?" buttons {"Exit", "Continue"} default button "Continue")'
                     ], capture_output=True, text=True).stdout.strip()
                if choice == "Continue":
                    pause_triggered = False
                    cursor_initializer()
                else:
                    is_on = False
                    pause_triggered = False
                    cursor_initializer()
                    return 0

            else:
                pause_triggered = False
                cursor_initializer()


    else:
        err_generator_model = "NT3.0"
        for i in range(0,len(word_to_print)):
            press_button(word_to_print[i])
            signal = detect_break()
            if signal == 0:
                return 0
            speed_control("typing")

    # if next_is_char and word_to_print != "\n":
    #     signal = detect_break()
    #     if signal == 0:
    #         return 0
    #     press_button("space")
    #     speed_control("typing")
    # else:
    #     return 0

def typing_thrd():
    global is_on, cursor_pos, chars,\
        resume, count, text_changed, \
        Speed, Error_rate, Dynamic_Speed, \
        Dynamic_err_rate,text,original_mouse_position, \
        pause_triggered,turn_off

    while not turn_off:

        if cursor_pos == len(text) and len(text) > 0: #end when complete
            is_on = False
            cursor_pos = 0
            textbox.configure(state = "normal")

        next_is_char:bool  #下一个字节是否是字母
        if cursor_pos+1 > len(text)-1:
            next_is_char = False
        elif ord(text[cursor_pos+1][0]) <65 or ord(text[cursor_pos+1][0])>122:
            next_is_char = False
        else:
            next_is_char = True

        if is_on == True:
            type(text[cursor_pos],next_is_char)
            cursor_pos += 1

        time.sleep(0) #this prevents the GUI from freezing


#below are the execution lines
def debug():
    global awaiting_current_word_to_finish,pause_mode
    while not turn_off:

        time.sleep(0.1)

debug_thread = threading.Thread(target=debug)
debug_thread.start()
typing_thread = threading.Thread(target = typing_thrd)
typing_thread.start()
root.protocol("WM_DELETE_WINDOW", Exit)
root.mainloop()
# typing_thread.join()


