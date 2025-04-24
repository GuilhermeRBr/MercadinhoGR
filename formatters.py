from datetime import datetime
import locale
import re


def formatar_data():
    while True:
        data_nascimento = input('DATA DE NASCIMENTO [DDMMYYYY]: ').strip()

        if not re.fullmatch(r"\d{8}", data_nascimento):
            print("Formato inválido. Use apenas números no formato DDMMYYYY.")
            continue

        try:
            data = datetime.strptime(data_nascimento, "%d%m%Y")

            if data > datetime.now():
                print("Data de nascimento não pode ser no futuro.")
            elif data.year < 1900:
                print("Ano inválido. Deve ser a partir de 1900.")
            else:
                return data.strftime("%d/%m/%Y")
        except ValueError:
            print("Data inválida. Verifique o dia, mês e ano.")

    
    
def formatar_cpf(): 
    while True:
        cpf = input('CPF: ') 
        if not cpf.isdigit():
            print("CPF deve conter apenas números.")
        elif len(cpf) != 11:
            print("CPF deve ter 11 dígitos.")
        else:
            cpf_formatado = f"{cpf[:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:]}"
            return cpf_formatado
    

def formatar_cnpj():
    while True:
        cnpj = input('CNPJ: ')
        if not cnpj.isdigit():
            print("CNPJ deve conter apenas números.")
        elif len(cnpj) != 14:
            print("CNPJ deve ter 14 dígitos.")
        else:
            cnpj_formatado = f"{cnpj[:2]}.{cnpj[2:5]}.{cnpj[5:8]}/{cnpj[8:12]}-{cnpj[12:]}"
            return cnpj_formatado

def formatar_telefone():
    while True:
        telefone = input('TELEFONE:')
        if not telefone.isdigit():
            print("Telefone deve conter apenas números.")
        elif len(telefone) != 11:
            print("Telefone deve ter 11 dígitos.")
        else:
            telefone_formatado = f"({telefone[:2]}) {telefone[2:7]}-{telefone[7:]}"
            return telefone_formatado

def formatar_dinheiro():
    while True:
        valor = input('VALOR: ')
        if valor.replace(".", "").replace(",", "").isdigit():
            valor = float(valor.replace(",", "."))
            if valor < 0 or valor == 0:
                print("Valor não pode ser zero ou negativo.")
            
            locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
            valor_formatado = locale.currency(valor, grouping=True)
            return valor_formatado
        else:
            print("Valor deve conter apenas números.")

def dinheiro_para_float(valor_str):
    valor_limpo = valor_str.replace("R$", "").strip().replace(",", ".")
 
    return float(valor_limpo)

def float_para_dinheiro(valor_float):
    locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')
    return locale.currency(valor_float, grouping=True)



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
        