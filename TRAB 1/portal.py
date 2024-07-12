#!/usr/bin/env python3
import socket
import sys
import random
import threading

#python3 portal.py rr

PORTAL_HOST = '172.26.4.133'
PORTAL_PORT = 7777


SERVERS = [
    ('172.26.4.150', 8888),
    ('172.26.4.220', 8888),
    ('172.26.4.202', 8888)
]

MODE = sys.argv[1]


#contador para round robin
rr_counter = 0

#escalonador de servidores pro rr
def get_server_rr():
    global rr_counter
    if (rr_counter == 3):
        rr_counter = 0

    server = SERVERS[rr_counter]
    rr_counter += 1
    return server


#escalonador de servidores por random
def get_server_random():
    servers = SERVERS.copy()
    random.shuffle(servers)
    return servers


##randomiza os servidores
if (MODE == 'random'): 
    random_servers = get_server_random();
else:
    random_servers = [];


def handle_client(client_conn, client_addr):
    global random_servers

    #recebendo nome do arquivo do cliente
    filename = client_conn.recv(1024).decode()

    if MODE == 'rr':
        server_host, server_port = get_server_rr()
    elif MODE == 'random':
        #se a lista ficou vazia
        if not random_servers:
            random_servers = get_server_random()
        server_host, server_port = random_servers.pop()


    #conectando ao servidor
    server_conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_conn.connect((server_host, server_port))

    #enviando nome do arquivo para o servidor
    server_conn.send(filename.encode())

    #recebendo resposta do servidor
    server_response = server_conn.recv(1024).decode()

    #enviando resposta do servidor de volta para o cliente
    client_conn.send(server_response.encode())

    #fechando conexões
    server_conn.close()
    client_conn.close()


#criando o socket do portal
portal = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#ligando o portal
portal.bind((PORTAL_HOST, PORTAL_PORT))

#permitindo 10 conexoes
portal.listen(10) 

#print("Portal conectado")

while True:
    #aceitando a conexao do cliente
    client_conn, client_addr = portal.accept()

    #cria uma thread para essa conexao
    client_thread = threading.Thread(target=handle_client, args=(client_conn, client_addr))

    #inicia a thread
    client_thread.start()
