import pyautogui
import subprocess
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

cursor_initializer()