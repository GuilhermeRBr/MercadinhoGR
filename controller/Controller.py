import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAO.DAO import ClienteDAO
from models.Models import Pessoa, Cliente
from validators import *
from formatters import *

class ClienteController:
    @classmethod
    def cadastrar_cliente(cls):
        nome = "jqwo"
        cpf = "12345212901"
        telefone = "15387654221"
        email = "joss2o@gmail.com"
        endereco = "Rua A, 123"
        data_nascimento = "01122000"

        try:
            cliente = Cliente(nome, cpf, telefone, email, endereco, data_nascimento)
            ClienteDAO.salvar_cliente(cliente)
            print("Cliente cadastrado com sucesso!")
        except ValueError as e:
            print(f"\nErro ao cadastrar cliente:\n{e}")
    
    @classmethod
    def listar_clientes(cls):
        clientes = ClienteDAO.listar_clientes()

        for cliente in clientes:
             print(f'\nID: {formatar_id(cliente.id_cliente)} | Nome: {cliente.nome} | CPF: {cliente.cpf} | Telefone: {cliente.telefone} | Email: {cliente.email}, Endereço: {cliente.endereco} | Data de Nascimento: {cliente.data_nascimento}\n')

    @classmethod
    def pesquisar_cliente(cls, cpf):
        pesq_cliente = ClienteDAO.pesquisar_cliente(cpf)

        print(f'\nID: {formatar_id(pesq_cliente.id_cliente)} | NOME: {pesq_cliente.nome} | CPF: {pesq_cliente.cpf} | TELEFONE: {pesq_cliente.telefone} | EMAIL: {pesq_cliente.email} | ENDEREÇO: {pesq_cliente.endereco} | DATA DE NASCIMENTO: {pesq_cliente.data_nascimento}')

    @classmethod
    def atualizar_cliente(cls, opcao):
        pass