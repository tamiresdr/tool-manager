from db.connection import create_database_connection

db_connection = create_database_connection()
cursor = db_connection.cursor()

print('Criando tabela USERS...')
query = """CREATE TABLE users (name text, cpf text, shift text, phone text, team text)"""

cursor.execute(query)

db_connection.commit()

db_connection.close()
