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

parser = argparse.ArgumentParser()
parser.parse_args()

parser.add_argument("ip_cliente", help="Ip del cliente")
parser.add_argument("puerto_cliente", help="Puerto del cliente")
parser.add_argument("coordinador", help="Indica con True o False si es o no coordinador")
parser.add_argument("--ip_coordinador", help="Ip del coordinador",action="store_true")
parser.add_argument("--puerto_coordinador", help="Puerto del coordinador",action="store_true")

args = parser.parse_args()
if args.ip_cliente:
    globals()["ip_cliente"] = args.ip_cliente
else:
    exit
if args.ip_cliente:
    globals()["puerto_cliente"] = args.puerto_cliente
else:
    exit
if args.coordinador:
    globals()["puerto_cliente"] = args.coordinador
else:
    globals()["nodo_coordinador"] = 'False'
if args.ip_coordinador and globals()["nodo_coordinador"] == 'False':
    globals()["ip_cliente"] = args.ip_cliente
else:
    exit
if args.puerto_coordinador and globals()["nodo_coordinador"] == 'False':
    globals()["puerto_cliente"] = args.puerto_cliente
else:
    exit

"""
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
"""

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