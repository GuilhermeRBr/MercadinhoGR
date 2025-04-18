import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAO.DAO import ClienteDAO, FuncionarioDAO, ProdutoDAO
from models.Models import Cliente, Funcionario, Produto
from validators import *
from formatters import *

class ClienteController:
    @classmethod
    def cadastrar_cliente(cls):
        nome = "felipe"
        cpf = "453.452.434-41"
        telefone = "(65) 21255-4221"
        email = "go2532@gmail.com"
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
             print(f'\nID: {cliente.id_cliente} | Nome: {cliente.nome} | CPF: {cliente.cpf} | Telefone: {cliente.telefone} | Email: {cliente.email}, Endereço: {cliente.endereco} | Data de Nascimento: {cliente.data_nascimento}\n')

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

    @classmethod
    def pesquisar_cliente(cls, cpf):
        try:
            pesq_cliente = ClienteDAO.pesquisar_cliente(cpf)
            print(f'\nID: {pesq_cliente.id_cliente} | NOME: {pesq_cliente.nome} | CPF: {pesq_cliente.cpf} | TELEFONE: {pesq_cliente.telefone} | EMAIL: {pesq_cliente.email} | ENDEREÇO: {pesq_cliente.endereco} | DATA DE NASCIMENTO: {pesq_cliente.data_nascimento}')
        except:
            print(f"\nCliente com CPF {cpf} não encontrado!")

class FuncionarioController:
    @classmethod
    def cadastrar_funcionario(cls):
        nome = validar_nome() 
        cpf = formatar_cpf()
        telefone = formatar_telefone()
        email = validar_email()
        endereco = validar_endereco()
        data_nascimento = formatar_data()
        cargo = validar_cargo()
        salario = formatar_dinheiro()

        try:
            funcionario = Funcionario(nome, cpf, telefone, email, endereco, data_nascimento, cargo, salario)
            FuncionarioDAO.salvar_funcionario(funcionario)
            print("\nFuncionário cadastrado com sucesso!") 
        except ValueError as e:
            print(f"\nErro ao cadastrar funcionário:\n{e}")

    @classmethod
    def listar_funcionarios(cls):
        funcionarios = FuncionarioDAO.listar_funcionarios()
        for funcionario in funcionarios:
            print(f'\nID: {funcionario.id_funcionario} | Nome: {funcionario.nome} | CPF: {funcionario.cpf} | Telefone: {funcionario.telefone} | Email: {funcionario.email}, Endereço: {funcionario.endereco} | Data de Nascimento: {funcionario.data_nascimento} | Cargo: {funcionario.cargo} | Salário: {funcionario.salario}\n')

    @classmethod
    def atualizar_funcionario(cls, opcao, cpf):
        match opcao:
            case 1:
                nome = validar_nome()
                try:
                    FuncionarioDAO.atualizar_funcionario(1, cpf, nome)
                    return True
                except:
                    return False
            case 2:
                telefone = formatar_telefone()
                try:
                    FuncionarioDAO.atualizar_funcionario(2, cpf, telefone)
                    return True
                except:
                    return False
            case 3:
                email = validar_email()
                try:
                    FuncionarioDAO.atualizar_funcionario(3, cpf, email)
                    return True
                except:
                    return False
            case 4:
                endereco = validar_endereco()
                try:
                    FuncionarioDAO.atualizar_funcionario(4, cpf, endereco)
                    return True
                except:
                    return False
            case 5:
                data_nascimento = formatar_data()
                try:
                    FuncionarioDAO.atualizar_funcionario(5, cpf, data_nascimento)
                    return True
                except:
                    return False
            case 6:
                cargo = validar_cargo()
                try:
                    FuncionarioDAO.atualizar_funcionario(6, cpf, cargo)
                    return True
                except:
                    return False
            case 7:
                salario = formatar_dinheiro()
                try:
                    FuncionarioDAO.atualizar_funcionario(7, cpf, salario)
                    return True
                except:
                    return False

    @classmethod
    def excluir_funcionario(cls):
        cpf_excluir = formatar_cpf()
        if FuncionarioDAO.excluir_funcionario(cpf_excluir) == True:
            print(f'\nFuncionário com CPF {cpf_excluir} excluído com sucesso!')
        else:
            print(f'\nFuncionário com CPF {cpf_excluir} não encontrado.')
    
    @classmethod
    def pesquisar_funcionario(cls, cpf):
        try:
            pesq_funcionario = FuncionarioDAO.pesquisar_funcionario(cpf)
            print(f'\nID: {pesq_funcionario.id_funcionario} | NOME: {pesq_funcionario.nome} | CPF: {pesq_funcionario.cpf} | TELEFONE: {pesq_funcionario.telefone} | EMAIL: {pesq_funcionario.email} | ENDEREÇO: {pesq_funcionario.endereco} | DATA DE NASCIMENTO: {pesq_funcionario.data_nascimento} | CARGO: {pesq_funcionario.cargo} | SALÁRIO: {pesq_funcionario.salario}\n')
        except:
            print(f"\nFuncionário com CPF {cpf} não encontrado!")

class ProdutoController:
    @classmethod
    def cadastrar_produto(cls):
        nome = 'Biscoito'
        descricao = 'Biscoito rechado com chocolate'
        preco = 'R$ 2,50'
        categoria = 'Alimentos'
        quantidade = 20

        try:
            produto = Produto(nome, descricao, preco, categoria, quantidade)
            ProdutoDAO.salvar_produto(produto)
            print("\nProduto cadastrado com sucesso!")
        except ValueError as e:
            print(f"\nErro ao cadastrar produto:\n{e}")

    @classmethod
    def listar_produtos(cls):
        produtos = ProdutoDAO.listar_produtos()

        for produto in produtos:
            print(f'\nID: {produto.id_produto} | Nome: {produto.nome} | Descrição: {produto.descricao} | Preço: {produto.preco} |Categoria: {produto.categoria} | Quantidade: {produto.quantidade}\n')
        

    @classmethod
    def atualizar_produto(cls, opcao, id_produto):
        match opcao:
            case 1:
                nome = validar_nome_produto()
                try:
                    ProdutoDAO.atualizar_produto(1, id_produto, nome)
                    return True
                except:
                    return False
            case 2:
                descricao = validar_descricao()
                try:
                    ProdutoDAO.atualizar_produto(2, id_produto, descricao)
                    return True
                except:
                    return False
            case 3:
                preco = formatar_dinheiro()
                try:
                    ProdutoDAO.atualizar_produto(3, id_produto, preco)
                    return True
                except:
                    return False
            case 4:
                quantidade = validar_quantidade()
                try:
                    ProdutoDAO.atualizar_produto(4, id_produto, quantidade)
                    return True
                except:
                    return False
            case 5:
                    categoria = validar_categoria()
                    try:
                        ProdutoDAO.atualizar_produto(5, id_produto, categoria)
                        return True
                    except:
                        return False
                

    @classmethod
    def pesquisar_produto(cls, id_produto):

        try:
            pesq_produto = ProdutoDAO.pesquisar_produto(id_produto)
            print(f'\nID: {pesq_produto.id_produto} | Nome: {pesq_produto.nome} | Descrição: {pesq_produto.descricao} | Preço: {pesq_produto.preco} |Categoria: {pesq_produto.categoria} | Quantidade: {pesq_produto.quantidade}\n')
        except:
            print(f"\nProduto com ID {id_produto} não encontrado!")

    