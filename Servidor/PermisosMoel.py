from conexion import Data

class PermisoModel:
    def __init__(self):
        self.DataBase=Data()

    def select (self):
        self.lista=[]
        for row in self.DataBase.Selecionar("SELECT * FROM PERMISOS"):
            obj = {"ID":row[0],"NOMBRE":row[1]}
            self.lista.append(obj)
        return self.lista
    
    def insert(self,Nombre):
        query='INSERT INTO "main"."PERMISOS"("NOMBRE") VALUES ("'+Nombre+'")'
        print(self.DataBase.Modificar(query))
    
    def Update(self,Nombre,id):
        query='UPDATE "main"."PERMISOS" SET  NOMBRE="'+Nombre+'" WHERE "_rowid_"='+str(id)
        print(self.DataBase.Modificar(query))
    
    def Delet(self,id):
        query='DELETE FROM "main"."PERMISOS" WHERE "_rowid_"='+str(id)
        print(self.DataBase.Modificar(query))