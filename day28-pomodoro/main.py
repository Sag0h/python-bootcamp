from tkinter import *
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
CHECK_SYMBOL = "✔"
timer = None
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    window.after_cancel(timer)
    title_lb.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    check_lb.config(text="")
    reps = 0
    start_button.grid(column=0, row=2)
# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    start_button.grid_remove()
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps <= 8:
        if reps % 2 == 0:
            check_lb.config(text=check_lb.cget("text")+CHECK_SYMBOL)
            if reps < 8:
                time = short_break_sec
                title_lb.config(text="Break", fg=PINK)
            else:
                title_lb.config(text="Break", fg=RED)
                time = long_break_sec
                reps = 0
        else:
            title_lb.config(text="Work", fg=GREEN)
            time = work_sec

        count_down(time)
    else:
        reset_timer()
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

def count_down(count):
    global timer
    count_min = math.floor(count / 60)
    count_sec = math.floor(count % 60)
    if count_min < 10:
        count_min = f"0{count_min}"
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


title_lb = Label(text="Timer", bg=YELLOW, font=(FONT_NAME, 35, "bold"), fg=GREEN)
title_lb.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file=r"C:\Users\mique\OneDrive\Escritorio\python-bootcamp\day28-pomodoro\tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 132, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

#THIS INVISIBLE LABEL IS HERE BC WHEN WE REMOVE THE START BUTTON, THE GRID GETS SMALLER AND THE WINDOW SIZE TOO
invisible_lb = Label(text="         ",bg=YELLOW)
invisible_lb.grid(column=0, row=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_lb = Label(text="", fg=GREEN, bg= YELLOW, font=(FONT_NAME, 15, "bold"))
check_lb.grid(column=1, row=4)



window.mainloop()