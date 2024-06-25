# import the necessary libraries

from tkinter import *
import time
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
BLACK = "#323232"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
timer = None


# create the functions that will perform
def start_timer():
    global REPS, TICKS
    REPS += 1

    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        status.config(text="Break", fg=RED)

    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        status.config(text="Break", fg=PINK)
    else:
        count_down(WORK_MIN * 60)
        status.config(text="Work")


def reset_timer():
    global REPS

    tk.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    status.config(text="Timer", fg=GREEN)
    tick.config("")
    REPS = 0


def count_down(seconds_left):
    global timer
    minutes = math.floor(seconds_left / 60)
    seconds = seconds_left % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")

    if seconds_left >= 0:
        timer = tk.after(1000, count_down, seconds_left - 1)
    else:
        start_timer()

        if REPS % 2 == 0:
            tick.config(text=f"{'✔' * math.floor(REPS / 2)}")


# create and configure the UI

tk = Tk()

tk.title("POMODORO!")
tk.config(padx=100, pady=50, bg=BLACK)
tk.resizable(False, False)

tomato_photo = PhotoImage(file="data/day28_tomato.png")

canvas = Canvas(width=210, height=224, bg=BLACK, highlightthickness=0)
canvas.create_image(105, 112, image=tomato_photo)
timer_text = canvas.create_text(110, 130, text="00:00", fill="White", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# add the command buttons

start_button = Button(text="Start", highlightthickness=0, bg=GREEN, command=start_timer)
start_button.grid(row=2, column=0)

restart_button = Button(text="Restart", highlightthickness=0, bg=BLACK, command=reset_timer)
restart_button.grid(row=2, column=2)

tick = Label(bg=BLACK, fg=GREEN, font=(FONT_NAME, 50, "bold"))
tick.grid(row=3, column=1)

status = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=BLACK, fg=GREEN)
status.grid(row=0, column=1)

tk.mainloop()
