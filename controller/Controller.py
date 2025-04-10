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
            erros = []
            try:
                nome= validar_nome(nome)
            except ValueError as e:
                erros.append(str(e))
            try:
                cpf= formatar_cpf(cpf)
            except ValueError as e:
                erros.append(str(e))
            try:
                telefone= formatar_telefone(telefone)
            except ValueError as e:
                erros.append(str)
            try:
                email= validar_email(email)
            except ValueError as e:
                erros.append(str(e))
            try:
                endereco= validar_endereco(endereco)
            except ValueError as e:
                erros.append(str(e))
            try:
                data_nascimento= formatar_data(data_nascimento)
            except ValueError as e:
                erros.append(str(e))    
            if erros:
                raise ValueError("\n".join(erros))

            cliente = Cliente(nome, cpf, telefone, email, endereco, data_nascimento)
            ClienteDAO.salvar_cliente(cliente)
            print("Cliente cadastrado com sucesso!")

        except ValueError as e:
            print(f"\nErro ao cadastrar cliente:\n{e}")