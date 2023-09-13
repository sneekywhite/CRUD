import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import psycopg2
from dotenv import load_dotenv

load_dotenv()


URL = os.environ["database_url"]



engine = create_engine(URL)


sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()