import sys

try:
    arq = open(sys.argv[1], "r")
except FileNotFoundError:
    print("Erro: arquivo não encontrado!")
    sys.exit(1)

arq.close()
