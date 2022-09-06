from db.connection import create_database_connection


class CRUD:
    def create_user(self, name, cpf, shift, phone, team):
        base_query = """
            INSERT INTO users (NAME, CPF, SHIFT, PHONE, TEAM)
            VALUES('{name}', '{cpf}','{shift}', '{phone}','{team}')
        """

        db_connection = create_database_connection()
        query = base_query.format(name=name, cpf=cpf, shift=shift, phone=phone, team=team)
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
        db_connection.close()

    def update_user(self, name, cpf, shift, phone, team):
        base_query = """
            UPDATE users
            SET NAME='{name}', CPF='{cpf}', SHIFT='{shift}', PHONE='{phone}', TEAM='{team}'
            WHERE cpf='{cpf}'
        """

        db_connection = create_database_connection()
        query = base_query.format(name=name, cpf=cpf, shift=shift, phone=phone, team=team)
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
        db_connection.close()

    def delete_user(self, cpf):
        base_query = """
            DELETE FROM users WHERE CPF='{cpf}'
        """

        db_connection = create_database_connection()
        query = base_query.format(cpf=cpf)
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
        db_connection.close()

    def get_users(self):
        query = """
            SELECT * FROM users
        """

        db_connection = create_database_connection()
        cursor = db_connection.cursor()
        users = cursor.execute(query)

        return users.fetchall()
