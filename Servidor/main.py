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
def GetSemaforo():
    response =  varIndex.DtoSemaforos().select()
    return jsonify(response)

#-----------------------------------------------------------------------------------
#Get Usuarios
@app.route("/Usarios"  )
#@jwt_required()
def GetUsario():
    #current_user = get_jwt_identity()
    #print(current_user)
    response =  varIndex.DtoUsuario().select()
    return jsonify(response)

"""@app.route("/Usarios/Add", methods =["POST"] )
def AddUsuarios():
    if request.method == 'POST':
        return ("OK")"""


"""@app.route("/Semaforos/Add", methods =["POST"] )
def AddUSemaforo():
    if request.method == 'POST':
        return ("OK")  """



if __name__ == '__main__':
    app.run(debug=True,port=7000)