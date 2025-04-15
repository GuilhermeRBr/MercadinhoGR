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
        nome = "jeorge"
        cpf = "453.452.564-01"
        telefone = "(65) 34455-4221"
        email = "go2522@gmail.com"
        endereco = "Rua A, 123"
        data_nascimento = "11112000"

        try:
            cliente = Cliente(nome, cpf, telefone, email, endereco, data_nascimento)
            ClienteDAO.salvar_cliente(cliente)
            print("\nCliente cadastrado com sucesso!")
        except ValueError as e:
            print(f"\nErro ao cadastrar cliente:\n{e}")
    
    @classmethod
    def listar_clientes(cls):
        clientes = ClienteDAO.listar_clientes()

        for cliente in clientes:
             print(f'\nID: {formatar_id(cliente.id_cliente)} | Nome: {cliente.nome} | CPF: {cliente.cpf} | Telefone: {cliente.telefone} | Email: {cliente.email}, Endereço: {cliente.endereco} | Data de Nascimento: {cliente.data_nascimento}\n')

    @classmethod
    def pesquisar_cliente(cls, cpf):
        try:
            pesq_cliente = ClienteDAO.pesquisar_cliente(cpf)
            print(f'\nID: {formatar_id(pesq_cliente.id_cliente)} | NOME: {pesq_cliente.nome} | CPF: {pesq_cliente.cpf} | TELEFONE: {pesq_cliente.telefone} | EMAIL: {pesq_cliente.email} | ENDEREÇO: {pesq_cliente.endereco} | DATA DE NASCIMENTO: {pesq_cliente.data_nascimento}')
        except:
            print(f"\nCliente com CPF {cpf} não encontrado!")


    @classmethod
    def atualizar_cliente(cls, opcao, cpf):
        match opcao:
            case 1:
                nome = validar_nome()
                try:
                    ClienteDAO.atualizar_cliente(1, cpf, nome)
                    return True
                except:
                    return False
            case 2:
                telefone = formatar_telefone()
                try:
                    ClienteDAO.atualizar_cliente(2, cpf, telefone)
                    return True
                except:
                    return False
            case 3:
                email = validar_email()
                try:
                    ClienteDAO.atualizar_cliente(3, cpf, email)
                    return True
                except:
                    return False
            case 4:
                endereco = validar_endereco()
                try:
                    ClienteDAO.atualizar_cliente(4, cpf, endereco)
                    return True
                except:
                    return False
            case 5:
                data_nascimento = formatar_data()
                try:
                    ClienteDAO.atualizar_cliente(5, cpf, data_nascimento)
                    return True
                except:
                    return False
    
    @classmethod
    def excluir_cliente(cls):
        cpf_excluir = formatar_cpf()
        if ClienteDAO.excluir_cliente(cpf_excluir) == True:
            print(f'\nCliente com CPF {cpf_excluir} excluído com sucesso!')
        else:
            print(f'\nCliente com CPF {cpf_excluir} não encontrado.')