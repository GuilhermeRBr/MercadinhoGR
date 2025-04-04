import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAO.DAO import PessoaDAO, ClienteDAO
from models.Models import Pessoa, Cliente
from validators import validar_nome

class PessoaController:
    @classmethod
    def cadastrar_pessoa(cls, nome, cpf, telefone, email, endereco):
        validar_nome(nome)
        pessoa = Pessoa(nome, cpf, telefone, email, endereco)
        PessoaDAO.salvar_pessoa(pessoa) 

PessoaController.cadastrar_pessoa("João", "12345678901", "12345678901", "joao@example.com", "Rua A, 123")