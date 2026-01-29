from gestion_citas.models.usuario import Usuario


class Empleado(Usuario):
    def __init__(self, especialidad):
        super().__init__(especialidad)