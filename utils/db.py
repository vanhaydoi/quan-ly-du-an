from sqlalchemy import create_engine

engine = create_engine(
    "mysql+pymysql://root:newpassword@localhost/qldt_abc?charset=utf8mb4",
    echo=True,
)
