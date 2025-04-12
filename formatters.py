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
    elif data_nascimento > datetime.now().strftime("%d%m%Y"):
        raise ValueError("Data de nascimento inválida.")
    elif int(data_nascimento[:2]) > 31:
        raise ValueError("Dia inválido.")
    elif int(data_nascimento[2:4]) > 12:
        raise ValueError("Mês inválido.")
    elif int(data_nascimento[4:]) < 1900:
        raise ValueError("Ano inválido.")
    

    dia = data_nascimento[:2]
    mes = data_nascimento[2:4]
    ano = data_nascimento[4:]

    data_formatada = f"{dia}/{mes}/{ano}"
    return data_formatada
 
    
def formatar_cpf():  
    while True:
        cpf = input('Digite o CPF: ') 
        if not cpf.isdigit():
            print("CPF deve conter apenas números.")
        elif len(cpf) != 11:
            print("CPF deve ter 11 dígitos.")
        else:
            break

    cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
    return cpf_formatado

def formatar_cnpj():
    while True:
        cnpj = input('Digite o CNPJ: ')
        if not cnpj.isdigit():
            print("CNPJ deve conter apenas números.")
        elif len(cnpj) != 14:
            print("CNPJ deve ter 14 dígitos.")
        else:
            break
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

def formatar_id(id):
    match len(id):
        case 1:
            return f"00000{id}"
        case 2:
            return f"0000{id}"
        case 3:
            return f"000{id}"
        case 4:
            return f"00{id}"
        case 5:
            return f"0{id}"
        case 6:
            return id