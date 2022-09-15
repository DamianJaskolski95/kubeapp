import os

APP_ENV = os.getenv('APP_ENV', 'development')
DATABASE_USERNAME = os.getenv('DATABASE_USERNAME', 'postgres')
DATABASE_PASSWORD = os.getenv('DATABASE_PASSWORD', 'damian12')
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost:5432')
DATABASE_NAME = os.getenv('DATABASE_NAME', 'kubeapp')
TEST_DATABASE_NAME = os.getenv('DATABASE_NAME', 'kubeapp_test')