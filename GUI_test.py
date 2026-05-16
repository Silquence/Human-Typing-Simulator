import customtkinter as ctk

Error_rate = 2
Speed = 10
Dynamic_err_rate = False
Dynamic_Speed = False

def slider_color(value):
    value = float(value)
    if value <= 30:
        ratio = value / 30
        r = int(0 + (255 * ratio))
        g = int(200 - (35 * ratio))
        b = 0
    else:
        ratio = (value - 30) / 70
        r = 255
        g = int(165 - (165 * ratio))
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
title_label = ctk.CTkLabel(
    main_frame,
    text="Typing Configuration",
    font=("Segoe UI", 26, "bold")
)
title_label.pack(pady=(20, 25))

# Error Rate Slider
err_rate_title = ctk.CTkLabel(
    main_frame,
    text="Error Rate",
    font=("Segoe UI", 16)
)
err_rate_title.pack(anchor="w", padx=30)

def get_err_rate(value):
    global Error_rate
    Error_rate = value
    err_rate_slider.configure(
        progress_color=slider_color(value)
    )
    print(Error_rate)

err_rate_slider = ctk.CTkSlider(
    main_frame,
    from_=0,
    to=100,
    command=get_err_rate
)

err_rate_slider.set(Error_rate)
err_rate_slider.configure(
    progress_color=slider_color(Error_rate)
)
err_rate_slider.pack(
    fill="x",
    padx=30,
    pady=(5, 20)
)

# Speed Slider
speed_title = ctk.CTkLabel(
    main_frame,
    text="Typing Speed",
    font=("Segoe UI", 16)
)
speed_title.pack(anchor="w", padx=30)
def get_speed(value):
    global Speed
    Speed = value
    speed_slider.configure(
        progress_color=slider_color(value)
    )
    print(Speed)
speed_slider = ctk.CTkSlider(
    main_frame,
    from_=0,
    to=100,
    command=get_speed
)
speed_slider.set(Speed)
speed_slider.configure(
    progress_color=slider_color(Speed)
)
speed_slider.pack(
    fill="x",
    padx=30,
    pady=(5, 30)
)

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

root.mainloop()