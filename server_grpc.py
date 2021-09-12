import ast
from concurrent import futures
import logging
import  json
import grpc
import requests
from urllib3 import request

import  regras_pb2
import regras_pb2_grpc
import paho.mqtt.client as mqtt
client_mqtt=mqtt.Client()
brocker="mqtt.eclipseprojects.io"
client_mqtt.connect("mqtt.eclipseprojects.io",1883)


username='jb'
password="19jb"
listClient=[]
customer_dictionary=dict()
class signIn(regras_pb2_grpc.signInServicer):
    def login(self,request,context):
        return regras_pb2.loginResponse(menssage=("sigIn" if(request.username==username and  request.userpassword==password) else "incorrect username or password"))

    def customerregister(self,request,context):
        global listClient
        global customer_dictionary
        listClient.append([request.usercustomer,request.passwordcustomer])
        customer_dictionary=dict((listClient))
        client_mqtt.publish("resgister_client",str(customer_dictionary))

        return regras_pb2.customerregistrationResponse(customerregisterMessage="resgister user sucess")

def on_message(client, userdata, message):
    global hashtable
    print("Cadastros existentes: ", str(message.payload.decode("utf-8")))
    hashtable = ast.literal_eval(str(message.payload.decode("utf-8")))


client_mqtt.subscribe("resgister_client")
client_mqtt.on_message = on_message
try:
    client_mqtt.loop_forever()

except:
    print("descnected")
    client_mqtt.disconnect()


def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    regras_pb2_grpc.add_signInServicer_to_server(signIn(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()

                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  import ast
from concurrent import futures
import logging
import  json
import grpc
import requests
from urllib3 import request

import  regras_pb2
import regras_pb2_grpc
import paho.mqtt.client as mqtt
client_mqtt=mqtt.Client()
brocker="mqtt.eclipseprojects.io"
client_mqtt.connect("mqtt.eclipseprojects.io",1883)


username='jb'
password="19jb"
listClient=[]
customer_dictionary=dict()
class signIn(regras_pb2_grpc.signInServicer):
    def login(self,request,context):
        return regras_pb2.loginResponse(menssage=("sigIn" if(request.username==username and  request.userpassword==password) else "incorrect username or password"))

    def customerregister(self,request,context):
        global listClient
        global customer_dictionary
        listClient.append([request.usercustomer,request.passwordcustomer])
        customer_dictionary=dict((listClient))
        client_mqtt.publish("resgister_client",str(customer_dictionary))

        return regras_pb2.customerregistrationResponse(customerregisterMessage="resgister user sucess")

def on_message(client, userdata, message):
    global hashtable
    print("Cadastros existentes: ", str(message.payload.decode("utf-8")))
    hashtable = ast.literal_eval(str(message.payload.decode("utf-8")))


client_mqtt.subscribe("resgister_client")
client_mqtt.on_message = on_message
try:
    client_mqtt.loop_forever()

except:
    print("descnected")
    client_mqtt.disconnect()


def serve():

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    regras_pb2_grpc.add_signInServicer_to_server(signIn(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    logging.basicConfig()
    serve()

