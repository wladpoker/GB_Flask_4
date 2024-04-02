from sqlalchemy import create_engine, MetaData

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()

# Определение таблиц в базе данных здесь