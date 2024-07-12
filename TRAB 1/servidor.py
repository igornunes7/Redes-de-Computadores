#!/usr/bin/env python3
import socket
import subprocess
import os
import sys
import threading

#python3 servidor.py 172.26.4.150
#python3 servidor.py 172.26.4.220
#python3 servidor.py 172.26.4.202

SERVER_HOST = sys.argv[1]
SERVER_PORT = 8888
PATH = '/home/AD/rgm47538/Área de Trabalho/arquivos' 

#função para compilar e executar os arquivos enviados
def compilar_e_executar(filename):
    try:
        #verifica se o arquivo existe no diretório correto
        caminho_arquivo = os.path.join(PATH, filename)
        if not os.path.exists(caminho_arquivo):
            return "Arquivo não encontrado."

        #executa o arquivo em python3
        result = subprocess.run(['python3', caminho_arquivo], capture_output=True, text=True)

        if result.returncode == 0:
            #retorn saida padrao
            return result.stdout  # Retorna a saída padrão se a execução foi bem-sucedida
        else:
            #retorn saida de erro
            return result.stderr  

    except:
        return "Erro ao executar o script"


#criando o socket do servidor (IPV4 e TCP)
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#ligando o servidor
server.bind((SERVER_HOST, SERVER_PORT))

#fazendo o servidor ouvir
server.listen(10) 



def operator(portal_conn, portal_addr):
    #recebendo nome do arquivo do portal
    filename = portal_conn.recv(1024).decode()

    #compilando e executando o script Python
    resposta = compilar_e_executar(filename)

    #enviando resposta para o portal
    portal_conn.send(resposta.encode())

    #fechando conexões
    portal_conn.close()



#loop infinito para receber conexoes
while True:
    #aceitando a conexao do portal
    portal_conn, portal_addr = server.accept()

    #cria uma thread para essa conexao
    portal_thread = threading.Thread(target=operator, args=(portal_conn, portal_addr))

    #inicia a thread
    portal_thread.start()
