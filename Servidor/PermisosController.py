from index import index
from PermisosMoel import PermisoModel

ind = index()
class PermisoController:
    def Get():
        return PermisoModel().select()