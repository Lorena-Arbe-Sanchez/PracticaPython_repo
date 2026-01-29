class Usuario:
    def __init__(self, id, nombre, email):
        if len(nombre) < 3:
            raise ValueError("El nombre debe tener al menos 3 caracteres")

        if "@" not in email:
            raise ValueError("El email debe contener @")

        self.id = id
        self.nombre = nombre
        self.email = email
        self.activo = True

    def activar(self):
        self.activo = True

    def desactivar(self):
        self.activo = False