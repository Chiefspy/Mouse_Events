from tkinter import *
from tkinter import messagebox


def doSomething(event):
    messagebox.showinfo(title="show info", message=f"Mouse coordinates: {event.x}, {event.y}")


window = Tk()

# window.bind("<Button-1>", doSomething)
# window.bind("<Button-2>", doSomething) only works on a mouse
# window.bind("<Button-3>", doSomething)
# window.bind("<Enter>", doSomething)
window.bind("<ButtonRelease>", doSomething)
# window.bind("<Motion>", doSomething)
# window.bind("<Leave>", doSomething)

window.mainloop()
