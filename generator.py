import random
import string

def gerar_senha():
    caracteres = string.ascii_letters + string.digits
    senha = ''.join(random.choice(caracteres) for _ in range(6))
    return str(senha)

def gerar_id():
    caracteres = string.digits
    id = ''.join(random.choice(caracteres) for _ in range(6))
    return str(id)
