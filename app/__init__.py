from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from flask_login import current_user
from dotenv import load_dotenv
import os

db = SQLAlchemy()

def create_app():
    # Load environment variables from .env
    load_dotenv()
    
    app = Flask(__name__)
    
    # Load config from environment
    db_url = os.environ.get('DATABASE_URL')
    if not db_url:
        raise RuntimeError(
            "DATABASE_URL not found in .env file. "
            "Please copy .env.example to .env and set your database URL."
        )
    
    # Configure the Flask app
    app.config.from_object('app.config.Config')
    
    # Initialize extensions
    db.init_app(app)
    Session(app)

    # Import models so SQLAlchemy is aware of them
    from . import models

    # Register blueprints and other services
    from .routes import bp
    app.register_blueprint(bp)

    @app.context_processor
    def inject_user():
        return dict(current_user=current_user)

    return app