from tkinter import *
import time
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- # 
def reset():
    global timer
    screen.after_cancel(timer)
    global reps
    reps = 1
    label_check.config(text="")
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps == 1 or reps % 2 != 0:
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)
    elif reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    min = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{min}:{seconds}")
    if count > 0:
        global timer
        timer = screen.after(1000, count_down, count - 1)
    else:
        start()
        global reps
        mark = ""
        for _ in range(math.floor(reps / 2)):
            mark += "✔"
        label_check.config(text=mark)

# ---------------------------- UI SETUP ------------------------------- #
screen = Tk()
screen.title("Pomodoro")
screen.config(padx=100, pady=50, bg=YELLOW)

title_label = Label(text="Timer", bg=YELLOW)
title_label.config(fg=GREEN, font=(FONT_NAME, 35, "bold"))
title_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

button_1 = Button(text="Start", highlightthickness=0, command=start)
button_1.grid(column=0, row=2)

label_check = Label(bg=YELLOW, fg=GREEN)
label_check.grid(column=1, row=3)

button_2 = Button(text="Reset", highlightthickness=0, command=reset)
button_2.grid(column=2, row=2)


screen.mainloop()