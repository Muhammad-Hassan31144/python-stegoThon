import os

class Config:
    SECRET_KEY = os.urandom(24)
    UPLOAD_FOLDER = 'uploads'
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16 MB
    # ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'bmp'}
