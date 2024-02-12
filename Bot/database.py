from sqlalchemy import create_engine


SQL_DATABASE_URL = r'postgresql://postgres:password@localhost/EmailTexts'

engine = create_engine(SQL_DATABASE_URL) # движок для базы данных