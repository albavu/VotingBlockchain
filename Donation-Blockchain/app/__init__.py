from flask import Flask
import requests
import sys
import json
import argparse

global ip_cliente 
global puerto_cliente 
global ip_coordinador
global puerto_coordinador 
global nodo_coordinador
global num_personas 
global peers
globals()["peers"] = []
globals()["num_personas"] = -1
globals()["num_personas"] = False
    
if len(sys.argv) < 4:
    print( "Inicialización fallida.")
    exit
else:
    globals()["ip_cliente"] = sys.argv[1]
    globals()["puerto_cliente"] = sys.argv[2]
    globals()["ip_coordinador"] = sys.argv[3]
    globals()["puerto_coordinador"] = sys.argv[4]
    if len(sys.argv) > 4:
        globals()["nodo_coordinador"] = sys.argv[5]
    else:
        globals()["nodo_coordinador"] = 'False'

app = Flask(__name__)

if globals()["nodo_coordinador"] == 'False':
    server = "http://" + globals()["ip_coordinador"] + ":" + globals()["puerto_coordinador"] + "/join_network/" + globals()["ip_cliente"] + "/" + globals()["puerto_cliente"]
    response = requests.get(server, headers={ "Content-Type" : "application/json"})
    globals()["peers"] = list(response.json())
    print(response)
else:
    node_address = {
        'ip': globals()["ip_cliente"], 
        'port':globals()["puerto_cliente"]
    }
    if node_address not in globals()["peers"]:
        globals()["peers"].append(node_address)

from app import views