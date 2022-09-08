from db.connection import create_database_connection

db_connection = create_database_connection()
cursor = db_connection.cursor()

# USERS
print('Criando tabela USERS...')
query = """
    CREATE TABLE users (name text, cpf text, shift text, phone text, team text)
"""
try:
    cursor.execute(query)
except:
    pass

# TOOLS
print('Criando tabela TOOLS...')
query = """
    CREATE TABLE tools (id text, description text, manufacturer text, voltage text, part_number text, size text,
    unit_measurement text, type text, material text, max_reservation_time text)
"""
try:
    cursor.execute(query)
except:
    pass

db_connection.commit()
db_connection.close()
