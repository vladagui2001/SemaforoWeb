from conexion import Data

class SemaforoModel:
    def __init__(self):
        self.DataBase=Data()

    def select (self):
        self.lista=[]
        for row in self.DataBase.Selecionar("SELECT * FROM SEMAFORO"):
            obj = {"ID":row[0],"IP":row[1],"NOMBRE":row[2]}
            self.lista.append(obj)
        return self.lista
    
    def insert(self,NOMBRE,IP):
        query='INSERT INTO "main"."SEMAFORO"("IP","NOMBRE") VALUES ("'+IP+'","'+NOMBRE+'")'
        print(self.DataBase.Modificar(query))
    
    def Update(self,NOMBRE,IP,id):
        query='UPDATE "main"."SEMAFORO" SET "NOMBRE"="'+NOMBRE+'", IP="'+IP+'" WHERE "_rowid_"='+str(id)
        print(self.DataBase.Modificar(query))
    
    def Delet(self,id):
        query='DELETE FROM "main"."SEMAFORO" WHERE "_rowid_"='+str(id)
        print(self.DataBase.Modificar(query))