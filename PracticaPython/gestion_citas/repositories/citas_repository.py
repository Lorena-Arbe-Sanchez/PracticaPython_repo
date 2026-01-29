class CitasRepository:
    def __init__(self):
        self.citas = []

    def anadir_cita(self, cita):
        self.citas.append(cita)

    def obtener_citas_por_empleado(self, empleado):
        return [citas for citas in self.citas if citas.empleado == empleado]

    def obtener_citas_por_cliente(self, cliente):
        return [citas for citas in self.citas if citas.cliente == cliente]

    def comprobar_cita_empleado(self, empleado, fecha, hora):
        return any(
            cita.empleado == empleado and cita.fecha == fecha and cita.hora == hora
            for cita in self.citas
        )

    def obtener_citas_confirmadas(self):
        return [cita for cita in self.citas if cita.estado == "CONFIRMADA"]

    def agrupar_citas_por_empleado(self):
        resultado = {}
        for cita in self.citas:
            resultado.setdefault(cita.empleado, []).append(cita)
        return resultado