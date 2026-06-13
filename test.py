import ctypes

result = ctypes.windll.user32.MessageBoxW(
    0,
    "Pause?",
    "Human Typing Simulator",
    0x04 | 0x20  # MB_YESNO | MB_ICONQUESTION
)