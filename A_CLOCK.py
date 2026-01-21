import tkinter as tk
import time
import math

# Clock settings
WIDTH = 400
HEIGHT = 400
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
RADIUS = 180

# Create main window
root = tk.Tk()
root.title("Analog Clock")

# Create canvas
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='white')
canvas.pack()

def draw_clock_face():
    canvas.create_oval(CENTER_X - RADIUS, CENTER_Y - RADIUS,
                       CENTER_X + RADIUS, CENTER_Y + RADIUS, width=7)

    for i in range(1, 13):
        angle = math.radians(i * 30)
        x = CENTER_X + RADIUS * 0.9 * math.sin(angle)
        y = CENTER_Y - RADIUS * 0.9 * math.cos(angle)
        canvas.create_text(x, y, text=str(i), font=("Helvetica", 16, "bold"))
        
    for i in range(12):
        angle = math.radians(i * 30)
        x_outer = CENTER_X + RADIUS * 0.82 * math.sin(angle)
        y_outer = CENTER_Y - RADIUS * 0.82 * math.cos(angle)
        x_inner = CENTER_X + RADIUS * 0.7 * math.sin(angle)
        y_inner = CENTER_Y - RADIUS * 0.7 * math.cos(angle)
        canvas.create_line(x_inner, y_inner, x_outer, y_outer, width=8)


def update_clock():
    canvas.delete("hands")

    # Current time
    now = time.localtime()
    sec = now.tm_sec
    min = now.tm_min
    hr = now.tm_hour % 12 + min / 60.0

    # Compute angles
    sec_angle = math.radians(sec * 6)
    min_angle = math.radians(min * 6)
    hr_angle = math.radians(hr * 30)

    # Hand lengths
    sec_length = RADIUS * 0.8
    min_length = RADIUS * 0.55
    hr_length = RADIUS * 0.3

    # Second hand
    x_sec = CENTER_X + sec_length * math.sin(sec_angle)
    y_sec = CENTER_Y - sec_length * math.cos(sec_angle)
    canvas.create_line(CENTER_X, CENTER_Y, x_sec, y_sec, fill='red', width=6, tag="hands")

    # Minute hand
    x_min = CENTER_X + min_length * math.sin(min_angle)
    y_min = CENTER_Y - min_length * math.cos(min_angle)
    canvas.create_line(CENTER_X, CENTER_Y, x_min, y_min, fill='blue', width=8, tag="hands")

    # Hour hand
    x_hr = CENTER_X + hr_length * math.sin(hr_angle)
    y_hr = CENTER_Y - hr_length * math.cos(hr_angle)
    canvas.create_line(CENTER_X, CENTER_Y, x_hr, y_hr, fill='black', width=10, tag="hands")

    root.after(1000, update_clock)  # Call again after 1 second

# Run
draw_clock_face()
update_clock()
root.mainloop()
