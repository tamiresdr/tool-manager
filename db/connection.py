import sqlite3


def create_database_connection():
    return sqlite3.connect('tool-manager.db')
