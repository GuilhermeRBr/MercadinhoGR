import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller.Controller import ClienteController, FuncionarioController, ProdutoController
from validators import *
from formatters import *


class Mercado:
    def __init__(self):
        self.rodando = True
    
    def menu_principal(self):
        print('\nBem-vindo ao sistema de gerenciamento de mercado!')

        while self.rodando:
            print('\n == MENU PRINCIPAL ==\n' \
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
                 '9. Sair\n' \
                 '0. Voltar\n' \
                )
        opcao = validar_opcao()
        
        match opcao:
            case 1:
                ClienteController.cadastrar_cliente()
                self.gerenciar_clientes()
            case 2:
                ClienteController.listar_clientes()
                self.gerenciar_clientes()
            case 3:
                def atualizar_cliente(cpf_edit):
                    ClienteController.pesquisar_cliente(cpf_edit)

                    print('\nEscolha o que deseja editar nesse cliente:')
                    print('\n1. Editar Nome\n' \
                    '2. Editar Telefone\n' \
                    '3. Editar Email\n' \
                    '4. Editar Endereço\n' \
                    '5. Editar Data de nascimento\n' \
                    '9. Sair\n')
                    '0. Voltar\n'

                    opcao = validar_opcao()

                    match opcao:
                        case 1:
                            if ClienteController.atualizar_cliente(1, cpf_edit):
                                print('\nNome do cliente alterado com sucesso.')
                            else:
                                print('\nErro ao alterar nome do cliente.')
                            atualizar_cliente(cpf_edit)
                        case 2:
                            if ClienteController.atualizar_cliente(2, cpf_edit):
                                print('\nTelefone do cliente alterado com sucesso.')
                            else:
                                print('\nErro ao alterar telefone do cliente.')
                            atualizar_cliente(cpf_edit)
                        case 3:
                            if ClienteController.atualizar_cliente(3, cpf_edit):
                                print('\nEmail do cliente alterado com sucesso.')
                            else:
                                print('\nErro ao alterar email do cliente.')
                            atualizar_cliente(cpf_edit)
                        case 4:
                            if ClienteController.atualizar_cliente(4, cpf_edit):
                                print('\nEndereço do cliente alterado com sucesso.')
                            else:
                                print('\nErro ao alterar endereço do cliente.')
                            atualizar_cliente(cpf_edit)
                        case 5:
                            if ClienteController.atualizar_cliente(5, cpf_edit):
                                print('\nData de nascimento do cliente alterado com sucesso.')
                            else:
                                print('\nErro ao alterar data de nascimento do cliente.')
                            atualizar_cliente(cpf_edit)
                        case 9:
                            print('\nSaindo...')
                            self.rodando = False
                        case 0:
                            print('\nVoltando...')
                            self.gerenciar_clientes()
                        case _:
                            print('\nOpção inválida!')
                            atualizar_cliente(cpf_edit)

                print('\n-- Digite o CPF para atualizar o cliente --')
                cpf_edit = formatar_cpf()
                atualizar_cliente(cpf_edit)
                self.gerenciar_clientes()

            case 4:
                print('\n-- Digite o CPF para excluir cliente --')
                ClienteController.excluir_cliente()
                self.gerenciar_clientes()
                
            case 5:
                print('\n-- Digite o CPF para pesquisar um cliente --')
                cpf_pesq = formatar_cpf()
                ClienteController.pesquisar_cliente(cpf_pesq)
                self.gerenciar_clientes()

            case 9:
                print('\nSaindo...')
                self.rodando = False
            case 0:
                print('\nVoltando...')
                self.menu_principal()
            case _:
                print('\nOpção inválida!')
                self.gerenciar_clientes()

    
    def gerenciar_funcionarios(self):
        print('\n == MENU FUNCIONÁRIOS ==\n' \
                '1. Cadastrar Funcionário\n' \
                '2. Listar Funcionários\n' \
                '3. Atualizar Funcionário(CPF)\n' \
                '4. Excluir Funcionário(CPF)\n' \
                '5. Pesquisar Funcionário(CPF)\n' \
                '9. Sair\n' 
                '0. Voltar\n' 
                )
        
        opcao = validar_opcao()

        match opcao:
            case 1:
                FuncionarioController.cadastrar_funcionario()
                self.gerenciar_funcionarios()
            case 2:
                FuncionarioController.listar_funcionarios()
                self.gerenciar_funcionarios()
            case 3:
                def atualizar_funcionario(cpf_edit):
                    FuncionarioController.pesquisar_funcionario(cpf_edit)

                    print('\nEscolha o que deseja editar nesse funcionário:')
                    print('\n1. Editar Nome\n' \
                    '2. Editar Telefone\n' \
                    '3. Editar Email\n' \
                    '4. Editar Endereço\n' \
                    '5. Editar Data de nascimento\n' \
                    '6. Editar Cargo\n' \
                    '7. Editar Salário\n' \
                    '9. Sair\n'
                    '0. Voltar\n')

                    opcao = validar_opcao()

                    match opcao:
                        case 1:
                            if FuncionarioController.atualizar_funcionario(1, cpf_edit):
                                print('\nNome do funcionário alterado com sucesso.')
                            else:
                                print('\nErro ao alterar nome do funcionário.')
                            atualizar_funcionario(cpf_edit)
                        case 2:
                            if FuncionarioController.atualizar_funcionario(2, cpf_edit):
                                print('\nTelefone do funcionário alterado com sucesso.')
                            else:
                                print('\nErro ao alterar telefone do funcionário.')
                            atualizar_funcionario(cpf_edit)
                        case 3:
                            if FuncionarioController.atualizar_funcionario(3, cpf_edit):
                                print('\nEmail do funcionário alterado com sucesso.')
                            else:
                                print('\nErro ao alterar email do funcionário.')
                            atualizar_funcionario(cpf_edit)
                        case 4:
                            if FuncionarioController.atualizar_funcionario(4, cpf_edit):
                                print('\nEndereço do funcionário alterado com sucesso.')
                            else:
                                print('\nErro ao alterar endereço do funcionário.')
                            atualizar_funcionario(cpf_edit)
                        case 5:
                            if FuncionarioController.atualizar_funcionario(5, cpf_edit):
                                print('\nData de nascimento do funcionário alterado com sucesso.')
                            else:
                                print('\nErro ao alterar data de nascimento do funcionário.')
                            atualizar_funcionario(cpf_edit)
                        case 6:
                            if FuncionarioController.atualizar_funcionario(6, cpf_edit):
                                print('\nCargo do funcionário alterado com sucesso.')
                            else:
                                print('\nErro ao alterar cargo do funcionário.')
                            atualizar_funcionario(cpf_edit)
                        case 7:
                            if FuncionarioController.atualizar_funcionario(7, cpf_edit):
                                print('\nSalário do funcionário alterado com sucesso.')
                            else:
                                print('\nErro ao alterar salario do funcionário.')
                            atualizar_funcionario(cpf_edit)
                        case 9:
                            print('\nSaindo...')
                            self.rodando = False
                        case 0:
                            print('\nVoltando...')
                            self.gerenciar_clientes()
                        case _:
                            print('\nOpção inválida!')
                            atualizar_funcionario(cpf_edit)


                print('\n-- Digite o CPF para atualizar o funcionário --\n')
                cpf_edit = formatar_cpf()
                atualizar_funcionario(cpf_edit)
                self.gerenciar_funcionarios()
            case 4:
                print('\n-- Digite o CPF para excluir funcionário --\n')
                FuncionarioController.excluir_funcionario()
                self.gerenciar_funcionarios()
            case 5:
                print('\n-- Digite o CPF para pesquisar um funcionário --\n')
                pesq_funcionario = formatar_cpf()
                FuncionarioController.pesquisar_funcionario(pesq_funcionario)
                self.gerenciar_funcionarios()
            case 9:
                print('\nSaindo...')
                self.rodando = False
            case 0:
                print('\nVoltando...')
                self.menu_principal()
            case _:
                print('\nOpção inválida!')
                self.gerenciar_funcionarios()
    
    def gerenciar_produtos(self):
        print('\n == MENU PRODUTOS ==\n' \
        '1. Cadastrar Produtos\n' \
        '2. Listar Produtos\n' \
        '3. Atualizar Produtos(ID)\n' \
        '4. Excluir Produtos(ID)\n' \
        '5. Pesquisar Produtos(ID)\n' \
        '9. Sair\n') 
        '0. Voltar\n'

        opcao = validar_opcao()
        match opcao:
            case 1:
                ProdutoController.cadastrar_produto()
                self.gerenciar_produtos()
            case 2:
                ProdutoController.listar_produtos()
                self.gerenciar_produtos()
            case 3:
                def atualizar_produto(id_produto):
                    ProdutoController.pesquisar_produto(id_produto)
                    print('\nEscolha o que deseja editar nesse produto:')
                    print('1. Nome\n'
                    '2. Descrição\n'
                    '3. Preço\n'
                    '4. Quantidade\n'
                    '5. Categoria\n'
                    '9. Sair\n'
                    '0. Voltar\n')
                    opcao = validar_opcao()
                    match opcao:
                        case 1:
                            if ProdutoController.atualizar_produto(1, id_produto):
                                print('\nNome do produto alterado com sucesso.')
                            else:
                                print('\nErro ao alterar nome do produto.')
                            atualizar_produto(id_produto)
                        case 2:
                            if ProdutoController.atualizar_produto(2, id_produto):
                                print('\nDescrição do produto alterado com sucesso.')
                            else:
                                print('\nErro ao alterar descrição do produto.')
                            atualizar_produto(id_produto)
                        case 3:
                            if ProdutoController.atualizar_produto(3, id_produto):
                                print('\nPreço do produto alterado com sucesso.')
                            else:
                                print('\nErro ao alterar preço do produto.')
                            atualizar_produto(id_produto)
                        case 4:
                            if ProdutoController.atualizar_produto(4, id_produto):
                                print('\nQuantidade do produto alterado com sucesso.')
                            else:
                                print('\nErro ao alterar quantidade do produto.')
                            atualizar_produto(id_produto)
                        case 5:
                            pass
                            if ProdutoController.atualizar_produto(5, id_produto):
                                print('\nCategoria do produto alterado com sucesso.')
                            else:
                                print('\nErro ao alterar categoria do produto.')
                            atualizar_produto(id_produto)
                        case 9:
                                print('\nSaindo...')
                                self.rodando = False
                        case 0:
                                print('\nVoltando...')
                                self.gerenciar_produtos()
                        case _:
                            print('\nOpção inválida!')
                            atualizar_produto(id_produto)
                        
                print('\n-- Digite o ID para atualizar o produto --\n')
                id_produto = validar_id()
                atualizar_produto(id_produto)
                self.gerenciar_produtos()
            case 5:
                print('\n-- Digite o ID para pesquisar um produto --\n')
                pesq_produto = validar_id()
                ProdutoController.pesquisar_produto(pesq_produto)
                self.gerenciar_produtos()
            case 9:
                print('\nSaindo...')
                self.rodando = False
            case 0:
                print('\nVoltando...')
                self.menu_principal()
            case _:
                print('\nOpção inválida!')
                self.gerenciar_produtos()

    def gerenciar_fornecedores(self):
        print('\n == MENU FORNECEDORES ==\n' 
        '1. Cadastrar Fornecedor\n'
        '2. Listar Fornecedores\n' 
        '3. Atualizar Fornecedor\n' 
        '4. Excluir Fornecedor\n'
        '5. Pesquisar Fornecedor(ID)\n'
        '9. Sair\n'
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
            case 9:
                print('\nSaindo...')
                self.rodando = False
            case 0:
                print('\nVoltando...')
                self.menu_principal()
            case _:
                print('\nOpção inválida!')
                self.gerenciar_fornecedores()

    def gerenciar_categorias(self):
        print('\n == MENU CATEGORIAS ==\n'
        '1. Cadastrar Categoria\n'
        '2. Listar Categorias\n'
        '3. Atualizar Categoria\n'
        '4. Excluir Categoria\n'
        '5. Pesquisar Categoria(ID)\n'
        '9. Sair\n'
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
            case 9:
                print('\nSaindo...')
                self.rodando = False
            case 0:
                print('\nVoltando...')
                self.menu_principal()
            case _:
                print('\nOpção inválida!')
                self.gerenciar_categorias()

    def relatorios(self):
        print('\n == MENU RELATÓRIOS ==\n'
                '1. Relatório de Vendas\n'
                '2. Relatório de Clientes\n'
                '3. Relatório de Funcionários\n'
                '4. Relatório de Produtos\n' 
                '5. Relatório de Fornecedores\n'
                '6. Relatório de Categorias\n'
                '9. Sair\n'
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
            case 9:
                print('\nSaindo...')
                self.rodando = False
            case 0:
                print('\nVoltando...')
                self.menu_principal()
            case _:
                print('\nOpção inválida!')
                self.relatorios()
app = Mercado()
app.menu_principal()