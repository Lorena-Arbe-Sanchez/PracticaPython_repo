from gestion_citas.models.usuario import Usuario


class Cliente(Usuario):
    def __init__(self, id, nombre, email, telefono):
        super().__init__(id, nombre, email)
        self.telefono = telefono