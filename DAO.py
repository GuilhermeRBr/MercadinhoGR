import json
from Models import Cliente



class ClienteDAO:
    @classmethod
    def salvar_cliente(cls, cliente: Cliente):
        with open('data/clientes.json', 'w', encoding='Utf-8' ) as arq:
            json.dump(cliente.nome, arq, indent=4, ensure_ascii=False)
            

    @classmethod
    def listar_clientes(cls):
        clientes = []
        with open('clientes.json', 'r') as arq:
            for linha in arq:
                cliente = Cliente.from_json(linha.strip())
                clientes.append(cliente)
        return clientes
    