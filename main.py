from tkinter import Tk, messagebox
from pl.form.Teacher_Register import App


if __name__ == "__main__":
    screen = Tk()
    screen.title("university")
    screen.geometry("%dx%d+%d+%d" % (800, 800, 200, 200))
    PageMe = App(screen)
    screen.mainloop()