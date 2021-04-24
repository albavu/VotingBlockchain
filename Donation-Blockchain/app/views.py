from flask import render_template, request, redirect, jsonify, make_response, send_from_directory, abort, session, url_for, flash, send_file, send_from_directory, safe_join, abort
from app import *
from flask import jsonify

"""
Página de inicio de la aplicación cliente.
Acepta métodos GET Y POST
- En el Método GET, simplemente renderiza la página de inicio
- En el Método POST, recoge los datos y los trata
"""
@app.route("/",methods=["GET","POST"])
def index():
    print(globals()["peers"])
    if request.method == "POST":
        if 'dni' in request.values:
            print(request.values['dni'])
            print(request.values.keys)
        globals()["num_personas"]= globals()["num_personas"] + 1
    return render_template("index.html",num_personas =globals()["num_personas"])


"""
Añade a un nuevo nodo a la red y comunica al resto de nodos que tienen que añadir a ese nodo
a su agenda
Acepta métodos GET
"""
@app.route("/join_network/<ip>/<port>",methods=["GET"])
def register_new_peers(ip,port):

    if ip == None or port == None:
        return "Invalid data", 400
    else:
        node_address = {
            'ip':ip, 
            'port':port
        }
        if node_address not in globals()["peers"]:
            globals()["peers"].append(node_address)
        return jsonify(globals()["peers"]), 200

@app.errorhandler(404)
def not_found(error):
    return render_template("not_found.html"), 404

@app.route("/update_blockchain")
# peers = lo que sea
def minar():
    pass

@app.route("/minar")
# Se mina
# Enviar a todos los nodos de mi peers el nuevo bloque request a update_blockchain
def lopquesea():
    pass
