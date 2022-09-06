from tool_manager.users.crud import CRUD


class Services:
    def __init__(self):
        self.crud = CRUD()

    def get_users(self):
        users = self.crud.get_users()

        return users

    def create_user(self, name, cpf, shift, phone, team):
        self.crud.create_user(name, cpf, shift, phone, team)

    def update_user(self, name, cpf, shift, phone, team):
        self.crud.update_user(name, cpf, shift, phone, team)

    def delete_user(self, cpf):
        self.crud.delete_user(cpf)
