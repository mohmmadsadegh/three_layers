from sqlalchemy import and_, or_
from sqlalchemy import create_engine, Column, Table, String, INTEGER
from sqlalchemy.orm import declarative_base, sessionmaker
from be.setting import Setting
from be.Be_Teacher import Teacher

conn = Setting().getconstrString()
engine = create_engine(str(conn))
Base = declarative_base()
Session = sessionmaker()
Session1 = Session()

class Repository():
    def create(self, obj):
        try:
            Session1.add(obj)
            Session1.commit()
        except Exception as e:
            print(f"error {e}")
            
    def Read(self ,obj):
        return Session1.query(obj).all()
    
    def Update(self, obj, id):
        new_obj = self.Read_By_id(obj, id)
        new_obj = obj
        Session1.commit()
    
    def Delete(self, obj):
        Session1.delete(obj)
        Session1.commit()
    
    def Read_By_id(self, obj, id):
        return Session1.query(obj).filter(obj.id == id).first()
    
    def Exist(self, Name, Famili, Age):
        result = Session1.query(Teacher).filter(
            and_(
                Teacher.Teacher_Name == Name,
                Teacher.Teacher_Famili == Famili,
                Teacher.Teacher_Age == Age
            )
        ).first()
        return result is not None