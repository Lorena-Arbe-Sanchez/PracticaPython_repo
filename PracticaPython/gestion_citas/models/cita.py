class Cita:
    def __init__(self, id, cliente, empleado, fecha, hora, estado):
        self.id = id
        self.cliente = cliente
        self.empleado = empleado
        self.fecha = fecha
        self.hora = hora
        self.estado = "PENDIENTE"

    def confirmar(self):
        self.estado = "CONFIRMADA"

    def cancelar(self):
        self.estado = "CANCELADA"

    def to_dict():
        print(self)

# TODO : ME FALTA POR HACER -->
"""
Reglas: (¿tipo en un método?)
● Una cita empieza siempre en estado PENDIENTE
● Una cita cancelada no puede confirmarse

Poner atributos con los tipos de dato necesarios o los posibles valores:
● cliente (objeto Cliente)
● empleado (objeto Empleado)
● fecha (string)
● hora (string)
● estado (PENDIENTE, CONFIRMADA, CANCELADA)
"""