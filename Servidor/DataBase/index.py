from DataBase.UsuarioModel import UsuarioModel
from DataBase.PermisosMoel import PermisoModel
from DataBase.Permisos_R_Usuarios import Permisos_R_Usuarios
from DataBase.SemaforosModel import SemaforoModel

class index:
    def DtoSemaforos():
        return SemaforoModel()

    def DtoUsuario():
        return UsuarioModel()

    def DtoPermiso():
        return PermisoModel()

    def DtoPermisoRUsuario():
        return Permisos_R_Usuarios()
    