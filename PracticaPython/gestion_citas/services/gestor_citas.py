from gestion_citas.exceptions.errores import UsuarioInactivoError, CitaSolapadaError, EstadoCitaError
from gestion_citas.models.cita import Cita


class GestorCitas():
    def __init__(self, repositorio):
        self.repositorio = repositorio

    def crear_cita(self, id, cliente, empleado, fecha, hora):
        if not cliente.activo or not empleado.activo:
            raise UsuarioInactivoError("Un usuario inactivo no puede crear citas")

        if self.repositorio.comprobar_cita_empleado(empleado, fecha, hora):
            raise CitaSolapadaError("Un empleado no puede tener dos citas a la misma hora")

        cita = Cita(id, cliente, empleado, fecha, hora)
        self.repositorio.anadir_cita(cita)
        return cita

    def confirmar_cita(self, cita):
        if cita.estado == Cita.CANCELADA:
            raise EstadoCitaError("Una cita cancelada no puede confirmarse")
        cita.confirmar()

    def cancelar_cita(self, cita):
        cita.cancelar()

    def obtener_citas_por_estado(self):
        resumen = {}
        for cita in self.repositorio.citas:
            resumen[cita.estado] = resumen.get(cita.estado, 0) + 1
        return resumen