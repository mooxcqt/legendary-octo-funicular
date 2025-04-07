import pygame
from PIL import Image, ImageTk
import tkinter as tk

root = tk.Tk()
root.title("shirmp detecor")
root.geometry("700x500+300+100")

image = Image.open("shrimp.jpeg")
resized_image = image.resize((700, 500))
bg_image = ImageTk.PhotoImage(resized_image)

bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

title_label = tk.Label(root, text="Shrimp detector", font=("Arial", 45)) 
title_label.place(x=140, y=130)


def shrimp_detected():
    shrimp_window = tk.Toplevel(root)
    shrimp_window.title("SHIRMOSP!!!!!!!!!!!!!!!!!!!!!!")
    shrimp_window.geometry("700x500+300+100")

    pygame.mixer.init()
    pygame.mixer.music.load("cat-laugh-meme-1.mp3")
    pygame.mixer.music.play()

    point = Image.open("shrimp_point.jpg")
    resized_point = point.resize((700, 500))
    bg_shrimp = ImageTk.PhotoImage(resized_point)

    bg_label1 = tk.Label(shrimp_window, image=bg_shrimp) 
    bg_label1.image = bg_shrimp 
    bg_label1.place(relwidth=1, relheight=1) 


def krill():
    krill_window = tk.Toplevel(root)
    krill_window.title("no shiromp")
    krill_window.geometry("700x500+300+100")

    pygame.mixer.init()
    pygame.mixer.music.load("tuco-get-out.mp3")
    pygame.mixer.music.play()

    krill = Image.open("krill_issue.jpeg")
    resized_krill = krill.resize((700, 500))
    bg_krill = ImageTk.PhotoImage(resized_krill)

    bg_label2 = tk.Label(krill_window, image=bg_krill) 
    bg_label2.image = bg_krill 
    bg_label2.place(relwidth=1, relheight=1) 

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("detectoring...")
    new_window.geometry("300x150+500+270")

    quiz_label = tk.Label(new_window, text="Are you shirmp?")
    quiz_label.place(x=106, y=50)

    yesbutt = tk.Button(new_window, text="yers", command=shrimp_detected, width=8, height=1)
    yesbutt.place(x=75, y=80)

    nobutt = tk.Button(new_window, text="nahr", command=krill, width=8, height=1)
    nobutt.place(x=150, y=80)

start = tk.Button(root, text="start detectored", command=open_new_window, width=25, height=1)
start.place(x=260, y=345)

def on_press(event):
    root.x = event.x
    root.y = event.y

def on_drag(event):
    x = root.winfo_x() + (event.x - root.x)
    y = root.winfo_y() + (event.y - root.y)
    root.geometry(f"+{x}+{y}")

root.bind("<ButtonPress-1>", on_press)
root.bind("<B1-Motion>", on_drag)

root.mainloop()