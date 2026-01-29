# TODO : Debo codificarlas para q hagan lo debido

class UsuarioInactivoError(Exception):
    def __init__(self, usuario):
        super().__init__(f"Usuario: {usuario}")

class CitaSolapadaError(Exception):
    def __init__(self, cita):
        super().__init__(f"Cita: {cita}")

class EstadoCitaError(Exception):
    def __init__(self, cita):
        super().__init__(f"Cita: {cita}")

# TODO
"""
Cuando se quiera ejecutar:
raise UsuarioInactivoError(b)
"""