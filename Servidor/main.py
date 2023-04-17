from flask import Flask ,request
from flask import jsonify 
from index import index

app= Flask(__name__)
varIndex=index()

#Get Usuarios
@app.route("/Usarios"  )
def GetUsario():
    response =  varIndex.DtoUsuario().select()
    return jsonify(response)

@app.route("/Usarios/Add", methods =["POST"] )
def AddUsuarios():
    if request.method == 'POST':
        return ("OK")
        



if __name__ == '__main__':
    app.run(debug=True,port=7000)