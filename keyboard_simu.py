import pyautogui
import time
import random
import customtkinter as ctk
import threading
import sys
import ctypes

# 保持原有的后端全局变量和逻辑不动
Error_rate = 2
Speed = 10
Dynamic_err_rate = False
Dynamic_Speed = False
max_rate = 20
is_on = False  # 打字器状态
turn_off = False  # 程序状态


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

<<<<<<< HEAD

=======
>>>>>>> 374116b7e12fe7b69fc77a4e36b0926206454f82
# --- macOS Tahoe 风格 UI 初始化 ---
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

<<<<<<< HEAD
# Tahoe 标准现代浅色基调
=======
# Tahoe 标准现代浅色基调 (轻铝灰)
>>>>>>> 374116b7e12fe7b69fc77a4e36b0926206454f82
TAHOE_BG = "#F3F3F3"
TAHOE_CARD_BG = "#FAFAFA"

root = ctk.CTk()
root.title("Human Typing Simulator")
<<<<<<< HEAD
root.geometry("640x620")
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
title_label = ctk.CTkLabel(
    main_frame,
    text="Typing Configuration",
    font=FONT_TITLE,
    text_color="#1E1E1E"
)
title_label.pack(pady=(5, 20), anchor="w")

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

=======
root.geometry("640x440")
root.resizable(False, False)
root.configure(fg_color=TAHOE_BG)

# 字体设置
FONT_TITLE = ("SF Pro Display", 20, "bold")
FONT_LABEL = ("SF Pro Text", 13, "bold")
FONT_VALUE = ("SF Pro Text", 13, "normal")
FONT_WIDGET = ("SF Pro Text", 13)

# 主容器：
main_frame = ctk.CTkFrame(root, corner_radius=0, fg_color=TAHOE_BG)
main_frame.pack(padx=30, pady=25, fill="both", expand=True)

#顶部标题，左对齐
title_label = ctk.CTkLabel(main_frame, text="Typing Configuration", font=FONT_TITLE, text_color="#1E1E1E")
title_label.pack(pady=(5, 20), anchor="w")

#卡片式分组框
group_box = ctk.CTkFrame(main_frame, corner_radius=14, fg_color=TAHOE_CARD_BG, border_width=0)
group_box.pack(fill="both", expand=True, pady=(0, 15))

# 内部间距与权重配置
group_box.grid_columnconfigure(0, weight=1)
group_box.grid_columnconfigure(1, weight=5)
group_box.grid_columnconfigure(2, weight=1)

# --- 1. ERROR RATE 控制行 ---
err_title = ctk.CTkLabel(group_box, text="Error Rate", font=FONT_LABEL, text_color="#2C2C2C")
err_title.grid(row=0, column=0, sticky="w", padx=(20, 10), pady=(25, 12))
>>>>>>> 374116b7e12fe7b69fc77a4e36b0926206454f82

def get_err_rate(value):
    global Error_rate
    Error_rate = value
<<<<<<< HEAD

    err_rate_slider.configure(
        progress_color=slider_color(value, max_rate)
    )

    err_value_label.configure(
        text=f"{value:.1f}"
    )

    print(Error_rate)


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

=======
    err_rate_slider.configure(progress_color=slider_color(value, max_rate))
    err_value_label.configure(text=f"{value:.1f}")
    print(Error_rate)

err_rate_slider = ctk.CTkSlider(
    group_box, from_=0, to=max_rate, number_of_steps=200, command=get_err_rate,
    fg_color="#E2E2E7",        #填充轨底色
    button_color="#FFFFFF",     #滑块颜色
    button_hover_color="#F5F5F7",
    height=5,                  #条状滑块粗细
    border_width=1,
    border_color="#D8D8DC"     #滑块描边
)
err_rate_slider.set(Error_rate)
err_rate_slider.configure(progress_color=slider_color(Error_rate, max_rate))
err_rate_slider.grid(row=0, column=1, sticky="ew", padx=10, pady=(25, 12))

err_value_label = ctk.CTkLabel(group_box, text=f"{Error_rate:.1f}", font=FONT_VALUE, text_color="#6E6E73", width=40, anchor="w")
err_value_label.grid(row=0, column=2, sticky="w", padx=(10, 20), pady=(25, 12))


# --- 2. TYPING SPEED 控制行 ---
speed_title = ctk.CTkLabel(group_box, text="Typing Speed", font=FONT_LABEL, text_color="#2C2C2C")
speed_title.grid(row=1, column=0, sticky="w", padx=(20, 10), pady=12)
>>>>>>> 374116b7e12fe7b69fc77a4e36b0926206454f82

def get_speed(value):
    global Speed
    Speed = value
<<<<<<< HEAD

    speed_slider.configure(
        progress_color=slider_color(value, max_rate)
    )

    speed_value_label.configure(
        text=f"{value:.1f}"
    )

    print(Speed)


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
=======
    speed_slider.configure(progress_color=slider_color(value, max_rate))
    speed_value_label.configure(text=f"{value:.1f}")
    print(Speed)

speed_slider = ctk.CTkSlider(
    group_box, from_=1, to=max_rate, number_of_steps=190, command=get_speed,
    fg_color="#E2E2E7", button_color="#FFFFFF", button_hover_color="#F5F5F7",
    height=5, border_width=1, border_color="#D8D8DC"
)
speed_slider.set(Speed)
speed_slider.configure(progress_color=slider_color(Speed, max_rate))
speed_slider.grid(row=1, column=1, sticky="ew", padx=10, pady=12)

speed_value_label = ctk.CTkLabel(group_box, text=f"{Speed:.1f}", font=FONT_VALUE, text_color="#6E6E73", width=40, anchor="w")
speed_value_label.grid(row=1, column=2, sticky="w", padx=(10, 20), pady=12)


# --- 3. DYNAMIC SWITCHES 控制行 ---
>>>>>>> 374116b7e12fe7b69fc77a4e36b0926206454f82
def toggle_t1():
    global Dynamic_err_rate
    Dynamic_err_rate = not Dynamic_err_rate
    print(Dynamic_err_rate)


def toggle_t2():
    global Dynamic_Speed
    Dynamic_Speed = not Dynamic_Speed
    print(Dynamic_Speed)

<<<<<<< HEAD

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
    text="Enable Dynamic Speed Window",
    command=toggle_t2,
    font=FONT_WIDGET,
    text_color="#2C2C2C",
    progress_color="#34C759",
    fg_color="#E2E2E7"
)
=======
switch_frame = ctk.CTkFrame(group_box, fg_color="transparent")
switch_frame.grid(row=2, column=1, columnspan=2, sticky="w", padx=10, pady=(15, 25))

toggle_t1_button = ctk.CTkSwitch(
    switch_frame, text="Enable Dynamic Error Rate", command=toggle_t1,
    font=FONT_WIDGET, text_color="#2C2C2C",
    progress_color="#34C759",
    fg_color="#E2E2E7"
)
toggle_t1_button.pack(anchor="w", pady=6)

toggle_t2_button = ctk.CTkSwitch(
    switch_frame, text="Enable Dynamic Speed", command=toggle_t2,
    font=FONT_WIDGET, text_color="#2C2C2C",
    progress_color="#34C759",
    fg_color="#E2E2E7"
)
toggle_t2_button.pack(anchor="w", pady=6)


# --- 底部动作栏 ---
bottom_frame = ctk.CTkFrame(main_frame, fg_color="transparent")
bottom_frame.pack(fill="x", side="bottom", pady=(5, 5))

def confirm_speed():
    speed_slider.configure(state="disabled")
    root.destroy()

confirm_speed_button = ctk.CTkButton(
    bottom_frame,
    text="Done",
    command=confirm_speed,
    width=80,
    height=30,
    corner_radius=8,
    fg_color="#007AFF",
    hover_color="#0066CC",
    font=("SF Pro Text", 13, "bold")
)
confirm_speed_button.pack(side="right")
>>>>>>> 374116b7e12fe7b69fc77a4e36b0926206454f82

toggle_t2_button.pack(anchor="w", pady=6)

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
    with open("cache.txt", "w") as cache:
        content = textbox.get("1.0", "end-1c")
        cache.write(content)

    speed_slider.configure(state="disabled")
    time.sleep(0.5)
    cursor_initializer()

    global is_on
    is_on = True


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


def pause():
    global is_on
    is_on = False


pause_button = ctk.CTkButton(
    bottom_frame,
    text="Pause",
    command=pause,
    width=80,
    height=30,
    corner_radius=8,
    fg_color="#007AFF",
    hover_color="#0066CC",
    font=("SF Pro Text", 13, "bold")
)

pause_button.pack(side="right", padx=(0, 10))


def Exit():
    global turn_off
    turn_off = True
    root.destroy()


Exit_button = ctk.CTkButton(
    bottom_frame,
    text="Exit",
    command=Exit,
    width=80,
    height=30,
    corner_radius=8,
    fg_color="#007AFF",
    hover_color="#0066CC",
    font=("SF Pro Text", 13, "bold")
)

Exit_button.pack(side="right", padx=(0, 10))

# ================= TEXTBOX CODE BELOW ====================
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

# below is the backend code
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
    # special characters
    " ": [" "],
    ",": ["."],
    ".": [","],
    "?": ["/"]
}


def cursor_initializer():
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width * 3 / 4, screen_height * 0.8)
    pyautogui.click()
    pyautogui.hotkey("ctrl", "end")
    time.sleep(0.5)


def probability(probability):
    if random.uniform(0, 100) < probability:
        return True
    else:
        return False


def typo_writer(typo_map, total_count, current_count, last_chr):
    if current_count < total_count:
        possible_typo = typo_map[last_chr]
        if probability(90):
            try:
                typo = random.choice(possible_typo)
            except KeyError:
                typo = chr(random.randint(97, 122))
        else:
            typo = chr(random.randint(97, 122))
        pyautogui.write(typo)
        current_count += 1
        typo_writer(typo_map, total_count, current_count, typo)


def typo_eraser(total_count, pause_time):
    for i in range(0, total_count):
        pyautogui.press("backspace")
    time.sleep(pause_time)


def typo_generator(typo_map, total_count, last_chr, rate):
    if probability(rate):
        typo_writer(typo_map, total_count, 0, last_chr)
        time.sleep(0.17)
        typo_eraser(total_count, 0.17)


def speed_control(speed, pause_rate, last_chr):  # 0-10
    if probability(pause_rate):
        time.sleep(random.uniform(0.1, 1.5))
    if last_chr in [",", ".", "?", " "]:
        time.sleep(random.uniform(3 / speed, 5 / speed))


cursor_pos = 0
chars: list[str]
resume = False
count = 0
text_changed = False


def type():
    global is_on, cursor_pos, chars, resume, count, text_changed, Speed, Error_rate, Dynamic_Speed, Dynamic_err_rate

    # refresh full texts every time
    with open("cache.txt", "r") as f:
        global chars
        chars = list(f.read())
    typo_generator(typo_map, random.randint(1, 4), chars[cursor_pos], Error_rate)
    pyautogui.write(chars[cursor_pos])
    speed_control(Speed, 2, chars[cursor_pos])
    count += 1
    cursor_pos += 1


def typing_thrd():
    global is_on, cursor_pos, chars, resume, count, text_changed, Speed, Error_rate, Dynamic_Speed, Dynamic_err_rate
    while True and (not turn_off):
        time.sleep(0.01)

        with open("cache.txt", "r") as f:
            if count == len(f.read()):
                is_on = False
                count = 0
                cursor_pos = 0
                Error_rate = 2
                Speed = 10

        if is_on == True:
            type()
            print(Error_rate)
            print(Speed)
            if Dynamic_err_rate:
                Error_rate += random.uniform(0.00001, 0.00005)
            if Dynamic_Speed:
                Speed += random.uniform(0.00001, 0.00005)


typing_thread = threading.Thread(target=typing_thrd)

# below is the execution code
root.protocol("WM_DELETE_WINDOW", Exit)
typing_thread.start()
root.mainloop()









