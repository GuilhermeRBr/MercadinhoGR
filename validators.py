import re
from datetime import datetime


def validar_nome(nome):
    if not nome.strip():
        raise ValueError("Nome não pode ser vazio.")
    elif not nome.isalpha():
        raise ValueError("Nome deve conter apenas letras.")
    elif len(nome) < 3:
        raise ValueError("Nome deve ter pelo menos 3 caracteres.")
    return nome.title()


def validar_email(email):
    if not email.strip():
        raise ValueError("Email não pode ser vazio.")
    elif not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
, email):
        raise ValueError("Email inválido.")
    return email.lower()

def validar_endereco(endereco):
    if not endereco.strip():
        raise ValueError("Endereço não pode ser vazio.")
    return endereco.title()

def validar_id(id):
    if not id.isdigit():
        raise ValueError("ID deve conter apenas números.")
    elif len(id) != 6:
        raise ValueError("ID deve ter 6 dígitos.")
    return id


def validar_quantidade(quantidade):
    if not isinstance(quantidade, (int, float)):
        raise TypeError("Quantidade deve ser um número.")
    elif quantidade == 0 or quantidade < 0:
        raise ValueError("Quantidade não pode ser zero ou negativo.")
    return quantidade

def validar_nome_produto(nome_produto):
    if not nome_produto.strip():
        raise ValueError("Nome do produto não pode ser vazio.")
    elif not nome_produto.isalpha():
        raise ValueError("Nome do produto deve conter apenas letras.")
    elif len(nome_produto) < 3:
        raise ValueError("Nome do produto deve ter pelo menos 3 caracteres.")
    return nome_produto

def validar_nome_categoria(nome_categoria):
    if not nome_categoria.strip():
        raise ValueError("Nome da categoria não pode ser vazio.")
    elif not nome_categoria.isalpha():
        raise ValueError("Nome da categoria deve conter apenas letras.")
    elif len(nome_categoria) < 3:
        raise ValueError("Nome da categoria deve ter pelo menos 3 caracteres.")
    return nome_categoria

def validar_opcao(opcao):
    while True:
        if opcao.isdigit():
           return int(opcao)
        else:
            print("Opção inválida. Digite um número.")
            opcao = input("Digite a opção desejada: ")

