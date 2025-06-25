import os
from sqlalchemy import create_engine, text
from dotenv import load_dotenv

class DatabaseService:
    def __init__(self, app=None):
        # Load environment variables from .env
        load_dotenv()
        
        # Get DATABASE_URL from .env file
        self.SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
        if not self.SQLALCHEMY_DATABASE_URI:
            raise RuntimeError(
                "DATABASE_URL not found in .env file. "
                "Please copy .env.example to .env and set your database URL."
            )
            
        self.engine = create_engine(self.SQLALCHEMY_DATABASE_URI)

