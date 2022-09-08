from tool_manager.tools.crud import CRUD


class Services:
    def __init__(self):
        self.crud = CRUD()

    def get_tools(self):
        tools = self.crud.get_tools()

        return tools

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
        self.crud.create_tool(
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
        )

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
        self.crud.update_tool(
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
        )

    def delete_tool(self, id):
        self.crud.delete_tool(id)
