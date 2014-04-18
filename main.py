import socket
import select

HOST = ''
PORT = 12800
END_SIGNAL = 'boooya'

main_connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
main_connection.bind((HOST, PORT))
main_connection.listen(5)

server_running = True
connected_clients = []
while server_running:
	connections_pending, wlist, xlist = select.select([main_connection], [], [], 0.05)
	for connection in connections_pending:
		connection_with_client, connections_infos = connection.accept()
		connected_client.append(connection_with_client)
	
	clients_waiting = []
	try:
		clients_waiting, wlist, xlist = select.select(connected_clients, [], [], 0.05)
	except select.error:
		pass
	else:
		for client in clients_waiting:
			data = client.recv(1024)
			if data = END_SIGNAL:
				server_running = False

for client in connected_clients:
	client.close()

main_connection.close()
