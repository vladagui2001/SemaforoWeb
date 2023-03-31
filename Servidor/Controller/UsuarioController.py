from DataBase.index import index
from DataBase.UsuarioModel import UsuarioModel

ind = index()
class UsuarioContrller:
    def Get():
        return UsuarioModel().select()