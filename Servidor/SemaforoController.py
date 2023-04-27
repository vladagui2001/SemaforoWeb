from index import index
from SemaforosModel import SemaforoModel

ind = index()
class SemaforoContrller:
    def Get():
        return SemaforoModel().select()