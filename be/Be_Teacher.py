from sqlalchemy import create_engine, Column, Table, String, INTEGER
from sqlalchemy.orm import declarative_base, sessionmaker
from be.setting import Setting

conn = Setting().getconstrString()
engine = create_engine(str(conn))
Base = declarative_base()
Session = sessionmaker()
Session1 = Session()

class Teacher(Base):
    __tablename__ = "Teacher"
    Teacher_id = Column(INTEGER, primary_key=True)
    Teacher_univer = Column(String)
    Teacher_Name = Column(String)
    Teacher_Famili = Column(String)
    Teacher_Age = Column(String)
    Teacher_Dars = Column(String)
    Teacher_History_jobs = Column(INTEGER)
    Teacher_time = Column(INTEGER)
    def __init__(self, Teacher_univer, Teacher_Name, Teacher_Famili, Teacher_Age, Teacher_Dars, Teacher_History_jobs, Teacher_time ):
        self.Teacher_univer = Teacher_univer
        self.Teacher_Name = Teacher_Name
        self.Teacher_Famili = Teacher_Famili
        self.Teacher_Age = Teacher_Age
        self.Teacher_Dars = Teacher_Dars
        self.Teacher_History_jobs = Teacher_History_jobs
        self.Teacher_time = Teacher_time

Base.metadata.create_all(engine)