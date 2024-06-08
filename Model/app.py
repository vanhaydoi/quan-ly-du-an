# Thư viện
from sqlalchemy import create_engine
from typing import List
from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship



mysql_db_url = "mysql://root:123456@localhost:3306/qlda"

engine = create_engine(mysql_db_url)

