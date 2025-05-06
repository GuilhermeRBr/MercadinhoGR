import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller.Controller import ClienteController, FuncionarioController, ProdutoController, FornecedorController, CaixaController, AcessoGerenteController
from validators import *
from formatters import *


class Mercado:

    def __init__(self):
        self.rodando = True
        self.caixa_aberto = False
        self.caixa_bloqueado = True
        self.acesso = False

    def menu_principal(self):
        print('\nBem-vindo ao sistema de gerenciamento de mercado!')

        while self.rodando:
            print('\n == MENU PRINCIPAL ==\n' \
            '1. Caixa\n' \
            '2. Gerenciar Clientes\n' \
            '3. Gerenciar Funcionários\n' \
            '4. Gerenciar Produtos\n' \
            '5. Gerenciar Fornecedores\n' \
            '6. Relatórios\n' \
            '0. Sair\n' \
            )

            opcao = validar_opcao()

            match opcao:
                case 1: 
                    self.caixa()
                case 2:
                    self.gerenciar_clientes()
                case 3 :
                    if self.acesso == False:
                        print('\nDigite seu ID e Senha de gerente para acessar o sistema: [Digite 0 para voltar]')
                        self.acesso = AcessoGerenteController.logar_gerente()
                        if self.acesso == '0':
                            self.acesso = False
                            self.menu_principal()
                        else:
                            self.gerenciar_funcionarios()
                    else:
                        self.gerenciar_funcionarios()
                case 4:
                    if self.acesso == False:
                        print('\nDigite seu ID e Senha de gerente para acessar o sistema: [Digite 0 para voltar]')
                        self.acesso = AcessoGerenteController.logar_gerente()
                        if self.acesso == '0':
                            self.acesso = False
                            self.menu_principal()
                        else:
                            self.gerenciar_produtos()
                    else:
                        self.gerenciar_produtos()
                case 5:
                    if self.acesso == False:
                        print('\nDigite seu ID e Senha de gerente para acessar o sistema: [Digite 0 para voltar]')
                        self.acesso = AcessoGerenteController.logar_gerente()
                        if self.acesso == '0':
                            self.acesso = False
                            self.menu_principal()
                        else:
                            self.gerenciar_fornecedores()
                    else:
                        self.gerenciar_fornecedores()
                case 6:
                    if self.acesso == False:
                        print('\nDigite seu ID e Senha de gerente para acessar o sistema: [Digite 0 para voltar]')
                        self.acesso = AcessoGerenteController.logar_gerente()
                        if self.acesso == '0':
                            self.acesso = False
                            self.menu_principal()
                        else:
                            self.relatorios()
                    else:
                        self.relatorios()
                case 0:
                    print('Saindo...')
                    self.rodando = False
                case _:
                    print('Opção inválida!')
                    
    def caixa(self):
        def desbloquear_caixa():
            print('\nDigite O ID e Senha do gerente para desbloquear o caixa:')
            self.caixa_bloqueado = CaixaController.desbloquear_caixa()
    
        def vender():
            CaixaController.realizar_venda()


        if self.caixa_bloqueado == False:
            print('\nCAIXA BLOQUEADO!')
            desbloquear_caixa()
        else: 
            if self.caixa_aberto == False:      
                print('\nDigite seu ID e Senha de funcionario para abrir o caixa:')
                self.caixa_aberto = CaixaController.logar_caixa()
                self.caixa_bloqueado = self.caixa_aberto
                if self.caixa_aberto == True:
                    vender()
                    
            else:
                vender()
                
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
                self.gerenciar_clientes()
            case 2:
                ClienteController.listar_clientes()
                self.gerenciar_clientes()
            case 3:
                def atualizar_cliente(cpf_edit):
                    while True:
                        if ClienteController.pesquisar_cliente(cpf_edit):
                            print('\nEscolha o que deseja editar nesse cliente:')
                            print('\n1. Editar Nome\n' \
                            '2. Editar Telefone\n' \
                            '3. Editar Email\n' \
                            '4. Editar Endereço\n' \
                            '5. Editar Data de nascimento\n' \
                            '6. Editar Total de divida\n' \
                            '7. Editar Compras\n' \
                            '0. Voltar\n')

                            opcao = validar_opcao()

                            mensagens = {
                                1: "Nome",
                                2: "Telefone",
                                3: "Email",
                                4: "Endereço",
                                5: "Data de nascimento",
                                6: "Total de dívidas",
                                7: "Compras"
                            }

                            if opcao == 0:
                                print('\nVoltando...')
                                break
                            
                            elif opcao in mensagens:
                                if opcao == 7:
                                    print("\n-- Submenu de Compras --"
                                        "\n1. Adicionar ID de venda"
                                        "\n2. Remover ID de venda" \
                                        "\n0. Voltar")
                                    subopcao = validar_opcao()

                                    match subopcao:
                                        case 1:
                                            if ClienteController.atualizar_cliente(7, cpf_edit, subopcao): 
                                                print("\nID de venda adicionado com sucesso.")
                                            else:
                                                print("\nErro ao adicionar ID de venda.")
                                        case 2:
                                            if ClienteController.atualizar_cliente(7,cpf_edit, subopcao):
                                                print("\nID de venda removido com sucesso.")
                                            else:
                                                print("\nErro ao remover ID de venda.")
                                        case 0:
                                            print("\nVoltando...")
                                            atualizar_cliente(cpf_edit)
                                        case _:
                                            print("\nOpção inválida.")
                                else:
                                    if ClienteController.atualizar_cliente(opcao, cpf_edit):
                                        print(f'\n{mensagens[opcao]} do cliente alterado com sucesso.')
                                    else:
                                        print(f'\nErro ao alterar {mensagens[opcao].lower()} do cliente.')

                            else:
                                print('\nOpção inválida!')
                        else:
                            break
                        
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
                    while True:
                        if FuncionarioController.pesquisar_funcionario(cpf_edit):
                            print('\nEscolha o que deseja editar nesse funcionário:')
                            print('\n1. Editar Nome\n' \
                            '2. Editar Telefone\n' \
                            '3. Editar Email\n' \
                            '4. Editar Endereço\n' \
                            '5. Editar Data de nascimento\n' \
                            '6. Editar Cargo\n' \
                            '7. Editar Salário\n' \
                            '0. Voltar\n')

                            opcao = validar_opcao()

                            match opcao:
                                case 1:
                                    if FuncionarioController.atualizar_funcionario(1, cpf_edit):
                                        print('\nNome do funcionário alterado com sucesso.')
                                    else:
                                        print('\nErro ao alterar nome do funcionário.')
                                case 2:
                                    if FuncionarioController.atualizar_funcionario(2, cpf_edit):
                                        print('\nTelefone do funcionário alterado com sucesso.')
                                    else:
                                        print('\nErro ao alterar telefone do funcionário.')
                                case 3:
                                    if FuncionarioController.atualizar_funcionario(3, cpf_edit):
                                        print('\nEmail do funcionário alterado com sucesso.')
                                    else:
                                        print('\nErro ao alterar email do funcionário.')
                                case 4:
                                    if FuncionarioController.atualizar_funcionario(4, cpf_edit):
                                        print('\nEndereço do funcionário alterado com sucesso.')
                                    else:
                                        print('\nErro ao alterar endereço do funcionário.')
                                case 5:
                                    if FuncionarioController.atualizar_funcionario(5, cpf_edit):
                                        print('\nData de nascimento do funcionário alterado com sucesso.')
                                    else:
                                        print('\nErro ao alterar data de nascimento do funcionário.')
                                case 6:
                                    if FuncionarioController.atualizar_funcionario(6, cpf_edit):
                                        print('\nCargo do funcionário alterado com sucesso.')
                                    else:
                                        print('\nErro ao alterar cargo do funcionário.')
                                case 7:
                                    if FuncionarioController.atualizar_funcionario(7, cpf_edit):
                                        print('\nSalário do funcionário alterado com sucesso.')
                                    else:
                                        print('\nErro ao alterar salario do funcionário.')
                                case 0:
                                    print('\nVoltando...')
                                    break
                                case _:
                                    print('\nOpção inválida!')
                        else:
                            break


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
        '0. Voltar\n')

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
                    while True:
                        if ProdutoController.pesquisar_produto(id_produto):
                            print('\nEscolha o que deseja editar nesse produto:')
                            print('1. Nome\n'
                            '2. Descrição\n'
                            '3. Preço\n'
                            '4. Quantidade\n'
                            '5. Categoria\n'
                            '0. Voltar\n')
                            opcao = validar_opcao()
                            match opcao:
                                case 1:
                                    if ProdutoController.atualizar_produto(1, id_produto):
                                        print('\nNome do produto alterado com sucesso.')
                                    else:
                                        print('\nErro ao alterar nome do produto.')
                                case 2:
                                    if ProdutoController.atualizar_produto(2, id_produto):
                                        print('\nDescrição do produto alterado com sucesso.')
                                    else:
                                        print('\nErro ao alterar descrição do produto.')
                                case 3:
                                    if ProdutoController.atualizar_produto(3, id_produto):
                                        print('\nPreço do produto alterado com sucesso.')
                                    else:
                                        print('\nErro ao alterar preço do produto.')
                                case 4:
                                    if ProdutoController.atualizar_produto(4, id_produto):
                                        print('\nQuantidade do produto alterado com sucesso.')
                                    else:
                                        print('\nErro ao alterar quantidade do produto.')
                                case 5:
                                    pass
                                    if ProdutoController.atualizar_produto(5, id_produto):
                                        print('\nCategoria do produto alterado com sucesso.')
                                    else:
                                        print('\nErro ao alterar categoria do produto.')     
                                case 0:
                                        print('\nVoltando...')
                                        break
                                case _:
                                    print('\nOpção inválida!')
                        else:
                            break
                        
                print('\n-- Digite o ID para atualizar o produto --\n')
                id_produto = validar_id()
                atualizar_produto(id_produto)
                self.gerenciar_produtos()
            case 4:
                print('\n-- Digite o ID para excluir o produto --\n')
                ProdutoController.excluir_produto()
                self.gerenciar_produtos()
            case 5:
                print('\n-- Digite o ID para pesquisar um produto --\n')
                pesq_produto = validar_id()
                ProdutoController.pesquisar_produto(pesq_produto)
                self.gerenciar_produtos()
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
        '3. Atualizar Fornecedor(CNPJ)\n' 
        '4. Excluir Fornecedor(CNPJ)\n'
        '5. Pesquisar Fornecedor(CNPJ)\n'
        '0. Voltar\n' 
        )
        opcao = validar_opcao()

        match opcao:
            case 1:
                FornecedorController.cadastrar_fornecedor()
                self.gerenciar_fornecedores()
            case 2:
                FornecedorController.listar_fornecedores()
                self.gerenciar_fornecedores()
            case 3:
                
                def atualizar_fornecedor(cnpj):
                    while True:
                        if FornecedorController.pesquisar_fornecedor(cnpj):
                            print('\nEscolha o que deseja editar nesse fornecedor:')
                            print('1. Nome\n'
                            '2. Telefone\n'
                            '3. Email\n'
                            '4. Endereço\n'
                            '0. Voltar\n')
                            opcao = validar_opcao()
                            match opcao:
                                case 1:
                                    if FornecedorController.atualizar_fornecedor(1, cnpj):
                                        print('\nNome do fornecedor alterado com sucesso.')
                                    else:
                                        print('\nErro ao alterar nome do fornecedor.')
                                case 2:
                                    if FornecedorController.atualizar_fornecedor(2, cnpj):
                                        print('\nTelefone do fornecedor alterado com sucesso.')
                                    else:
                                        print('\nErro ao alterar telefone do fornecedor.')
                                case 3:
                                    if FornecedorController.atualizar_fornecedor(3, cnpj):
                                        print('\nEmail do fornecedor alterado com sucesso.')
                                    else:
                                        print('\nErro ao alterar email do fornecedor.')
                                case 4:
                                    if FornecedorController.atualizar_fornecedor(4, cnpj):
                                        print('\nEndereço do fornecedor alterado com sucesso.')
                                    else:
                                        print('\nErro ao alterar endereço do fornecedor.')
                                case 0:
                                        print('\nVoltando...')
                                        self.gerenciar_fornecedores()
                                case _:
                                    print('\nOpção inválida!')  
                        else:
                            break

                print('\n-- Digite o CNPJ para atualizar o fornecedor --\n')
                cnpj = formatar_cnpj()
                atualizar_fornecedor(cnpj)
            
            case 4:
                print('\n-- Digite o CNPJ para excluir um fornecedor --\n')
                FornecedorController.excluir_fornecedor()
                self.gerenciar_fornecedores()
            case 5:
                print('\n-- Digite o CNPJ para pesquisar um fornecedor --\n')
                pesq_fornecedor = formatar_cnpj()
                FornecedorController.pesquisar_fornecedor(pesq_fornecedor)
                self.gerenciar_fornecedores()
            case 0:
                print('\nVoltando...')
                self.menu_principal()
            case _:
                print('\nOpção inválida!')
                self.gerenciar_fornecedores()

    def relatorios(self):
        print('\n == MENU RELATÓRIOS ==\n'
                '1. Relatório de Vendas\n'
                '2. Relatório de Clientes\n'
                '3. Relatório de Funcionários\n'
                '4. Relatório de Produtos\n' 
                '5. Relatório de Fornecedores\n'
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
                print('\nVoltando...')
                self.menu_principal()
            case _:
                print('\nOpção inválida!')
                self.relatorios()
app = Mercado()
app.menu_principal()