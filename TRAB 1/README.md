Igor Monteiro Nunes


Comandos para execuções do código sem o makefile:

.Servidor (O parâmetro usado é <ip da máquina>)
python3 servidor.py 172.26.4.150
python3 servidor.py 172.26.4.220
python3 servidor.py 172.26.4.202

.Portal (O parâmetro pode ser <rr> para Round-Robin ou <random> para Aleatório)
python3 portal.py rr
python3 portal.py random

.Cliente (O parâmetro usado é <ip da máquina do portal> <porta>)
python3 cliente.py 172.26.4.133 7777




Comandos para execuções do código com o makefile:

make - compila todo os códigos da pasta

make servidor1 - executa o primeiro servidor com o ip da maquina (python3 servidor.py 172.26.4.150)

make servidor2 - executa o segundo servidor com o ip da maquina (python3 servidor.py 172.26.4.220)

make servidor3 - executa o terceiro servidor com o ip da maquina (python3 servidor.py 172.26.4.202)

make portal_rr - executa o portal com o escalonamento Round-Robin (python3 portal.py rr)

make portal_random - executa o portal com o escalonamento Aleatório (python3 portal.py random)

make cliente - executa o cliente com o ip da maquina do portal e a porta (python3 cliente.py 172.26.4.133 7777)
