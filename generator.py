import random
import string

def gerar_senha():
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(6))
    return str(senha)

def gerar_id():
    ids_bloqueados = ['000000']
    caracteres = string.digits
    while True:
        id = ''.join(random.choice(caracteres) for _ in range(6))
        if id not in ids_bloqueados:
            return str(id)
