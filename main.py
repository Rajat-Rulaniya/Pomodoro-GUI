from tkinter import *

GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
checkbox = "✅"
checkbox_count = 0
reps = 0
slot_number = 0
timer = None
start_button_clicked_times = 0


def reset_timer():
    global reps, checkbox_count, slot_number, start_button_clicked_times
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text=f"{WORK_MIN}:00")
    reps = 0
    start_button_clicked_times = 0
    checkbox_count = 0
    checkbox_display.config(text="")

    slot_number = 0
    slot1_label.config(text="")
    slot2_label.config(text="")
    slot3_label.config(text="")
    pomodoro_timer_label.config(font=(FONT_NAME, 25, 'bold'), text="Pomodoro-Timer", bg='#FFF2D8')


def start_button_clicked():
    global start_button_clicked_times
    if start_button_clicked_times == 0:
        start_button_clicked_times += 1
        start_timer()


def start_timer():
    global reps, checkbox_count, slot_number

    if slot_number == 3:
        window.after(2000, reset_screen)

    else:
        reps += 1
        work_min_sec = WORK_MIN * 60
        short_break_sec = SHORT_BREAK_MIN * 60
        long_break_sec = LONG_BREAK_MIN * 60
        if reps % 2 != 0:
            count_sec = work_min_sec
            checkbox_count += 1
            pomodoro_timer_label.config(font=(FONT_NAME, 25, 'bold'), text="   Work-Time   ", bg='white', fg='black')
        elif reps % 8 == 0:
            slot_number += 1
            count_sec = long_break_sec
            reps = 0
            checkbox_count = 0
            pomodoro_timer_label.config(font=(FONT_NAME, 25, 'bold'), text="  Long_Break  ", bg='white', fg='red')
            if slot_number == 1:
                slot1_label.grid(row=4, column=0)
            elif slot_number == 2:
                slot2_label.grid(row=4, column=1)
            elif slot_number == 3:
                slot3_label.grid(row=4, column=2)
        elif reps % 2 == 0:
            count_sec = short_break_sec
            pomodoro_timer_label.config(font=(FONT_NAME, 25, 'bold'), text="  Break-Time  ", bg='white', fg='red')

        window.after(0, count_down, count_sec, checkbox_count)


def blink_completed(times_blink, show_text):
    if times_blink > 0:
        if show_text:
            canvas.itemconfig(timer_text, text="Completed!", font=(FONT_NAME, 14, 'bold'))
        else:
            canvas.itemconfig(timer_text, text="", font=(FONT_NAME, 14, 'bold'))
            times_blink += 1
        window.after(500, blink_completed, times_blink - 1, not show_text)


def count_down(count, checkbox_count):
    global timer
    min_count = count // 60
    sec_count = count % 60

    if min_count <= 0 and sec_count <= 0:
        blink_completed(4, True)
        checkbox_display.config(text=f"{checkbox * checkbox_count}")
        window.after(4000, start_timer)

    else:
        if sec_count < 10:
            sec_count = f"0{sec_count}"
        canvas.itemconfig(timer_text, text=f"{min_count}:{sec_count}", font=(FONT_NAME, 25, 'bold'))
        timer = window.after(1000, count_down, count - 1, checkbox_count)


def reset_screen():
    canvas.delete("all")
    slot1_label.grid_forget()
    slot2_label.grid_forget()
    slot3_label.grid_forget()
    pomodoro_timer_label.grid_forget()
    start_button.grid_forget()
    reset_button.grid_forget()
    ending_label = Label(window, text="It Was a Productive Day!, right?", font=(FONT_NAME, 25, 'bold'), fg='black',
                         bg='white')
    ending_label.grid(row=1, column=1)


window = Tk()
window.title(string="Pomodoro GUI application")
window.minsize(width=1000, height=500)
window.config(padx=100, pady=100, bg="#B6FFFA")

canvas = Canvas(width=210, height=224, bg="#B6FFFA", highlightthickness=0)

img = PhotoImage(file="tomato.png")

canvas.create_image(110, 112, image=img)

timer_text = canvas.create_text(110, 135, text=f"{WORK_MIN}:00", font=(FONT_NAME, 25, "bold"), fill="White")

pomodoro_timer_label = Label(window, font=(FONT_NAME, 25, 'bold'), text="Pomodoro-Timer", bg='#FFF2D8')

pomodoro_timer_label.grid(row=0, column=1)

slot1_label = Label(window, text="Slot1✔", font=(FONT_NAME, 15, "bold"), bg="#0C356A", width=7, fg='white')
slot2_label = Label(window, text="Slot2✔", font=(FONT_NAME, 15, "bold"), bg="#0C356A", width=7, fg='white')
slot3_label = Label(window, text="Slot3✔", font=(FONT_NAME, 15, "bold"), bg="#0C356A", width=7, fg='white')

canvas.grid(row=1, column=1)

start_button = Button(window, text="Start", highlightthickness=0, font=(FONT_NAME, 14, "bold"), bg="#79AC78",
                      fg="white", command=start_button_clicked)
start_button.grid(row=2, column=0)

reset_button = Button(window, text="Reset", highlightthickness=0, font=(FONT_NAME, 14, "bold"), command=reset_timer)
reset_button.grid(row=2, column=2)

checkbox_display = Label(bg="#B6FFFA", font=(FONT_NAME, 20, "normal"), fg="#1A5D1A")
checkbox_display.grid(row=3, column=1)

window.mainloop()
