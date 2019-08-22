import socket
import datetime

serverPort = 1200

# AF_INET == IPv4
# SOCK_STREAM == TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), serverPort))

# Escutando requisicoes TCP
s.listen(5)
print("escutando...")

while True:
   clientsocket, endereco = s.accept()
   print("Conexao com " + str(tuple(endereco)) + " foi estabelecida!")
   
   requisicao = clientsocket.recv(1024)
   
   if (requisicao == "getHorario"):
      clientsocket.send(str(datetime.datetime.now()))


