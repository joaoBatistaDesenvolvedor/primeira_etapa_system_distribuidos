
import socket,json                          # Import socket module
dados_entrada=dict()
s = socket.socket()                    # Create a socket object
host = socket.gethostname()            # Get local machine name
port = 12345      # Reserve a port for your service.
user=str(input("diga seu user para logar no nosso sistema "))
dados_entrada[user]=str(input(f'Diga a senha desse {user} '))



meudadoemjoson=json.dumps(dados_entrada).encode('utf-8')
s.connect((host, port))
s.sendall(meudadoemjoson)
data = s.recv(1024)
situaçãologin=data.decode()
if situaçãologin =="vc é um usuario valido":
    pedido=str(input("faça seu pedido "))
    s.sendall(pedido.encode())
else:
    print(situaçãologin)

s.close()                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
import socket,json                          # Import socket module
dados_entrada=dict()
s = socket.socket()                    # Create a socket object
host = socket.gethostname()            # Get local machine name
port = 12345      # Reserve a port for your service.
user=str(input("diga seu user para logar no nosso sistema "))
dados_entrada[user]=str(input(f'Diga a senha desse {user} '))



meudadoemjoson=json.dumps(dados_entrada).encode('utf-8')
s.connect((host, port))
s.sendall(meudadoemjoson)
data = s.recv(1024)
situaçãologin=data.decode()
if situaçãologin =="vc é um usuario valido":
    pedido=str(input("faça seu pedido "))
    s.sendall(pedido.encode())
else:
    print(situaçãologin)

s.close()