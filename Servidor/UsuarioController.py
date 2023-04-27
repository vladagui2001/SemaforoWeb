from index import index
from UsuarioModel import UsuarioModel

ind = index()
class UsuarioContrller:
    def Get():
        return UsuarioModel().select()