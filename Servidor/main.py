from flask import Flask ,request
from flask import jsonify 
from index import index
from flask_cors import CORS

from flask_jwt_extended import create_access_token , get_jwt_identity
from flask_jwt_extended import jwt_required ,JWTManager



app= Flask(__name__)
cors = CORS(app, resources={r"*": {"origins": "*"}})
varIndex=index()

app.config["JWT_SECRET_KEY"] = "SemaforoMagico"  # Change this!
jwt = JWTManager(app)




    
#---------Area de Login --------------
@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")
    print(username)
    print(password)
    response =  varIndex.DtoUsuario().select()
    for item in response:
        if item["NOMBRE"] == username or item["PASSWORD"]==password:
            access_token = create_access_token(identity=username)
            return jsonify(access_token=access_token)
            #return "ok"
    return jsonify({"msg":"Introduzca correctamente la información requerida "})

#-----------------------------------------------------------------------------------
#-------------------Area de Semaforo -----------------------------------------------
#Get Semáforos
@app.route("/Semaforos"  )
#@jwt_required()
def GetSemaforo():
    response =  varIndex.DtoSemaforos().select()
    return jsonify(response)

@app.route("/Semaforos/<id>"  )
#@jwt_required()
def GetByIdSemaforo(id):
    response =  varIndex.DtoSemaforos().selectById(Id=id)
    if response != []:
        return jsonify(response)
    else:
        return jsonify({"mensage":"usario no encotrado"})

#POST Semáforos
@app.route("/Semaforos/Add",methods=["POST"])
#@jwt_required()
def PostSemaforo():
    Ip="xxx.xxx.x.xx"
    Nombre=request.json.get("Nombre")
    response =  varIndex.DtoSemaforos().insert(IP=Ip,NOMBRE=Nombre)
    return jsonify(response)
#PUT Semáforos
@app.route("/Semaforos/Edit",methods=["POST"])
#@jwt_required()
def PutSemaforo():
    Id=request.json.get("Id")
    Ip=request.json.get("Ip")
    Nombre=request.json.get("Nombre")
    response =  varIndex.DtoSemaforos().Update(IP=Ip,NOMBRE=Nombre,id=Id)
    return jsonify(response)

@app.route("/Semaforo/Delete/<id>", methods=["POST"])
#@jwt_required()
def DeleteSemaforo(id):
    response =  varIndex.DtoSemaforos().Delet(id=id)
    return jsonify(response)

#-----------------------------------------------------------------------------------
#-------------------Area de Usuario -----------------------------------------------
#Get Usuarios
@app.route("/Usarios")
#@jwt_required()
def GetUsario():
    response= varIndex.DtoPermisos_R_Usuarios().select()
    return jsonify(response)


@app.route("/Usarios/<id>")
#@jwt_required()
def GetByIdUsario(Id):
    #current_user = get_jwt_identity()
    #print(current_user)
    response =  varIndex.DtoUsuario().select()
    return jsonify(response)

@app.route("/Usarios/Add", methods=["POST"])
#@jwt_required()
def AddUsario():
    PASSWORD=request.json.get("Password")
    NOMBRE=request.json.get("Nombre")
    FICHA=request.json.get("FICHA")
    response =  varIndex.DtoUsuario().insert(Usuario=NOMBRE,Ficha=FICHA,Password=PASSWORD)
    return jsonify(response)

@app.route("/Usarios/Edit", methods=["POST"])
#@jwt_required()
def EditUsario():
    Id=request.json.get("Id")
    PASSWORD=request.json.get("Password")
    NOMBRE=request.json.get("Nombre")
    FICHA=request.json.get("FICHA")
    response =  varIndex.DtoUsuario().Update(Usuario=NOMBRE,Ficha=FICHA,Password=PASSWORD,id=Id)
    return jsonify(response)

@app.route("/Usarios/Delete/<id>", methods=["POST"])
#@jwt_required()
def DeleteUsario(id):
    response =  varIndex.DtoUsuario().Delet(id=id)
    return jsonify(response)

#-----------------------------------------------------------------------------------
#-------------------Area de COntrol de Semaforo ------------------------------------
# Control
@app.route('/Control/<id>',methods=["POST"]) 
def ContolVerificar(id):
    Ip=request.json.get("Ip")
    Nombre=request.json.get("Nombre")
    response =  varIndex.DtoSemaforos().selectById(Id=id)
    if response != []:
        if response[0]['NOMBRE'] == Nombre:
            varIndex.DtoSemaforos().Update(IP=Ip,NOMBRE=Nombre,id=id)
            return jsonify({'men':'Ok'})
        else:
            return jsonify({'men':'error'}) 
    else:
        return jsonify({'men':'error'})
    
@app.route('/Control/A/<id>')
def EstadoA (id):
    response =  varIndex.DtoSemaforos().selectById(Id=id)
    if response != []:
        nodo ='http://'+response[0]['IP']+'/' 

        return jsonify({'men':nodo})
    else:
        return jsonify({'men':'error'})

@app.route('/Control/B/<id>')
def EstadoB (id):
    response =  varIndex.DtoSemaforos().selectById(Id=id)
    if response != []:
        nodo ='http://'+response[0]['IP']+'/' 

        return jsonify({'men':nodo})
    else:
        return jsonify({'men':'error'})
    
@app.route('/Control/Con/<id>',methods=["POST"])
def Config (id):
    response =  varIndex.DtoSemaforos().selectById(Id=id)
    if response != []:
        Config={
            "Modo":"",
            "DataSet":"" 
        }
        nodo ='http://'+response[0]['IP']+'/' 

        return jsonify({'men':nodo,"obj":Config})
    else:
        return jsonify({'men':'error'})
#-----------------------------------------------------------------------------------
if __name__ == '__main__':
    app.run(port=7000)