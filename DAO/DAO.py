import json
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.Models import Cliente, Pessoa


class PessoaDAO:
    @classmethod
    def salvar_pessoa(cls, pessoa: Pessoa):
        pessoas = []
        with open('data/pessoas.json', 'r', encoding='utf-8') as arq:
            pessoas = json.load(arq)
            for p in pessoas:
                if p['cpf'] == pessoa.cpf:
                    raise ValueError("CPF já cadastrado.")
                if p['telefone'] == pessoa.telefone:
                    raise ValueError("Telefone já cadastrado.")
                if p['email'] == pessoa.email:
                    raise ValueError("Email já cadastrado.")
            
            pessoas.append({
                'nome': pessoa.nome,
                'cpf': pessoa.cpf,
                'telefone': pessoa.telefone,
                'email': pessoa.email,
                'endereco': pessoa.endereco
            })

            with open('data/pessoas.json', 'w', encoding='utf-8') as arq:
                json.dump(pessoas, arq, indent=4, ensure_ascii=False)

    @classmethod
    def listar_pessoas(cls):
        with open('data/pessoas.json', 'r', encoding='utf-8') as arq:
            pessoas = json.load(arq)
            for pessoa in pessoas:
                return Pessoa(pessoa['nome'], pessoa['cpf'], pessoa['telefone'], pessoa['email'], pessoa['endereco'])

class ClienteDAO:
    @classmethod
    def salvar_cliente(cls, cliente: Cliente):
        clientes = []
        with open('data/clientes.json', 'r', encoding='utf-8') as arq:
            clientes = json.load(arq)
            for c in clientes:
                if c['cpf'] == cliente.cpf:
                    raise ValueError("CPF já cadastrado.")
                if c['telefone'] == cliente.telefone:
                    raise ValueError("Telefone já cadastrado.")
                if c['email'] == cliente.email:
                    raise ValueError("Email já cadastrado.")
                if c['id_cliente'] == cliente.id_cliente:
                    id_attribuido = int(c['id_cliente'])
                    id_attribuido += 1

        clientes.append({
            'nome': cliente.nome,
            'cpf': cliente.cpf,
            'telefone': cliente.telefone,
            'email': cliente.email,
            'endereco': cliente.endereco,
            'data_nascimento': cliente.data_nascimento,
            'id_cliente': id_attribuido
        })
        with open('data/clientes.json', 'w', encoding='utf-8') as arq:
            json.dump(clientes, arq, indent=4, ensure_ascii=False)

    @classmethod
    def listar_clientes(cls):
        with open('data/clientes.json', 'r', encoding='utf-8') as arq:
            clientes = json.load(arq)
            for cliente in clientes:
                return Cliente(cliente['nome'], cliente['cpf'], cliente['telefone'], cliente['email'], cliente['endereco'], cliente['data_nascimento'], cliente['id_cliente'])

