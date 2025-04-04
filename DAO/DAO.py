import json

from models.Models import Cliente, Pessoa


class PessoaDAO:
    @classmethod
    def salvar_pessoa(cls, pessoa: Pessoa):
        pessoas = []
        with open('data/pessoas.json', 'r', encoding='utf-8') as arq:
            pessoas = json.load(arq)
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

        clientes.append({
            'nome': cliente.nome,
            'cpf': cliente.cpf,
            'telefone': cliente.telefone,
            'email': cliente.email,
            'endereco': cliente.endereco,
            'data_nascimento': cliente.data_nascimento,
            'id_cliente': cliente.id_cliente
        })
        with open('data/clientes.json', 'w', encoding='utf-8') as arq:
            json.dump(clientes, arq, indent=4, ensure_ascii=False)

    @classmethod
    def listar_clientes(cls):
        with open('data/clientes.json', 'r', encoding='utf-8') as arq:
            clientes = json.load(arq)
            for cliente in clientes:
                return Cliente(cliente['nome'], cliente['cpf'], cliente['telefone'], cliente['email'], cliente['endereco'], cliente['data_nascimento'], cliente['id_cliente'])
    