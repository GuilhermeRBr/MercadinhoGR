from src.controller.controller import *
from src.utils.formatters import *
from src.utils.validators import *


class Mercado:

    def __init__(self):
        self.rodando = True
        self.caixa_aberto = False
        self.acesso = False
        self.caixa_desbloqueado = True

    def menu_principal(self):
        print('\nBem-vindo ao sistema de gerenciamento do MERCADINHO GR!')

        while self.rodando:
            print('\n == MENU PRINCIPAL ==\n' \
            '1. Abrir Caixa\n' \
            '2. Gerenciar Clientes\n' \
            '3. Gerenciar Funcionários\n' \
            '4. Gerenciar Produtos\n' \
            '5. Gerenciar Fornecedores\n' \
            '6. Vendas\n' \
            '7. Relatórios\n' \
            '8. Fechar Caixa\n' \
            '0. Sair\n' \
            )

            opcao = validar_opcao()

            match opcao:
                case 1: 
                    self.caixa()
                case 2:
                    if not self.caixa_desbloqueado:
                        print('\nACESSO BLOQUEADO!')
                        print('Digite o ID e Senha do gerente para desbloquear o acesso à aba de clientes [Digite 0 para voltar]:')
                        resultado = AcessoSistemaController.logar_gerente()
                        if resultado == '0':
                            self.menu_principal()
                            return
                        elif resultado == True:
                            self.caixa_desbloqueado = True
                            self.acesso = True
                            self.gerenciar_clientes()
                        else:
                            self.menu_principal()
                        
                    if not self.caixa_aberto:
                        print('\nDigite seu ID e Senha de funcionário para acessar a aba de clientes: [Digite 0 para voltar]')
                        resultado = AcessoSistemaController.logar_funcionario()
                        if resultado == '0':
                            self.menu_principal()
                            return
                        elif resultado == True:
                            self.gerenciar_clientes()
                        else:
                            self.caixa_desbloqueado = False
                            self.menu_principal()
                    else:
                        self.gerenciar_clientes()                   
                case 3 :
                    if self.acesso == False:
                        print('\nDigite seu ID e Senha de gerente para acessar o sistema: [Digite 0 para voltar]')
                        resultado = AcessoSistemaController.logar_gerente()
                        if resultado == '0':
                            self.acesso = False
                            self.menu_principal()
                        
                        else:
                            self.acesso = True
                            self.gerenciar_funcionarios()
                    else:
                        self.gerenciar_funcionarios()
                case 4:
                    if self.acesso == False:
                        print('\nDigite seu ID e Senha de gerente para acessar o sistema: [Digite 0 para voltar]')
                        resultado = AcessoSistemaController.logar_gerente()
                        if resultado == '0':
                            self.acesso = False
                            self.menu_principal()
                        else:
                            self.acesso = True
                            self.gerenciar_produtos()
                    else:
                        self.gerenciar_produtos()
                case 5:
                    if self.acesso == False:
                        print('\nDigite seu ID e Senha de gerente para acessar o sistema: [Digite 0 para voltar]')
                        self.acesso = AcessoSistemaController.logar_gerente()
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
                        resultado = AcessoSistemaController.logar_gerente()
                        if resultado == '0':
                            self.acesso = False
                            self.menu_principal()
                        else:
                            self.acesso = True
                            self.gerenciar_vendas()
                    else:
                        self.gerenciar_vendas()
                case 7:
                    if self.acesso == False:
                        print('\nDigite seu ID e Senha de gerente para acessar o sistema: [Digite 0 para voltar]')
                        resultado = AcessoSistemaController.logar_gerente()
                        if resultado == '0':
                            self.acesso = False
                            self.menu_principal()
                        else:
                            self.acesso = True
                            self.relatorios()
                    else:
                        self.relatorios()
                case 8:
                    if self.caixa_aberto == False:
                        print('\nO caixa já está FECHADO!')
                    else:
                        print('\nDigite seu ID e Senha de funcionario para fechar o caixa: [Digite 0 para voltar]')
                        resultado = AcessoSistemaController.logar_funcionario()
                        if resultado == '0':
                            self.menu_principal()
                            return
                        elif resultado == True:
                            self.caixa_aberto = False
                            CaixaController.fechar_caixa()
                            print('\nO caixa foi FECHADO!')
                case 0:
                    if self.caixa_aberto:
                        print('\nO caixa ainda está ABERTO! Feche-o primeiro!')
                    else:
                        print('\nSaindo...')
                        self.rodando = False
                case _:
                    print('Opção inválida!')
                    
    def caixa(self):
        def vender():
            if CaixaController.realizar_venda():
                self.menu_principal()

        if not self.caixa_desbloqueado:
            print('\nACESSO BLOQUEADO!')
            print('Digite o ID e Senha do gerente para desbloquear o caixa [Digite 0 para voltar]:')
            resultado = AcessoSistemaController.logar_gerente()
            if resultado == '0':
                self.menu_principal()
                return
            elif resultado == True:
                self.caixa_desbloqueado = True
                self.caixa_aberto = True
                self.acesso = True
                vender()
            else:
                self.menu_principal()

        if not self.caixa_aberto:
            print('\nDigite seu ID e Senha de funcionário para abrir o caixa: [Digite 0 para voltar]')
            resultado = CaixaController.logar_caixa()
            if resultado == '0':
                self.menu_principal()
                return
            elif resultado == True:
                self.caixa_aberto = True
                vender()
            else:
                self.caixa_desbloqueado = False
                self.menu_principal()
        else:
            vender()
    
    def gerenciar_clientes(self):
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
                            while True:
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
                                        break
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
        while True:       
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
                    print('\n-- Digite o CPF para atualizar o cliente [Digite 0 para voltar] --')
                    cpf_edit = formatar_cpf()
                    if cpf_edit == '0':
                        return
                    else:
                        atualizar_cliente(cpf_edit)
                case 4:
                    print('\n-- Digite o CPF para excluir cliente --')
                    ClienteController.excluir_cliente()
                case 5:
                    print('\n-- Digite o CPF para pesquisar um cliente --')
                    cpf_pesq = formatar_cpf()
                    ClienteController.pesquisar_cliente(cpf_pesq)
                case 0:
                    print('\nVoltando...')
                    break
                case _:
                    print('\nOpção inválida!')

    def gerenciar_funcionarios(self):
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
                    if opcao == 0:
                        print('\nVoltando...')
                        break
                    mensagens = {
                        1: 'Nome',
                        2: 'Telefone',
                        3: 'Email',
                        4: 'Endereço',
                        5: 'Data de nascimento',
                        6: 'Cargo',
                        7: 'Salário'
                    }

                    if opcao in mensagens:
                        sucesso = FuncionarioController.atualizar_funcionario(opcao, cpf_edit)
                        if sucesso:
                            print(f'\n{mensagens[opcao]} do funcionário alterado com sucesso.')
                        else:
                            print(f'\nErro ao alterar {mensagens[opcao].lower()} do funcionário.')
                    else:
                        print('\nOpção inválida!')

                else:
                    break
        while True:
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
                case 2:
                    FuncionarioController.listar_funcionarios()
                case 3:
                    print('\n-- Digite o CPF para atualizar o funcionário [Digite 0 para voltar] --\n')
                    cpf_edit = formatar_cpf()
                    if cpf_edit == '0':
                        return
                    else:
                        atualizar_funcionario(cpf_edit)
                case 4:
                    print('\n-- Digite o CPF para excluir funcionário --\n')
                    FuncionarioController.excluir_funcionario()
                case 5:
                    print('\n-- Digite o CPF para pesquisar um funcionário --\n')
                    pesq_funcionario = formatar_cpf()
                    FuncionarioController.pesquisar_funcionario(pesq_funcionario)
                case 0:
                    print('\nVoltando...')
                    break
                case _:
                    print('\nOpção inválida!')
    
    def gerenciar_produtos(self):
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

                    if opcao ==  0:
                        print('\nVoltando...')
                        break

                    mensagens = {
                        1: 'Nome',
                        2: 'Descrição',
                        3: 'Preço',
                        4: 'Quantidade',
                        5: 'Categoria'
                    }
                    if opcao in mensagens:
                        sucesso = ProdutoController.atualizar_produto(opcao, id_produto)
                        if sucesso:
                            print(f'\n{mensagens[opcao]} do produto alterado com sucesso.')
                        else:
                            print(f'\nErro ao alterar {mensagens[opcao].lower()} do produto.')
                    else:
                        print('\nOpção inválida!')
                else:
                    break
        while True:
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
                case 2:
                    ProdutoController.listar_produtos()
                case 3:  
                    print('\n-- Digite o ID para atualizar o produto [Digite 0 para voltar] --\n')
                    id_produto = validar_id()
                    if id_produto == '000000':
                        return
                    else:
                        atualizar_produto(id_produto)
                case 4:
                    print('\n-- Digite o ID para excluir o produto --\n')
                    ProdutoController.excluir_produto()
                case 5:
                    print('\n-- Digite o ID para pesquisar um produto --\n')
                    pesq_produto = validar_id()
                    ProdutoController.pesquisar_produto(pesq_produto)
                case 0:
                    print('\nVoltando...')
                    break
                case _:
                    print('\nOpção inválida!')

    def gerenciar_fornecedores(self):
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

                    if opcao == 0:
                        print('\nVoltando...')
                        break
                    mensagens = {
                        1: 'Nome',
                        2: 'Telefone',
                        3: 'Email',
                        4: 'Endereço'
                    }

                    if opcao in mensagens:
                        sucesso = FornecedorController.atualizar_fornecedor(opcao, cnpj)
                        if sucesso:
                            print(f'\n{mensagens[opcao]} do fornecedor atualizado com sucesso.')
                        else:
                            print(f'\nErro ao atualizar {mensagens[opcao].lower()} do fornecedor.')
                    else:
                        print('\nOpção inválida!')
                else:
                    break
        while True:
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
                case 2:
                    FornecedorController.listar_fornecedores()
                case 3:
                    print('\n-- Digite o CNPJ para atualizar o fornecedor [Digite 0 para voltar] --\n')
                    cnpj = formatar_cnpj()
                    if cnpj == '0':
                        return
                    else:
                        atualizar_fornecedor(cnpj)
                case 4:
                    print('\n-- Digite o CNPJ para excluir um fornecedor --\n')
                    FornecedorController.excluir_fornecedor()
                case 5:
                    print('\n-- Digite o CNPJ para pesquisar um fornecedor --\n')
                    pesq_fornecedor = formatar_cnpj()
                    FornecedorController.pesquisar_fornecedor(pesq_fornecedor)
                case 0:
                    print('\nVoltando...')
                    break
                case _:
                    print('\nOpção inválida!')

    def gerenciar_vendas(self):
        while True:
            opcoes = {
                1: VendaController.listar_vendas,
                2: lambda: VendaController.pesquisar_venda(validar_id()),
                0: lambda: print('\nVoltando...'),
            }

            print('\n == MENU VENDAS ==\n'
                    '1. Listar Vendas\n'
                    '2. Pesquisar Venda(ID)\n'
                    '0. Voltar\n')
            opcao = validar_opcao()

            acao = opcoes.get(opcao)
            if acao:
                acao()
                if opcao == 0:
                    self.menu_principal()
                    break
            else:
                print('\nOpção inválida!')

    def relatorios(self):
        opcoes = {
            1: RelatorioController.total_vendas,
            2: RelatorioController.total_vendas_por_funcionario,
            3: RelatorioController.total_por_pagamento,
            4: RelatorioController.mais_vendidos,
            5: lambda: RelatorioController.relatorio_mensal(*input_mes_ano()),
            6: RelatorioController.relatorio_geral,
            0: lambda: print('\nVoltando...')
        }

        while True:
            print('\n== MENU RELATÓRIOS ==\n'
                '1. Total de vendas\n'
                '2. Total de vendas por funcionários\n'
                '3. Total de vendas por forma de pagamento\n'
                '4. Os 5 produtos mais vendidos\n'
                '5. Relatório por mês do ano\n'
                '6. Dados do mercado\n'
                '0. Voltar\n'
                )
            opcao = validar_opcao()

            acao = opcoes.get(opcao)
            if acao:
                acao()
                if opcao == 0:
                    self.menu_principal()
                    break
            else:
                print('\nOpção inválida!')

app = Mercado()
app.menu_principal()