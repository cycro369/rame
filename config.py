import os

class Config:
    # Secret key for session management and signing
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-key-for-rame-application'
    
    # Database configuration - using SQLite by default
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///rame.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    
    # File upload configuration
    # Ensure this path exists or is created
    UPLOAD_FOLDER = os.path.join(os.getcwd(), 'uploads')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
