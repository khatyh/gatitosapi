from flask import Flask , jsonify , request
#import socket

app = Flask(__name__) 

from metodosSERVIDOR import gatos
 
@app.route('/ping')#Metodo GET es para listar 

def ping():
    return jsonify({"message": "Pong "})

@app.route("/gatos")#Metodo GET

def getGatos():
    return jsonify(gatos)

@app.route("/gatos/<string:gatos_nombre>")#Metodo GET

def getGato(gatos_nombre):
    gatito =[cat for cat in gatos if cat ["nombre"]== gatos_nombre]
    if (len(gatito)> 0):
         return jsonify ({"cat" : gatito[0]})
    return jsonify ({"message" : "Gatito no encontrado"})

@app.route("/gatos", methods = ["POST"])#Metodo POST es para crear

def agregarGatito():
    nuevo_gatito ={

        "nombre": request.json["nombre"],
        "raza": request.json["raza"],
        "edad": request.json["edad"]
    }
    
    gatos.append(nuevo_gatito)
    return jsonify({"message": "Gatito agregado" , "gatos" : gatos })

@app.route("/gatos/<string:gatos_nombre>", methods = ["PUT"])#Metodo PUT es para actualizar 

def editarGatito(gatos_nombre):#Servira para poder editar el valor que queremos de la lista
    gatito =[cat for cat in gatos if cat["nombre"]== gatos_nombre]
    if(len(gatito)> 0):

        gatito[0]["nombre"] = request.json["nombre"]
        gatito[0]["raza"] = request.json["raza"]
        gatito[0]["edad"] = request.json["edad"]
        return jsonify({

            "message": "Gatito actualziado",
            "cat" : gatito[0]

        })
    return jsonify ({"message": "Gatito no encontrado"})

@app.route("/gatos/<string:gatos_nombre>", methods= ["DELETE"])#Sirve para poder eliminar algo en la lista

def eliminarGatito(gatos_nombre):
    gatito=[cat for cat in gatos if cat["nombre"] == gatos_nombre]
    if (len(gatito)> 0):
        gatos.remove(gatito[0])
        return jsonify({

            "message": "Gatito eliminado",
            "gatos": gatos
        })
    return jsonify({"message": "Gatito no encontrado"})
    




if __name__ == "__main__":
    app.run(debug=True,port= 5000)


#@app.route('/')

#def cat():
   # return "hi cat" % request.host

#if __name__ =="__main__":
    # sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
     #sock.bind(('localhost', 0))
     #port = sock.getsockname()[1]
     #sock.close()
     #app.run(port=port)
