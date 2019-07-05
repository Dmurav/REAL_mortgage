import os

#директория в которой лежит скрипт
basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = ""
USERNAME = 'admin'
PASSWORD = 'admin'
WTF_CSRF_ENABLED = True
SECRET_KEY = 'myprecious'
DATABASE_PATH = os.path.join(basedir, DATABASE)