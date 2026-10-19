from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker


class Base(DeclarativeBase):
    pass
database_url="mysql+pymysql://root:password@localhost:3306/PTManager"
engine = create_engine(database_url,echo=True)
SessionLocal = sessionmaker(bind=engine)
