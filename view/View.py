import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller.Controller import ClienteController
from models.Models import Pessoa, Cliente
from DAO.DAO import ClienteDAO
from validators import validar_opcao
from formatters import *


class Mercado:
    def __init__(self):
        self.rodando = True
    
    def menu_principal(self):
        while self.rodando:

            print('\n== MENU PRINCIPAL ==\n' \
            '1. Caixa\n' \
            '2. Gerenciar Clientes\n' \
            '3. Gerenciar Funcionários\n' \
            '4. Gerenciar Produtos\n' \
            '5. Gerenciar Fornecedores\n' \
            '6. Gerenciar Categorias\n' \
            '7. Relatórios\n' \
            '0. Sair\n' \
            )

            opcao = validar_opcao()

            match opcao:
                case 1:
                    self.caixa()
                case 2:
                    self.gerenciar_clientes()
                case 3 :
                    self.gerenciar_funcionarios()
                case 4:
                    self.gerenciar_produtos()
                case 5:
                    self.gerenciar_fornecedores()
                case 6:
                    self.gerenciar_categorias()
                case 7:
                    self.relatorios()
                case 0:
                    print('Saindo...')
                    self.rodando = False
                case _:
                    print('Opção inválida!')
    def caixa(self):
        print('Caixa')
    
    def gerenciar_clientes(self):

        print('\n == MENU CLIENTES ==\n' \
                 '1. Cadastrar Cliente\n' \
                 '2. Listar Clientes\n' \
                 '3. Atualizar Cliente(CPF)\n' \
                 '4. Excluir Cliente(CPF)\n' \
                 '5. Pesquisar Cliente(CPF)\n' \
                 '0. Voltar\n' \
                )
        opcao = validar_opcao()
        
        match opcao:
            case 1:
                ClienteController.cadastrar_cliente()
              
            case 2:
                ClienteController.listar_clientes()

            case 3:
                def atualizar_cliente(cpf_edit):
                    print('\nEscolha o que deseja editar nesse cliente:')
                    ClienteController.pesquisar_cliente(edit_cpf)
                    print('\n1. Editar nome\n' \
                    '2. Editar telefone\n' \
                    '3. Editar email\n' \
                    '4. Editar endereço\n' \
                    '5. Editar data de nascimento\n' \
                    '0. Voltar\n')

                    opcao = validar_opcao()

                    match opcao:
                        case 1:
                            ClienteController.atualizar_cliente(1)
                        case 2:
                            ClienteController.atualizar_cliente(2)
                        case 3:
                            ClienteController.atualizar_cliente(3)
                        case 4:
                            ClienteController.atualizar_cliente(4)
                        case 5:
                            ClienteController.atualizar_cliente(5)
                        case 0:
                            print('Voltando...')
                            self.gerenciar_clientes()
                        case _:
                            print('Opção inválida!')
                            self.gerenciar_clientes()

                edit_cpf = formatar_cpf()
                atualizar_cliente(edit_cpf)


            case 4:
                print('\n--Exluir cliente--')
                cpf_excluir = formatar_cpf()
                ClienteDAO.excluir_cliente(cpf_excluir)
                
            case 5:
                cpf_pesquisa = formatar_cpf()
                ClienteController.pesquisar_cliente(cpf_pesquisa)
            case 0:
                print('Voltando...')
                self.menu_principal()
            case _:
                print('Opção inválida!')
                self.gerenciar_clientes()

    
    def gerenciar_funcionarios(self):
        print('\n == MENU FUNCIONÁRIOS ==\n' \
                '1. Cadastrar Funcionário\n' \
                '2. Listar Funcionários\n' \
                '3. Atualizar Funcionário\n' \
                '4. Excluir Funcionário\n' \
                '5. Pesquisar Funcionário(ID)\n' \
                '0. Voltar\n' 
                )
        
        opcao = validar_opcao()

        match opcao:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 0:
                print('Voltando...')
                self.menu_principal()
            case _:
                print('Opção inválida!')
                self.gerenciar_funcionarios()
    
    def gerenciar_produtos(self):
        print('\n == MENU PRODUTOS ==\n' \
        '1. Cadastrar Produtos\n' \
        '2. Listar Produtos\n' \
        '3. Atualizar Produtos\n' \
        '4. Excluir Produtos\n' \
        '5. Pesquisar Produtos(ID)\n' \
        '0. Voltar\n' ) 

        opcao = validar_opcao()
        match opcao:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 0:
                print('Voltando...')
                self.menu_principal()
            case _:
                print('Opção inválida!')
                self.gerenciar_produtos()

    def gerenciar_fornecedores(self):
        print('\n == MENU FORNECEDORES ==\n' 
        '1. Cadastrar Fornecedor\n'
        '2. Listar Fornecedores\n' 
        '3. Atualizar Fornecedor\n' 
        '4. Excluir Fornecedor\n'
        '5. Pesquisar Fornecedor(ID)\n'
        '0. Voltar\n' 
        )
        opcao = validar_opcao()

        match opcao:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 0:
                print('Voltando...')
                self.menu_principal()
            case _:
                print('Opção inválida!')
                self.gerenciar_fornecedores()

    def gerenciar_categorias(self):
        print('\n == MENU CATEGORIAS ==\n'
        '1. Cadastrar Categoria\n'
        '2. Listar Categorias\n'
        '3. Atualizar Categoria\n'
        '4. Excluir Categoria\n'
        '5. Pesquisar Categoria(ID)\n'
        '0. Voltar\n' 
        )
        
        opcao = validar_opcao()
        match opcao:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 0:
                print('Voltando...')
                self.menu_principal()
            case _:
                print('Opção inválida!')
                self.gerenciar_categorias()

    def relatorios(self):
        print('\n == MENU RELATÓRIOS ==\n'
                '1. Relatório de Vendas\n'
                '2. Relatório de Clientes\n'
                '3. Relatório de Funcionários\n'
                '4. Relatório de Produtos\n' 
                '5. Relatório de Fornecedores\n'
                '6. Relatório de Categorias\n'
                '0. Voltar\n'   
              )
        opcao = validar_opcao()
        match opcao:
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 0:
                print('Voltando...')
                self.menu_principal()
            case _:
                print('Opção inválida!')
                self.relatorios()
app = Mercado()
app.menu_principal()