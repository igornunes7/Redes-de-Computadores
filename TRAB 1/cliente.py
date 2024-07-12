#!/usr/bin/env python3
import socket
import os
import sys
import threading

#python3 cliente.py 172.26.4.133 7777

PORTAL_HOST = sys.argv[1]
PORTAL_PORT = int(sys.argv[2])
PATH = '/home/AD/rgm47538/Área de Trabalho/arquivos'  

#função para listar arquivos no diretório
def listar_arquivos(diretorio):
    try:
        arquivos = os.listdir(diretorio)
        if not arquivos:
            print("Nenhum arquivo encontrado no diretório.")
        else:
            for arquivo in arquivos:
                print(f"[{arquivo}]")
    except FileNotFoundError:
        print("Diretório não encontrado.")
    except Exception as e:
        print(f"Erro ao listar arquivos: {e}")

while True:
    comando = input("")

    if comando == 'L':
        listar_arquivos(PATH)
    elif comando.startswith('S '):
        arquivos_para_enviar = comando[3:-1].strip().split(',')
        for arquivo in arquivos_para_enviar:
            ##concatena diretorio com arquivo
            caminho_arquivo = os.path.join(PATH, arquivo)

            #verifica se o arquivo existe
            if os.path.exists(caminho_arquivo):

                #criando um novo socket para cada envio
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                try:
                    #conectando ao portal
                    client.connect((PORTAL_HOST, PORTAL_PORT))
                    

                    client.send(arquivo.encode())
                    response = client.recv(1024).decode()
                    print(f"{response}")
                finally:
                    client.close()
