from db.connection import create_database_connection


class CRUD:
    def create_tool(
        self,
        id,
        description,
        manufacturer,
        voltage,
        part_number,
        size,
        unit_measurement,
        type,
        material,
        max_reservation_time,
    ):
        base_query = """
            INSERT INTO tools (ID, DESCRIPTION, MANUFACTURER, VOLTAGE, PART_NUMBER, SIZE, UNIT_MEASUREMENT,
            TYPE, MATERIAL, MAX_RESERVATION_TIME)
            VALUES('{id}', '{description}', '{manufacturer}', '{voltage}', '{part_number}', '{size}',
            '{unit_measurement}', '{type}', '{material}', '{max_reservation_time}')
        """

        db_connection = create_database_connection()
        query = base_query.format(
            id=id,
            description=description,
            manufacturer=manufacturer,
            voltage=voltage,
            part_number=part_number,
            size=size,
            unit_measurement=unit_measurement,
            type=type,
            material=material,
            max_reservation_time=max_reservation_time,
        )
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
        db_connection.close()

    def update_tool(
        self,
        id,
        description,
        manufacturer,
        voltage,
        part_number,
        size,
        unit_measurement,
        type,
        material,
        max_reservation_time,
    ):
        base_query = """
            UPDATE tools
            SET ID='{id}', DESCRIPTION='{description}', MANUFACTURER='{manufacturer}', VOLTAGE='{voltage}',
            PART_NUMBER='{part_number}', SIZE='{size}', UNIT_MEASUREMENT='{unit_measurement}', TYPE='{type}',
            MATERIAL='{material}', MAX_RESERVATION_TIME='{max_reservation_time}'
            WHERE ID='{id}'
        """

        db_connection = create_database_connection()
        query = base_query.format(
            id=id,
            description=description,
            manufacturer=manufacturer,
            voltage=voltage,
            part_number=part_number,
            size=size,
            unit_measurement=unit_measurement,
            type=type,
            material=material,
            max_reservation_time=max_reservation_time,
        )
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
        db_connection.close()

    def delete_tool(self, id):
        base_query = """
            DELETE FROM tools WHERE ID='{id}'
        """

        db_connection = create_database_connection()
        query = base_query.format(id=id)
        cursor = db_connection.cursor()
        cursor.execute(query)
        db_connection.commit()
        db_connection.close()

    def get_tools(self):
        query = """
            SELECT * FROM tools
        """

        db_connection = create_database_connection()
        cursor = db_connection.cursor()
        tools = cursor.execute(query)

        return tools.fetchall()
