import os

DATABASE_URL = os.environ.get('DATABASE_URL', 'sqlite:////tmp/main.db')
