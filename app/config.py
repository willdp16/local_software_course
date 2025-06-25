import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Database
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # Flask
    SECRET_KEY = os.getenv('SECRET_KEY', 'local-dev-key')
    
    # Session configuration
    SESSION_TYPE = 'filesystem'
    
    # Debug mode
    DEBUG = os.getenv('DEBUG', 'True').lower() == 'true'