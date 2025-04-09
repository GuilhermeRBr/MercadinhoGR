from datetime import datetime
import locale
import re

def formatar_data(data_nascimento):
    if not data_nascimento.isdigit():
        raise ValueError('Data de nascimento deve conter apenas números.')
    elif not re.match(r"^\d{8}$", data_nascimento):
        raise ValueError("Formato inválido. Use DDMMYYYY.")
    elif len(data_nascimento) != 8:
        raise ValueError("Data de nascimento deve ter 8 dígitos.")
    elif data_nascimento < "0101190":
        raise ValueError("Data de nascimento inválida.")
    elif data_nascimento > datetime.now().strftime("%d%m%Y"):
        raise ValueError("Data de nascimento inválida.")

    dia = data_nascimento[:2]
    mes = data_nascimento[2:4]
    ano = data_nascimento[4:]

    data_formatada = f"{dia}/{mes}/{ano}"

    try:
        datetime.strptime(data_formatada, "%d/%m/%Y")
        return data_formatada
    except ValueError:
        return "Data inválida."
    
def formatar_cpf(cpf):   
    if not cpf.isdigit():
        raise ValueError("CPF deve conter apenas números.")
    elif len(cpf) != 11:
        raise ValueError("CPF deve ter 11 dígitos.")
    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"

    return cpf_formatado

def formatar_cnpj(cnpj):
    if not cnpj.isdigit():
        raise ValueError("CNPJ deve conter apenas números.")
    elif len(cnpj) != 14:
        raise ValueError("CNPJ deve ter 14 dígitos.")
    cnpj_formatado = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"

    return cnpj_formatado

def formatar_telefone(telefone):
    if not telefone.isdigit():
        raise ValueError("Telefone deve conter apenas números.")
    elif len(telefone) != 11:
        raise ValueError("Telefone deve ter 11 dígitos.")
    telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"

    return telefone_formatado

def formatar_dinheiro(valor):
    if not isinstance(valor, (int, float)):
        raise TypeError("Valor deve ser um número.")
    elif valor < 0 or valor == 0:
        raise ValueError("Valor não pode ser zero ou negativo.")
    
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    valor_formatado = locale.currency(valor, grouping=True)
    return valor_formatado

