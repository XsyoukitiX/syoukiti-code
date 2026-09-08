#2026/9/7
import tkinter as tk

window = tk.Tk()
window.title("GAME")
window.geometry("500x300")

canvas = tk.Canvas(window, width=500, height=300)
canvas.pack()

canvas.create_rectangle(100, 50, 200, 150)

canvas.create_polygon(150, 100, 160, 110, 150, 120, 140, 110, fill="red")

def move(event):
    if event.keysym == "Up":
        canvas.move(player, 0, -10)
    elif event.keysym == "Down":
        canvas.move(player, 0, 10)
    elif event.keysym == "Left":
        canvas.move(player, -10, 0)
    elif event.keysym == "Right":
        canvas.move(player, 10, 0)


window.mainloop()