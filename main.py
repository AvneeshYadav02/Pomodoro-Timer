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
reps = 0
check_mark_number = 1
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    window.after_cancel(timer)
    check_mark.config(text="")
    heading.config(text="POMODORO")
    global reps
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps

    work_sec = WORK_MIN*60
    short_break_sec = SHORT_BREAK_MIN*60
    long_break_sec = LONG_BREAK_MIN*60
    ticks = int(reps/2+1)
    
    if reps%2==0:
        heading.config(text="WORK TIME", fg=RED)
        check_mark.config(text="✓"*(ticks))
        count_down(10)
        reps +=1
    elif reps%7==0:
        heading.config(text="LONG BREAK", fg=GREEN)
        count_down(8)
        reps+=1
    else:
        heading.config(text="SHORT BREAK", fg=PINK)
        count_down(5)
        reps+=1

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global timer
    count_min = math.floor(count/60)
    count_sec = count%60

    if count_sec in range(10):
        count_sec = f"0{count_sec}"
    if count_min in range(10):
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count>0:
        timer = window.after(1000, count_down, count-1)
    else:
        start_timer()
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100,112, image=tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", fill="white", font=(FONT_NAME, 20, "bold"))
canvas.grid(column=1, row=1)

heading = Label(text="POMODORO", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
heading.grid(column=1, row=0)

check_mark = Label(text=" ", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 20, "bold"))
check_mark.grid(column=1, row=3)

start_button = Button(text="START", bg=PINK, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="RESET", bg=PINK, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()
