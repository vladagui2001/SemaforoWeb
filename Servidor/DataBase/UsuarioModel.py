from DataBase.conexion import Data

class UsuarioModel:
    def __init__(self):
        self.DataBase=Data()

    def select (self):
        self.lista=[]
        for row in self.DataBase.Selecionar("SELECT * FROM Usuario"):
            obj = {"ID":row[0],"PASSWORD":row[1],"NOMBRE":row[2],"FICHA":row[3]}
            self.lista.append(obj)
        return self.lista
    
    def insert(self,Usuario,Password,Ficha):
        query='INSERT INTO "main"."Usuario"("NOMBRE","PASSWORD","FICHA") VALUES ("'+Usuario+'","'+Password+'","'+Ficha+'")'
        print(self.DataBase.Modificar(query))
    
    def Update(self,Usuario,Password,Ficha,id):
        query='UPDATE "main"."Usuario" SET "PASSWORD"="'+Usuario+'", NOMBRE="'+Password+'", FICHA="'+Ficha+'" WHERE "_rowid_"='+str(id)
        print(self.DataBase.Modificar(query))
    
    def Delet(self,id):
        query='DELETE FROM "main"."Usuario" WHERE "_rowid_"='+str(id)
        print(self.DataBase.Modificar(query))
