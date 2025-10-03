from sqlmodel import create_engine
import os

db_file = os.environ.get('VBS_DB', 'vbs.db')
engine = create_engine(f"sqlite:///{db_file}", echo=False, connect_args={"check_same_thread": False})
