class Cita:
    PENDIENTE = "PENDIENTE"
    CONFIRMADA = "CONFIRMADA"
    CANCELADA = "CANCELADA"

    def __init__(self, id, cliente, empleado, fecha, hora):
        self.id = id
        self.cliente = cliente
        self.empleado = empleado
        self.fecha = fecha
        self.hora = hora
        self.estado = Cita.PENDIENTE

    def confirmar(self):
        if self.estado == Cita.CANCELADA:
            raise Exception("Una cita cancelada no puede confirmarse")
        self.estado = Cita.CONFIRMADA

    def cancelar(self):
        self.estado = Cita.CANCELADA

    def to_dict(self):
        return {
            "id": self.id,
            "cliente": self.cliente.nombre,
            "empleado": self.empleado.nombre,
            "fecha": self.fecha,
            "hora": self.hora,
            "estado": self.estado
        }