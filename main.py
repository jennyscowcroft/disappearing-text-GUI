import tkinter as tk

# Variable to store the entered text to compare against future text box contents
text_entry = ""
timer = 5


# Erase text in notepad and reset timer
def delete_text():
    global timer
    textbox.delete('1.0', tk.END)
    textbox.focus()
    timer = 5


# Check if text in textbox has changed. Decrease countdown if it hasn't, reset timer if it has.
def check_activity():
    global timer, text_entry
    timer_text.config(text=timer)
    if text_entry == textbox.get(1.0, tk.END):
        if timer == 1:
            window.after(1000, delete_text)
        window.after(1000, check_activity)
        timer -= 1
    else:
        timer = 5
        text_entry = textbox.get(1.0, tk.END)
        window.after(1000, check_activity)


# GUI
# Initialise window
window = tk.Tk()
window.title("Disappearing Text Notepad")
window.minsize(400, 700)

# Format tkinter window
title = tk.Label(window, text="Disappearing Text Notepad", font=("Helvetica", 18))
title.grid(row=0, column=1)

description = tk.Label(window, text="Your text will disappear after 5 seconds of inactivity", font=("Helvetica", 12))
description.grid(row=1, column=1)

timer_text = tk.Label(window, text="5", font=("Helvetica", 12, "bold"), padx=10)
timer_text.grid(row=2, column=1)

textbox = tk.Text(height=35, width=50)
textbox.grid(row=3, column=1, padx=10, pady=10)
textbox.focus()

reset_button = tk.Button(text="Reset Text", command=delete_text)
reset_button.grid(row=4, column=1, pady=10)

check_activity()
window.mainloop()
