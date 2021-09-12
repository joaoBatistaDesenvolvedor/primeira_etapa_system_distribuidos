import ast
import json
import socket  # Import socket module
from shlex import join

import paho.mqtt.client as mqtt
import time
import json

hashtable = dict()

def on_message(client, userdata, message):

    global hashtable
    print("Cadastros existentes: ", str(message.payload.decode("utf-8")))
    hashtable = ast.literal_eval(str(message.payload.decode("utf-8")))




client = mqtt.Client()



client.connect("mqtt.eclipseprojects.io", 1883)
client.subscribe("resgister_client")
client.on_message = on_message
try:
    client.loop_forever()

except:
    print("descnected")
    client.disconnect()
'''
hashtable['cliente1'] = "cliente1"
'''
hashtable['pedido'] = None
s = socket.socket()  # Create a socket objeimport ast
import json
import socket  # Import socket module
from shlex import join

import paho.mqtt.client as mqtt
import time
import json

hashtable = dict()

def on_message(client, userdata, message):

    global hashtable
    print("Cadastros existentes: ", str(message.payload.decode("utf-8")))
    hashtable = ast.literal_eval(str(message.payload.decode("utf-8")))




client = mqtt.Client()



client.connect("mqtt.eclipseprojects.io", 1883)
client.subscribe("resgister_client")
client.on_message = on_message
try:
    client.loop_forever()

except:
    print("descnected")
    client.disconnect()
'''
hashtable['cliente1'] = "cliente1"
'''
hashtable['pedido'] = None
s = socket.socket()  # Create a socket object
host = socket.gethostname()  # Get local machine name
port = 12345  # Reserve a port for your service.
s.bind((host, port))  # Bind to the port

s.listen(5)  # Now wait for client connections.
while True:
    print(f"hash depois do em recebimento {hashtable}")

    c, addr = s.accept()  # Establish connection with client.
    dados_clientes = c.recv(1024)

    print(f"informaçoes passada pelo cliente  {dados_clientes.decode('utf-8')}")
    meuUser = dados_clientes.decode()
    meuUserdict = json.loads(meuUser)
    for chave, valor in meuUserdict.items():
        for key, value in hashtable.items():
            if (key == chave and value == valor):
                c.sendall("vc é um usuario valido".encode())
                meu_pdido = c.recv(1024)
                dados_meu_pedido = meu_pdido.decode()
                hashtable['pedido'] = meu_pdido.decode()
                client.publish("pedido", str(hashtable))
                hashtable.update(hashtable)

                print(hashtable)
            else:
                c.sendall("vc nao tem altorizaçao para logar no sistema".encode())
        print(f"minha chave e {chave} meu valor e {valor}")
    c.close()
