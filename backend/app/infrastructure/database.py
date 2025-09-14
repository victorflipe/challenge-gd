from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base
import os

USER = os.getenv("POSTGRES_USER")
PASSWORD = os.getenv("POSTGRES_PASSWORD")
HOST=os.getenv("POSTGRES_HOST")
PORT=os.getenv("POSTGRES_PORT")
DATABASE=os.getenv("POSTGRES_DB")
# DATABASE_URL = f'postgresql://{HOST}:{PORT}/{DATABASE}'
DATABASE_URL = f'postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{DATABASE}'
# DATABASE_URL = 'postgresql://tech:tech@techblog_db:5432/techblogdb'
print("========================================")
print("========================================")
print(f'database teste: {DATABASE_URL}')

engine = create_engine(DATABASE_URL, echo=True)
localSession = sessionmaker(bind=engine, autocommit=False, autoflush=False)

Base = declarative_base()

def open_session():
    db:Session = None
    try:
        db = localSession()
        yield db
    finally:
        if db is not None:
            db.close()