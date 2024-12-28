from tkinter import Tk, Frame, Label, Entry, Button, messagebox, ttk
from bll.bllTeacher import BllTeacher
from be.Be_Teacher import Teacher


class App(Frame):
    def __init__(self, screen):
        super().__init__(screen)
        self.master = screen
        self.create_widget()   
    
    def create_widget(self):
        self.screen = Tk()
        self.screen.title("خوش امدید")
        self.screen.resizable(True, True)
        self.screen.geometry("%dx%d+%d+%d" % (400, 400, 500, 200))
        self.lblUniver = Label(self.master, text="دانشگاه")
        self.lblUniver.place(x=480, y=0)
        self.TxtUniver = Entry(self.master)
        self.TxtUniver.place(x=330, y=0)
        self.TxtUniver.bind("<FocusOut>", self.Type_Univer)
        self.lblName = Label(self.master, text="نام")
        self.lblName.place(x=480, y=40)
        self.TxtName = Entry(self.master)
        self.TxtName.place(x=330, y=40)
        self.TxtName.bind("<FocusOut>", self.Type_Name)
        self.lblFamili = Label(self.master, text="نام خانوادگی ")
        self.lblFamili.place(x=480, y=80)
        self.TxtFamili = Entry(self.master)
        self.TxtFamili.place(x=330, y=80)
        self.TxtFamili.bind("<FocusOut>", self.Type_Famili)
        self.lblAge = Label(self.master, text="سن")
        self.lblAge.place(x=480, y=120)
        self.TxtAge = Entry(self.master)
        self.TxtAge.place(x=330, y=120)
        self.TxtAge.bind("<FocusOut>", self.Type_Age)
        self.lbl_History_teach = Label(self.master, text="سابقه تدریس")
        self.lbl_History_teach.place(x=480, y=160)
        self.Txt_History_teach = Entry(self.master)
        self.Txt_History_teach.place(x=330, y=160)
        self.Txt_History_teach.bind("<FocusOut>", self.Txt_History_teach)
        self.lblDars = Label(self.master, text="درس")
        self.lblDars.place(x=480, y=200)
        self.TxtDars = ttk.Combobox(self.master, state="readonly")
        self.Dars_title = ["c++", "javascrip", "c#", "html", "mongo", "python", "php"]
        self.TxtDars["values"] = self.Dars_title
        self.TxtDars.set("python")
        # self.TxtDars.bind("<FocusOut>", self.Dars)
        self.TxtDars.place(x=330, y=200)
        self.lblSaat = Label(self.master, text="ساعت شروع تا پایان",)
        self.lblSaat.place(x=480, y=240)
        self.TxtSaat = ttk.Combobox(self.master, state="readonly")
        self.combo_saat = ["8 ta 10", "10 ta 12", "12 ta 14", "14 ta 16", "18 ta 20"]
        self.TxtSaat["values"] = self.combo_saat
        # self.TxtSaat.bind("<FocusOut>", self.saat)
        self.TxtSaat.place(x=330, y=240)
        self.BtnRegister = Button(self.master, text="ثبت",
                                  command=self.OnclickSave)
        self.BtnRegister.place(x=330, y=280)
        self.screen.mainloop()
    
    def Type_Age(self, e):
        if not self.TxtAge.get().isnumeric():
            return False 
        else:
            return True 
    
    def Type_History(self, e):
        if not self.Txt_History_teach.get().isnumeric():
            return False 
        else:
            return True 
    
    def Type_Name(self, e):
        if self.TxtName.get().isalpha():
            return False 
        else:
            return True 
    
    def Type_Famili(self, e):
        if self.TxtFamili.get().isnumeric():
            return False 
        else:
            return True 
    
    def Type_Univer(self, e):
        if self.TxtUniver.get().isnumeric():
            return False 
        else:
            return True 
    
    def OnclickSave(self):
        if self.TxtUniver.get() == "":
            messagebox.showerror("خطا", "لطفا فیلد دانشگاه را پر کنید")
            return False
        elif self.TxtUniver.get().isnumeric():
            messagebox.showerror("خطا", "لطفا فیلد دانشگاه را با حروف وارد کنید")
            return False 
        elif self.TxtName.get() == "":
            messagebox.showerror("خطا", "لطفا فیلد نام را پر کنید")
            return False
        elif not self.TxtName.get().isalpha():
            messagebox.showerror("خطا", "لطفا فیلد نام را با حروف وارد کنید")
            return False 
        elif self.TxtFamili.get() == "":
            messagebox.showerror("خطا", "لطفا فیلد نام خانوادگی را پر کنید")
            return False
        elif self.TxtFamili.get().isnumeric():
            messagebox.showerror("خطا", "لطفا فیلد نام خانوادگی را با حروف وارد کنید")
            return False 
        elif self.TxtAge.get() == "":
            messagebox.showerror("خطا", "لطفا فیلد سن را پر کنید")
            return False
        elif not self.TxtAge.get().isnumeric():
            messagebox.showerror("خطا", "لطفا فیلد سن را با عدد وارد کنید")
            return False 
        elif not self.Txt_History_teach.get().isnumeric():
            messagebox.showerror("خطا",
                                 "لطفا فیلد سابقه تدریس را با عدد وارد کنید")
            return False 
        else:
            repo = Teacher(self.TxtUniver.get(), self.TxtName.get(), self.TxtFamili.get(), self.TxtAge.get(), self.TxtDars.get(), self.Txt_History_teach.get(), self.TxtSaat.get())
            RES = BllTeacher()
            RES.Add(repo)
            messagebox.showinfo("منتظر تماس باشید",
                                "سوابق اموزشی شما در حال بررسی است ")
            return True