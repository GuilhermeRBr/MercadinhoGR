import re
from datetime import datetime
from utils.formatters import formatar_id


def validar_nome():
    while True:
        nome = input('NOME: ')
        if not nome.strip():
            print("Nome não pode ser vazio.")
        elif not nome.replace(" ", "").isalpha():
            print("Nome deve conter apenas letras.")
        elif len(nome) < 3:
            print("Nome deve ter pelo menos 3 caracteres.")
        else:
            return nome.title()

def validar_email():
    while True:
        email = input('EMAIL: ')
        if not email.strip():
            print("Email não pode ser vazio.")
        elif not re.match(r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    , email):
            print("Email inválido.")
        else:
            return email.lower()

def validar_endereco():
    while True:
        endereco = input('ENDEREÇO: ')
        if not endereco.strip():
            print("Endereço não pode ser vazio.")
        else:
            return endereco.title()

def validar_id():
    while True:
        id = input('ID: ')
        if id.lower() == 'v':
              return 'v'
        if id == '0':
            return formatar_id(str(id))
        if not id.isdigit():
            print("ID deve conter apenas números.")
        elif len(id) > 6:
            print("ID deve ter no maximo 6 dígitos.")
        else:
            return formatar_id(str(id))


def validar_quantidade():
    while True:
        quantidade = input('QUANTIDADE: ')
        if not quantidade.isdigit():
            print("Quantidade deve conter apenas números.")
        elif int(quantidade) < 0 or int(quantidade) == 0:
            print("Quantidade não pode ser zero ou negativo.")
        else:
            return int(quantidade)


def validar_nome_produto():
    while True:
        nome_produto = input('NOME DO PRODUTO: ')
        if not nome_produto.strip():
            print("Nome do produto não pode ser vazio.")
        elif len(nome_produto) < 3:
            print("Nome do produto deve ter pelo menos 3 caracteres.")
        else:
            return nome_produto.title()

def validar_descricao():
    while True:
        descricao = input('DESCRIÇÃO: ')
        if not descricao.strip():
            print("Descrição não pode ser vazia.")
        elif len(descricao) < 3:
            print("Descrição deve ter pelo menos 3 caracteres.")
        else:
            return descricao.title() 

def validar_categoria():
    while True:
        categoria = input('CATEGORIA: ')
        if not categoria.strip():
            print("Categoria não pode ser vazia.")
        elif len(categoria) < 3:
            print("Categoria deve ter pelo menos 3 caracteres.")
        else:
            return categoria.title()

def validar_opcao():
    while True:
        opcao = input('\nDigite a opção desejada: ')
        if not opcao.isdigit():
            print("Opção inválida. Digite um número.")
        else:
            return int(opcao)

def validar_cargo():
    while True:
        cargo = input('CARGO: ')
        if not cargo.strip():
            print("Cargo não pode ser vazio.")
        elif not cargo.isalpha():
            print("Cargo deve conter apenas letras.")
        elif len(cargo) < 3:
            print("Cargo deve ter pelo menos 3 caracteres.")
        else:
            return cargo.title()

def validar_senha():
    while True:
        senha = input('SENHA: ')
        if not senha.strip():
            print("Senha não pode ser vazia.")
        elif len(senha) < 6:
            print("Senha deve ter pelo menos 6 caracteres.")
        else:
            return str(senha)

def validar_parcelas():
    while True:
        parcelas = input('PARCELAS: ')
        if not parcelas.isdigit():
            print("Parcelas deve conter apenas números.")
        elif int(parcelas) < 1 or int(parcelas) > 12:
            print("Parcelas deve ser entre 1 e 12.")
        else:
            return int(parcelas)
         
def input_mes_ano():
    while True:
        data_mes = input('DATA MÊS [MM]: ').strip()
        data_ano = input('DATA ANO [YYYY]: ').strip()
        
        try:
            data = datetime.strptime(data_mes + data_ano, "%m%Y")
            if data > datetime.now():
                print("Data não pode ser no futuro.")
            elif data.year < 1900:
                print("Ano inválido. Deve ser a partir de 1900.")
            else:
                return int(data_mes), int(data_ano)
        except ValueError:
            print("Data inválida. Verifique o mês e ano.")
