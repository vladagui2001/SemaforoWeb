from UsuarioModel import UsuarioModel
from PermisosMoel import PermisoModel
from Permisos_R_Usuarios import Permisos_R_Usuarios
from SemaforosModel import SemaforoModel

class index:
    def DtoSemaforos():
        return SemaforoModel()

    def DtoUsuario():
        return UsuarioModel()

    def DtoPermiso():
        return PermisoModel()

    def DtoPermisoRUsuario():
        return Permisos_R_Usuarios()
    