import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1200))

requisicao = "getHorario"

s.send(bytes(requisicao))
print("enviada requisicao: getHorario")

resposta = s.recv(1024)
print("resposta recebida: ", resposta)
