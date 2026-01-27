from gestion_citas.models.usuario import Usuario


class Cliente(Usuario):
    def __init__(self, telefono):
        super().__init__(telefono)