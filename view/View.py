import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller.Controller import PessoaController
from validators import validar_opcao


class Mercado:
    def __init__(self):
        self.rodando = True
    
    def menu_principal(self):
        while self.rodando:

            print('\n== MENU PRINCIPAL ==\n' \
            '1. Caixa\n' \
            '2. Gerenciar Clientes\n' \
            '3. Gerenciar Funcionários' \
            '4. Gerenciar Produtos\n' \
            '5. Gerenciar Fornecedores\n' \
            '6. Gerenciar Categorias\n' \
            '7. Relatórios\n' \
            '0. Sair\n' \
            )

            opcao = validar_opcao(input('Digite a opção desejada: '))

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
                 '3. Atualizar Cliente\n' \
                 '4. Excluir Cliente\n' \
                 '5. Pesquisar Cliente\n' \
                 '0. Voltar\n' \
                )
        opcao = validar_opcao(input('Digite a opção desejada: '))
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
                self.gerenciar_clientes()

    
    def gerenciar_funcionarios(self):
        print('Gerenciar Funcionários')
    
    def gerenciar_produtos(self):
        print('Gerenciar Produtos')

    def gerenciar_fornecedores(self):
        print('Gerenciar Fornecedores')

    def gerenciar_categorias(self):
        print('Gerenciar Categorias')

    def relatorios(self):
        print('Relatórios')

app = Mercado()
app.menu_principal()