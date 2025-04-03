from ..DAO import PessoaDAO, ClienteDAO
from models.Models import Pessoa, Cliente
from validators import validar_nome

class PessoaController:
    @classmethod
    def cadastrar_pessoa(cls, nome, cpf, telefone, email, endereco):
        validar_nome(nome)
        pessoa = Pessoa(nome, cpf, telefone, email, endereco)
        PessoaDAO.salvar_pessoa(pessoa) 

