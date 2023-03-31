from flask import Flask 
from flask import jsonify as json
from Controller.UsuarioController import UsuarioContrller
from DataBase.UsuarioModel import UsuarioModel

DtoUsario = UsuarioModel()

app= Flask(__name__)


#Get Usuarios
@app.route("/Usarios")
def GetUsario():
   # response = UsuarioContrller.Get()
    DtoUsario.select()
    return json([{"N":1},{"N":2}])



if __name__ == '__main__':
    app.run(debug=True,port=7000)