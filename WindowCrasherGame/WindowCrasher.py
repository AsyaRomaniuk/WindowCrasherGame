from tkinter import *
from PIL import ImageGrab, ImageTk
from pygame import mixer

class Timer(object):
    def __init__(self, seconds):
        self.seconds = seconds

def subTimer(timer):
    if timer.seconds != 0:
        timer.seconds -= 1
        lab.config(text=str(timer.seconds))
        opening.after(1000, lambda: subTimer(timer))
    else:
        opening.destroy()

def main():
    mixer.init()
    mixer.music.load("res\gun_shot_sound.mp3")
    root = Tk()
    root.title("Main Window")
    root.attributes('-fullscreen', True)
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    canv = Canvas(root, cursor="none")
    screenshot = ImageTk.PhotoImage(ImageGrab.grab())
    gun = PhotoImage(file=r"res\gun.gif")
    glass = PhotoImage(file=r"res\broken_glass.gif")
    glass2 = PhotoImage(file=r"res\broken_glass1.gif")
    shot = PhotoImage(file=r"res\gun_shot.gif")
    shot2 = PhotoImage(file=r"res\gun_shot1.gif")
    canv.create_image(w / 2, h / 2, image=screenshot)
    canvas_gun = canv.create_image(w / 2 + gun.width() / 2, h / 2 + gun.height() / 2, image=gun)
    canv.pack(fill=BOTH, expand=1)
    canv.focus()
    popup = Menu(root, tearoff=0)
    popup.add_command(label="Exit", command=root.destroy)
    popup.add_command(label="Broken glass 1", command=lambda: root.bind("<Button-1>",
                    lambda e: (canv.create_image(e.x, e.y, image=glass),
                        mixer.music.play(),
                        canv.tag_raise(canvas_gun))))
    popup.add_command(label="Broken glass 2", command=lambda: root.bind("<Button-1>",
                     lambda e: (canv.create_image(e.x, e.y, image=glass2),
                        mixer.music.play(),
                        canv.tag_raise(canvas_gun))))
    popup.add_command(label="Hole 1", command=lambda: root.bind("<Button-1>",
                     lambda e: (canv.create_image(e.x, e.y, image=shot),
                        mixer.music.play(),
                        canv.tag_raise(canvas_gun))))
    popup.add_command(label="Hole 2", command=lambda: root.bind("<Button-1>",
                     lambda e: (canv.create_image(e.x, e.y, image=shot2),
                        mixer.music.play(),
                        canv.tag_raise(canvas_gun))))
    root.bind("<Button-1>", lambda e: (canv.create_image(e.x, e.y, image=glass),
                        mixer.music.play(),
                        canv.tag_raise(canvas_gun)))
    root.bind("<Motion>", lambda e: canv.coords(canvas_gun, e.x + gun.width() / 2, e.y + gun.height() / 2))
    root.bind("<Button-3>", lambda e: popup.post(e.x, e.y))
    root.mainloop()


if __name__ == "__main__":
    time = Timer(5)
    opening = Tk()
    opening.geometry(f"+{int(opening.winfo_screenwidth()/2)}+{int(opening.winfo_screenheight()/2)}")
    opening.overrideredirect(True)
    opening.attributes("-transparentcolor", "SystemButtonFace")
    opening.attributes("-topmost", True)
    lab = Label(opening, text=f"{time.seconds}", fg="red", font=("", 26, "bold"))
    lab.pack()
    lab.bind("<Button-1>", lambda e: opening.destroy())
    opening.after(1000, lambda: subTimer(time))
    opening.mainloop()
    if time.seconds == 0:
        main()
