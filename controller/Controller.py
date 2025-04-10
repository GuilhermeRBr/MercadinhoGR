import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAO.DAO import PessoaDAO, ClienteDAO
from models.Models import Pessoa, Cliente
from validators import *
from formatters import *

class PessoaController:
    @classmethod
    def cadastrar_pessoa(cls, nome, cpf, telefone, email, endereco):
        try:
            validar_nome(nome)
            formatar_cpf(cpf)
            formatar_telefone(telefone)
            validar_email(email)
            validar_endereco(endereco)
        except ValueError as e:
            print(f"Erro ao cadastrar pessoa: {e}")
            return
        try:
            pessoa = Pessoa(nome, cpf, telefone, email, endereco)
            PessoaDAO.salvar_pessoa(pessoa) 
            print("Pessoa cadastrada com sucesso!")
        except ValueError as e:
            print(f"Erro ao cadastrar pessoa: {e}")

class ClienteController:
    @classmethod
    def cadastrar_cliente(cls, nome, cpf, telefone, email, endereco, data_nascimento):
        try:
            validar_nome(nome)
            formatar_cpf(cpf)
            formatar_telefone(telefone)
            validar_email(email)
            validar_endereco(endereco)
            formatar_data(data_nascimento)
        except ValueError as e:
            print(f"Erro ao cadastrar cliente: {e}")
            return
        try:
            cliente = Cliente(validar_nome(nome), formatar_cpf(cpf), formatar_telefone(telefone), validar_email(email), validar_endereco(endereco), formatar_data(data_nascimento))
            ClienteDAO.salvar_cliente(cliente)
            print("Cliente cadastrado com sucesso!")
        except ValueError as e:
            print(f"Erro ao cadastrar cliente: {e}")