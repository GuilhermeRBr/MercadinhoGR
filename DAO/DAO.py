import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.Models import Cliente, Pessoa

class ClienteDAO:
    @classmethod
    def salvar_cliente(cls, cliente: Cliente):
        erros = []
        clientes = []
        id_cliente = 1
        try:
            with open('data/clientes.json', 'r', encoding='utf-8') as arq:
                clientes = json.load(arq)
        except FileNotFoundError:
            clientes = []

        for c in clientes:
            if c['id_cliente'] == str(id_cliente):
                id_cliente += 1
            if c['cpf'] == cliente.cpf:
                erros.append(f"Erro: CPF '{cliente.cpf}' já cadastrado.")
            if c['telefone'] == cliente.telefone:
                erros.append(f"Erro: Telefone '{cliente.telefone}' já cadastrado.")
            if c['email'] == cliente.email:
                erros.append(f"Erro: E-mail '{cliente.email}' já cadastrado.")
        if erros:
            raise ValueError('\n'.join(erros))

        clientes.append({
            'nome': cliente.nome,
            'cpf': cliente.cpf,
            'telefone': cliente.telefone,
            'email': cliente.email,
            'endereco': cliente.endereco,
            'data_nascimento': cliente.data_nascimento,
            'id_cliente': str(id_cliente)
        })

        with open('data/clientes.json', 'w', encoding='utf-8') as arq:
            json.dump(clientes, arq, indent=4, ensure_ascii=False)

    @classmethod
    def listar_clientes(cls):
        with open('data/clientes.json', 'r', encoding='utf-8') as arq:
            clientes = json.load(arq)
            lista_clientes = []
            for c in clientes:
                nome,  cpf, telefone, email, endereco, data_nascimento, id_cliente = c.values()
                cliente = Cliente(nome, cpf, telefone, email, endereco, data_nascimento, id_cliente)
                lista_clientes.append(cliente)

            return lista_clientes
        
    @classmethod        
    def excluir_cliente(cls, cpf):
        with open('data/clientes.json', 'r', encoding='utf-8') as arq:
            clientes = json.load(arq)
        for i, cliente in enumerate(clientes):
            if cliente['cpf'] == cpf:
                del clientes[i]
                print(f'\nCliente com cpf {cpf} excluído com sucesso!')
                break
            else:
                print(f'\nCliente com cpf {cpf} não encontrado.')

        with open('data/clientes.json', 'w', encoding='utf-8') as arq:
            json.dump(clientes, arq, indent=4, ensure_ascii=False)

    @classmethod
    def pesquisar_cliente(cls, id):
        with open('data/clientes.json', 'r', encoding='utf-8') as arq:
            clientes = json.load(arq)
        
        for c in clientes:
            if c['id_cliente'] == id:
                nome, cpf, telefone, email, endereco, data_nascimento, id_cliente = c.values()
                return Cliente(nome, cpf, telefone, email, endereco, data_nascimento, id_cliente)
                
        