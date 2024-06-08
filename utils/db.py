from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from Model.Base import Base

engine = create_engine(
    "mysql+pymysql://root:newpassword@localhost/qldt_abc?charset=utf8mb4",
    echo=True,
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(engine)
