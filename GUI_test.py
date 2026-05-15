import customtkinter as ctk

def on_click():
    print("button clicked")


root = ctk.CTk()
root.geometry("300x200")

button = ctk.CTkButton(
    root,
    text="Click Me",
    command=on_click
)

button.pack(pady=60)

root.mainloop()