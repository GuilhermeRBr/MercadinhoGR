import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAO.DAO import ClienteDAO, FuncionarioDAO, ProdutoDAO, FornecedorDAO, CaixaDAO, VendaDAO, AcessoGerenteDao
from models.Models import Cliente, Funcionario, Produto, Fornecedor, Caixa, Venda
from validators import *
from formatters import *
from generator import *
import qrcode
from pixqrcode import PixQrCode

total = 0
id_caixa, id_funcionario = '  '
produtos = []

class AcessoGerenteController:
    @classmethod
    def logar_gerente(cls):
        while True:
            id_gerente = validar_id()
            if id_gerente == '000000':
                return '0'
            else:
                senha = validar_senha()
                if AcessoGerenteDao.login_gerente(id_gerente, senha):
                    print('\nLogado com sucesso!')
                    return True
                else:
                    print(f'\nID ou senha inválidos! Tente novamente!')
                    
                

class CaixaController:
    @classmethod
    def logar_caixa(cls):
        global id_caixa, id_funcionario
        tentativas = 1
        while tentativas > 0:
            id_funcionario = '132642'
            senha = 'wAssri'

            if CaixaDAO.login_funcionario(id_funcionario, senha):
                print('\nLogado com sucesso!')
                print('\nDigite o ID do caixa: ')
                id_caixa = '000001'

                print('\nO CAIXA AGORA ESTÁ ABERTO')
                return True
            else:
                tentativas -= 1
                print(f'\nID ou senha inválidos!')
                if tentativas == 0:
                    print('\nLOGIN BLOQUEADO')
                    return False
                print(f'\nVocê tem {tentativas} tentativas restantes.')
        


    @classmethod
    def desbloquear_caixa(cls):
        id_gerente = validar_id()
        senha = validar_senha()

        if CaixaDAO.senha_gerente(id_gerente, senha):
            print('\nO CAIXA AGORA ESTÁ DESBLOQUEADO\n')
            return True
        else:
            print('\nID ou senha inválidos!')
            return False
    
    @classmethod
    def realizar_venda(cls):
        def meio_pagamento():
            global total
            print('\nDigite o metodo de pagamento:' \
            '\n1. Dinheiro' \
            '\n2. Pix' \
            '\n3. Credito' \
            '\n4. Debito' \
            '\n5. Fiado' \
            '\n9. Voltar' \
            '\n0. Cancelar venda')

            opcao = validar_opcao()

            match opcao:
                case 1:
                    print('\nPagamento em dinheiro!')

                    print(f'\nTOTAL: {float_para_dinheiro(total)}')

                    print('\nDigite o dinheiro recebido:')
                    dinheiro = dinheiro_para_float(formatar_dinheiro())
                    troco = dinheiro - total

                    if troco < 0:
                        print('\nDinheiro insuficiente!')
                        meio_pagamento()
                    else:
                        print(f'\nTROCO: {float_para_dinheiro(troco)}')

                    print('\n[Digite 0 para finalizar a venda!]' \
                    '\n[Digite 9 para alterar meio de pagamento!]')

                    while True:
                        opcao = validar_opcao()
                        if opcao == 0:
                            break
                        if opcao == 9:
                            print('\nAlterando meio de pagamento!')
                            meio_pagamento()
                        else:
                            print('\nOpção inválida!\n')

                    print('\nPagamento confirmado!')
                    
                    
                    VendaController.cadastrar_venda(id_funcionario, produtos, id_caixa, float_para_dinheiro(total), 'Dinheiro')

                    produtos.clear()
                    total = 0
                    CaixaController.realizar_venda()
        
                case 2:

                    def gerar_payload_pix(chave, valor, nome, cidade):

                        payload = f"""000201260014br.gov.bcb.pix01{len(chave):02}{chave}52040000530398654{len(f"{valor:.2f}".replace(".", "")):02}{valor:.2f}5802BR59{len(nome):02}{nome}60{len(cidade):02}{cidade}62070503***"""
                        payload = payload.replace("\n", "")  
                        return payload
                                        
                    print('\nPagamento com pix!\n')
                    chave= '77996554545'
                    nome = 'Guilherme'
                    cidade = 'bahia'

                    payload = gerar_payload_pix(chave, total, nome, cidade)

                    qr = qrcode.QRCode()
                    qr.add_data(payload)
                    qr.make()
                    qr.print_ascii(invert=True)
                    
                    print('\n[Digite 0 para finalizar a venda!]' \
                    '\n[Digite 9 para alterar meio de pagamento!]')

                    while True:
                        opcao = validar_opcao()
                        if opcao == 0:
                            break
                        if opcao == 9:
                            print('\nAlterando meio de pagamento!')
                            meio_pagamento()
                        else:
                            print('\nOpção inválida!\n')
                            
                    print('\nPagamento confirmado!')

                    VendaController.cadastrar_venda(id_funcionario, produtos, id_caixa, float_para_dinheiro(total), 'Pix')

                    produtos.clear()
                    total = 0

                    CaixaController.realizar_venda()

                case 3:
                    print('\nPagamento em credito!')
                    print(f'\nTOTAL: {float_para_dinheiro(total)}')

                    while True:
                        parcelas = input('\nDigite o numero de parcelas: ')

                        if not parcelas.isdigit:
                            print('\nParcelas inválidas!')

                        if int(parcelas) < 1 or int(parcelas) > 12:
                            print('\nParcelas inválidas!')
                        
                        else:
                            parcelas = int(parcelas)
                            break

                    print(f'\nPAGAMENTO EM {parcelas} PARCELAS')
                    print(f'\nVALOR DA PARCELA: {float_para_dinheiro(total / parcelas)} APROVADO NO CREDITO')
                     
        
                    print('\n[Digite 0 para finalizar a venda!]' \
                    '\n[Digite 9 para alterar meio de pagamento!]\n')

                    while True:
                        opcao = validar_opcao()
                        if opcao == 0:
                            break
                        if opcao == 9:
                            print('\nAlterando meio de pagamento!')
                            meio_pagamento()
                        else:
                            print('\nOpção inválida!\n')
                            
                    print('\nPagamento confirmado!')

                    VendaController.cadastrar_venda(id_funcionario, produtos, id_caixa, float_para_dinheiro(total), 'Cartão de Credito')

                    produtos.clear()
                    total = 0
                    
                    CaixaController.realizar_venda()

                case 4:
                    print('\nPagamento no debito!')
                    print(f'\nTOTAL: {float_para_dinheiro(total)}')


                    print('\n[Digite 0 para finalizar a venda!]' \
                    '\n[Digite 9 para alterar meio de pagamento!]\n')

                    while True:
                        opcao = validar_opcao()
                        if opcao == 0:
                            break
                        if opcao == 9:
                            print('\nAlterando meio de pagamento!')
                            meio_pagamento()
                        else:
                            print('\nOpção inválida!\n')
                            
                    print('\nPagamento confirmado!')

                    VendaController.cadastrar_venda(id_funcionario, produtos, id_caixa, float_para_dinheiro(total), 'Cartão de Debito')

                    produtos.clear()
                    total = 0


                    CaixaController.realizar_venda()

                case 5:
                    print('\nPagamento em fiado!')

                    total = 0
                case 9:
                    print('\nVoltando para adicionar mais produtos!')
                    venda_produtos()
                case 0:
                    print('\nCancelando venda...')
                    CaixaController.realizar_venda()
                case _:
                    print('\nOpção inválida!\n')
                    meio_pagamento()

        print(f'\n -- NOVA VENDA NO CAIXA: {id_caixa.replace('0000', '')} --')

        def venda_produtos():
            
            while True:
                global total, id_produto
                print('\nDigite o ID do produto: [0 para ir para o pagamento]')
                id_produto = validar_id()
            
                if id_produto == '000000':
                    if total == 0:
                        print('\nNenhum produto adicionado!')
                        continue
                    else:
                        print(f'\nTotal a pagar: {float_para_dinheiro(total)}')
                        meio_pagamento()

                venda = CaixaDAO.realizar_venda(id_produto)

                if venda == None:
                    print('\nProduto não encontrado!')
                    continue
                if venda == False:
                    print('\nProduto fora de estoque!')
                    continue

                while True:
                    for v in venda:
                        print(f'\nProduto: {v.nome} | Preço: {v.preco}')
                        total += dinheiro_para_float(v.preco)
                        produtos.append(v.id_produto)
                        break
                    break

                print(f'\nTotal: {float_para_dinheiro(total)}')

        venda_produtos()
        print(produtos)
        meio_pagamento()
               
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
        nome = 'Ana Maria'
        cpf = '783.752.564-41'
        telefone = '(55) 21765-4221'
        email = 'Anam@gmail.com'
        senha = gerar_senha()
        endereco = 'Rua A, endereço 123'
        data_nascimento = '30/12/2000'
        cargo = 'Caixa 4'
        salario = 'R$ 1.500,00'

        try:
            funcionario = Funcionario(nome, cpf, telefone, email, senha, endereco, data_nascimento, cargo, salario)
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
    def excluir_produto(cls):
        id_excluir = validar_id()
        if ProdutoDAO.excluir_produto(id_excluir) == True:
            print(f'\nProduto com ID {id_excluir} excluído com sucesso!')
        else:
            print(f'\nProduto com ID {id_excluir} não encontrado.')

    @classmethod
    def pesquisar_produto(cls, id_produto):

        try:
            pesq_produto = ProdutoDAO.pesquisar_produto(id_produto)
            print(f'\nID: {pesq_produto.id_produto} | Nome: {pesq_produto.nome} | Descrição: {pesq_produto.descricao} | Preço: {pesq_produto.preco} |Categoria: {pesq_produto.categoria} | Quantidade: {pesq_produto.quantidade}\n')
        except:
            print(f"\nProduto com ID {id_produto} não encontrado!")

class FornecedorController:
    @classmethod
    def cadastrar_fornecedor(cls):
        nome = 'Unilever'
        cnpj = '12.345.678/0001-90'
        telefone = '(11) 98765-4321'
        email = 'unilever@gmail.com'
        endereco = 'Rua A, 123'

        try:
            fornecedor = Fornecedor(nome, cnpj, telefone, email, endereco)
            FornecedorDAO.salvar_fornecedor(fornecedor)
            print("\nFornecedor cadastrado com sucesso!")
        except ValueError as e:
            print(f"\nErro ao cadastrar fornecedor:\n{e}")

    @classmethod
    def listar_fornecedores(cls):
        fornecedores = FornecedorDAO.listar_fornecedores()

        for fornecedor in fornecedores:
            print(f'\nID: {fornecedor.id_fornecedor} | Nome: {fornecedor.nome} | CNPJ: {fornecedor.cnpj} | Telefone: {fornecedor.telefone} | Email: {fornecedor.email} | Endereço: {fornecedor.endereco}\n')

    @classmethod
    def atualizar_fornecedor(cls, opcao, cnpj):
        match opcao:
            case 1:
                nome = validar_nome()
                try:
                    FornecedorDAO.atualizar_fornecedor(1, cnpj, nome)
                    return True
                except:
                    return False
            case 2:
                    telefone = formatar_telefone()
                    try:
                        FornecedorDAO.atualizar_fornecedor(2, cnpj, telefone)
                        return True
                    except:
                        return False
            case 3:
                    email = validar_email()
                    try:
                        FornecedorDAO.atualizar_fornecedor(3, cnpj, email)
                        return True
                    except:
                        return False
            case 4:
                    endereco = validar_endereco()
                    try:
                        FornecedorDAO.atualizar_fornecedor(4, cnpj, endereco)
                        return True
                    except:
                        return False

    @classmethod
    def excluir_fornecedor(cls):
        cnpj_excluir = formatar_cnpj()
        if FornecedorDAO.excluir_fornecedor(cnpj_excluir) == True:
            print(f'\nFornecedor com ID {cnpj_excluir} excluído com sucesso!')
        else:
            print(f'\nFornecedor com ID {cnpj_excluir} não encontrado.')

    @classmethod
    def pesquisar_fornecedor(cls, cnpj):
        try:
            pesq_fornecedor = FornecedorDAO.pesquisar_fornecedor(cnpj)
            print(f'\nID: {pesq_fornecedor.id_fornecedor} | Nome: {pesq_fornecedor.nome} | CNPJ: {pesq_fornecedor.cnpj} | Telefone: {pesq_fornecedor.telefone} | Email: {pesq_fornecedor.email} | Endereço: {pesq_fornecedor.endereco}\n')
        except:
            print(f"\nFornecedor com CNPJ {cnpj} não encontrado!")

class VendaController:
    @classmethod
    def cadastrar_venda(cls, id_funcionario, id_produtos, id_caixa, valor_total, forma_pagamento):

        try:
            venda = Venda(id_funcionario, id_produtos, id_caixa, valor_total, forma_pagamento)

            VendaDAO.salvar_venda(venda)
            print("\nVenda cadastrada com sucesso!")
        except ValueError as e:
            print(f"\nErro ao cadastrar venda:\n{e}")