class Usuario:
    def __init__(self, id, nombre, email, activo):
        self.id = id
        self.nombre = nombre
        self.email = email
        self.activo = activo

    def activar(self):
        self.activo = True
    def desactivar(self):
        self.activo = False

# TODO : ME FALTA POR HACER -->
"""
Reglas: (¿tipo en un método?)
● El nombre debe tener al menos 3 caracteres
● El email debe contener @

Poner 'activo' como boolean
"""