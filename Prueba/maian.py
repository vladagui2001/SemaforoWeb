from flask import Flask ,request, jsonify



app= Flask(__name__)

@app.route("/Manual",methods =["POST"])
def Manual():
    if request.method == 'POST':
        Estado = request.json
        print(Estado['Estado'])
        return ("OK")
    




if __name__ == '__main__':
    app.run(debug=True,port=8081)