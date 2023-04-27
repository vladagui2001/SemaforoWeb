from UsuarioModel import UsuarioModel
from PermisosMoel import PermisoModel
from Permisos_R_Usuarios import Permisos_R_Usuarios
from SemaforosModel import SemaforoModel

class index:
    def DtoSemaforos(self):
        return SemaforoModel()

    def DtoUsuario(self):
        return UsuarioModel()

    def DtoPermiso(self):
        return PermisoModel()

    def DtoPermisoRUsuario(self):
        return Permisos_R_Usuarios()
    