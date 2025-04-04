from datetime import datetime
import re

def formatar_data(data_str):
    dia = data_str[:2]
    mes = data_str[2:4]
    ano = data_str[4:]

    data_formatada = f"{dia}/{mes}/{ano}"

    try:
        datetime.strptime(data_formatada, "%d/%m/%Y")
        return data_formatada
    except ValueError:
        return "Data inválida."
    
def formatar_cpf(cpf):    
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf_formatado

def formatar_telefone(telefone):
    telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
    return telefone_formatado

def formatar_email(email):
    email_formatado = email.lower()
    return email_formatado

def formatar_endereco(endereco):
    endereco_formatado = endereco.title()
    return endereco_formatado

def formatar_nome(nome):
    nome_formatado = nome.title()
    return nome_formatado

def formatar_dinheiro(valor):
    valor_formatado = f"R$ {valor:,.2f}".replace('.', ',')
    return valor_formatado


    