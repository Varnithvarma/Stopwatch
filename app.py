import tkinter as tk
import time

def start_timer():
    start_time = time.time()
    update_timer()

def stop_timer():
    global running
    running = False

def reset_timer():
    global start_time
    start_time = time.time()
    label.config(text="00:00:00")

def update_timer():
    elapsed_time = int(time.time() - start_time)
    minutes, seconds = divmod(elapsed_time, 60)
    hours, minutes = divmod(minutes, 60)
    time_string = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    label.config(text=time_string)
    if running:
        root.after(1000, update_timer)


root = tk.Tk()
root.title("Stopwatch")

label = tk.Label(root, text="00:00:00", font="Helvetica 50")
label.pack()

start_button = tk.Button(root, text="Start", command=start_timer)
start_button.pack()

stop_button = tk.Button(root, text="Stop", command=stop_timer)
stop_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_timer)
reset_button.pack()

running = False
start_time = time.time()

root.mainloop()
