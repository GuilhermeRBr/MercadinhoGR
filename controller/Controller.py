import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAO.DAO import PessoaDAO, ClienteDAO
from models.Models import Pessoa, Cliente
from validators import *

class PessoaController:
    @classmethod
    def cadastrar_pessoa(cls, nome, cpf, telefone, email, endereco):
        try:
            validar_nome(nome)
            validar_cpf(cpf)
            validar_telefone(telefone)
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

