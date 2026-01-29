from gestion_citas.models.usuario import Usuario


class Empleado(Usuario):
    def __init__(self, id, nombre, email, especialidad):
        super().__init__(id, nombre, email)
        self.especialidad = especialidad