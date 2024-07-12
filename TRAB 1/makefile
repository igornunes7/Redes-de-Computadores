PY_FILES = servidor.py portal.py cliente.py

all: chmod_files

chmod_files:
	@echo "Compiling...."
	chmod +x $(PY_FILES)

servidor1:
	python3 servidor.py 172.26.4.150

servidor2:
	python3 servidor.py 172.26.4.220

servidor3:
	python3 servidor.py 172.26.4.202

portal_rr:
	python3 portal.py rr

portal_random:
	python3 portal.py random

cliente:
	python3 cliente.py 172.26.4.133 7777

.PHONY: all chmod_files servidor1 servidor2 servidor3  portal_rr portal_random  cliente
