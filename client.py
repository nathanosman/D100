# -*-coding:Latin-1 -*

import socket

HOST = "localhost"
PORT = 12800

connection_with_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection_with_server.connect((HOST, PORT))
print("Connexion établie avec le serveur sur le port {}".format(port))

data = b""
while data != b"fin":
    data = input("> ")
    # Peut planter si vous tapez des caractères spéciaux
    data = data.encode()
    # On envoie le message
    connection_with_server.send(data)
    answer = connection_with_server.recv(1024)
    print(answer.decode()) # Là encore, peut planter s'il y a des accents

print("Fermeture de la connexion")
connection_with_server.close()
