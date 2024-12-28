from dal.Repository import Repository
from be.Be_Teacher import Teacher
from tkinter import messagebox

class BllTeacher():
    def Add(self, obj):
        if int(obj.Teacher_History_jobs) <= 5:
            if self.Exist(obj.Teacher_Name, obj.Teacher_Famili, obj.Teacher_Age):
                messagebox.showerror("خطا", "این داده تکراری است")
                return False
            else:
                object = Repository()
                result = object.create(obj)  
                return result  
        else :
            # 2 یعنی سابقه اموزشی کمتر از ده می باشد
            return 2        
    def Read(self ,obj):
        object = Repository()
        result = object.Read(obj)
        return result
    
    def Update(self, obj, id):
        object = Repository()
        result = object.Update(obj, id)
        return result
    
    def Delete(self, obj):
        object = Repository()
        result = object.Delete(obj)
        return result
    
    def Read_By_id(self, obj, id):
        object = Repository()
        result = object.Read_By_id(obj, id)
        return result
    
    def Exist(self, Name, Famili, Age):
        object = Repository()
        result = object.Exist(Name, Famili, Age)
        return result