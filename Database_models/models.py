from database.connection import Base,engine
from sqlalchemy import String, Integer, ForeignKey, DATETIME
from sqlalchemy.orm import Mapped,mapped_column

class Users(Base):
    __tablename__="users"
    uid:Mapped[int]=mapped_column(Integer,primary_key=True,autoincrement=True,index=True)
    email:Mapped[str]=mapped_column(String(50),nullable=False)
    password:Mapped[str]=mapped_column(String(255),nullable=False)
class Projects(Base):
    __tablename__="projects"
    pid:Mapped[int]=mapped_column(Integer,autoincrement=True,primary_key=True)
    uid:Mapped[int]=mapped_column(ForeignKey("users.uid"))
    project_name:Mapped[str]=mapped_column(String(50),nullable=False)
class Tasks(Base):
    __tablename__="tasks"
    tid:Mapped[int]=mapped_column(Integer,autoincrement=True,primary_key=True)
    pid:Mapped[int]=mapped_column(ForeignKey("projects.pid"),nullable=False)
    status:Mapped[str]=mapped_column(String(10),nullable=False)
    time:Mapped[DATETIME]=mapped_column(DATETIME,nullable=False)
Base.metadata.create_all(engine)