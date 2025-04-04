import re
from datetime import datetime


def validar_nome(nome):
    if not nome.strip():
        raise ValueError("Nome não pode ser vazio.")
    elif not nome.isalpha():
        raise ValueError("Nome deve conter apenas letras.")
    elif len(nome) < 3:
        raise ValueError("Nome deve ter pelo menos 3 caracteres.")
    return nome

def validar_cpf(cpf):
    if not cpf.strip():
        raise ValueError("CPF não pode ser vazio.")
    elif not cpf.isdigit():
        raise ValueError("CPF deve conter apenas números.")
    elif len(cpf) != 11:
        raise ValueError("CPF deve ter 11 dígitos.")
    return cpf

def validar_telefone(telefone):
    if not telefone.strip():
        raise ValueError("Telefone não pode ser vazio.")
    elif not telefone.isdigit():
        raise ValueError("Telefone deve conter apenas números.")
    elif len(telefone) != 11:
        raise ValueError("Telefone deve ter 11 dígitos.")
    return telefone

def validar_email(email):
    if not email.strip():
        raise ValueError("Email não pode ser vazio.")
    elif not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
, email):
        raise ValueError("Email inválido.")
    return email

def validar_endereco(endereco):
    if not endereco.strip():
        raise ValueError("Endereço não pode ser vazio.")
    return endereco

def validar_data_nascimento(data_nascimento):
    if not data_nascimento.isdigit(data_nascimento):
        raise ValueError('Data de nascimento deve conter apenas números.')
    elif not data_nascimento.strip():
        raise ValueError("Data de nascimento não pode ser vazia.")
    elif not re.match(r"^\d{8}$", data_nascimento):
        raise ValueError("Formato inválido. Use DDMMYYYY.")
    elif len(data_nascimento) != 8:
        raise ValueError("Data de nascimento deve ter 8 dígitos.")
    elif data_nascimento < "01011900":
        raise ValueError("Data de nascimento inválida.")
    elif data_nascimento > datetime.now().strftime("%d%m%Y"):
        raise ValueError("Data de nascimento inválida.")
    return data_nascimento


def validar_id(id):
    if not id.strip():
        raise ValueError("ID não pode ser vazio.")
    elif not id.isdigit():
        raise ValueError("ID deve conter apenas números.")
    elif len(id) != 6:
        raise ValueError("ID deve ter 6 dígitos.")
    return id

def validar_salario(salario):
    if not isinstance(salario, (int, float)):
        raise TypeError("Salário deve ser um número.")
    elif not salario.strip():
        raise ValueError("Salário não pode ser vazio.")
    return salario

def validar_cnpj(cnpj):
    if not cnpj.strip():
        raise ValueError('CNPJ não pode ser vazio.')
    elif not cnpj.isdigit():
        raise ValueError('CNPJ deve conter apenas números.')
    elif len(cnpj) != 14:
        raise ValueError('CNPJ deve ter 14 dígitos.')
    return cnpj

def validar_quantidade(quantidade):
    if not isinstance(quantidade, (int, float)):
        raise TypeError("Quantidade deve ser um número.")
    elif not quantidade.strip():
        raise ValueError("Quantidade não pode ser vazia.")
    elif quantidade == 0:
        raise ValueError("Quantidade não pode ser zero.")
    elif quantidade < 0:
        raise ValueError("Quantidade não pode ser negativa.")
    return quantidade

def validar_preco(preco):
    if not isinstance(preco, (int, float)):
        raise TypeError("Preço deve ser um número.")
    elif not preco.strip():
        raise ValueError("Preço não pode ser vazio.")
    elif preco == 0:
        raise ValueError("Preço não pode ser zero.")
    elif preco < 0:
        raise ValueError("Preço não pode ser negativo.")
    return preco

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