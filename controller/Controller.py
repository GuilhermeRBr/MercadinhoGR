import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from DAO.DAO import *
from models.Models import *
from utils.formatters import *
from utils.validators import *
from utils.generator import *
import qrcode
from collections import defaultdict
from pixqrcode import PixQrCode
from datetime import datetime


total = 0
id_caixa, id_funcionario, sair = '   '
produtos,id_venda, venda_temporaria = [], [], []

class AcessoSistemaController:
    @classmethod
    def logar_gerente(cls):
        while True:
            id_gerente = "745454"
            if id_gerente == '000000':
                return '0'
            else:
                senha = '856949'
                if AcessoSistemaDao.login_gerente(id_gerente, senha):
                    print('\nLogado com sucesso!')
                    return True
                else:
                    print(f'\nID ou senha inválidos! Tente novamente!')
    
    @classmethod
    def logar_funcionario(cls):
            global id_funcionario
            tentativas = 1
            while tentativas > 0:
                id_funcionario = '132642'
                if id_funcionario == '000000':
                    return '0'
                else:
                    senha = 'wAssri'
                    if CaixaDAO.login_funcionario(id_funcionario, senha):
                        print('\nLogado com sucesso!')
                        return True
                    else:
                        tentativas -= 1
                        print(f'\nID ou senha inválidos!')
                        if tentativas == 0:
                            print('\nLOGIN BLOQUEADO')
                            return False
                        print(f'\nVocê tem {tentativas} tentativas restantes.')
                    
class CaixaController:
    @classmethod
    def logar_caixa(cls):
        global id_caixa, id_funcionario
        tentativas = 1
        while tentativas > 0:
            id_funcionario = '877655'
            if id_funcionario == '000000':
                return '0'
            else:
                senha = '123456'
                if CaixaDAO.login_funcionario(id_funcionario, senha):
                    print('\nLogado com sucesso!')
                    print('\nDigite o ID do caixa: ')
                    id_caixa = '000002'

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
    def realizar_venda(cls):
        def meio_pagamento():
            global total, id_caixa
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
                            print('\nPagamento confirmado!')
                            CaixaDAO.realizar_venda(venda_temporaria)

                            VendaController.cadastrar_venda(id_funcionario, produtos, id_caixa, float_para_dinheiro(total), 'Dinheiro')

                            venda_temporaria.clear()
                            produtos.clear()
                            total = 0

                            break
                        if opcao == 9:
                            print('\nAlterando meio de pagamento!')
                            meio_pagamento()
                        else:
                            print('\nOpção inválida!\n')
        
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
                            print('\nPagamento confirmado!')
                            CaixaDAO.realizar_venda(venda_temporaria)

                            VendaController.cadastrar_venda(id_funcionario, produtos, id_caixa, float_para_dinheiro(total), 'Pix')

                            venda_temporaria.clear()
                            produtos.clear()
                            total = 0

                            break
                        if opcao == 9:
                            print('\nAlterando meio de pagamento!')
                            meio_pagamento()
                        else:
                            print('\nOpção inválida!\n')

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
                            print('\nPagamento confirmado!')
                            CaixaDAO.realizar_venda(venda_temporaria)

                            VendaController.cadastrar_venda(id_funcionario, produtos, id_caixa, float_para_dinheiro(total), 'Cartão de Credito')

                            venda_temporaria.clear()
                            produtos.clear()
                            total = 0

                            break
                        if opcao == 9:
                            print('\nAlterando meio de pagamento!')
                            meio_pagamento()
                        else:
                            print('\nOpção inválida!\n')

                case 4:
                    print('\nPagamento no debito!')
                    print(f'\nTOTAL: {float_para_dinheiro(total)}')


                    print('\n[Digite 0 para finalizar a venda!]' \
                    '\n[Digite 9 para alterar meio de pagamento!]\n')

                    while True:
                        opcao = validar_opcao()
                        if opcao == 0:
                            print('\nPagamento confirmado!')
                            CaixaDAO.realizar_venda(venda_temporaria)
        
                            VendaController.cadastrar_venda(id_funcionario, produtos, id_caixa, float_para_dinheiro(total), 'Cartão de Debito')

                            venda_temporaria.clear()   
                            produtos.clear()
                            total = 0

                            break
                        if opcao == 9:
                            print('\nAlterando meio de pagamento!')
                            meio_pagamento()
                        else:
                            print('\nOpção inválida!\n')
                    

                    CaixaController.realizar_venda()

                case 5:
                    print('\nPagamento em fiado!')
                    print(f'\nTOTAL: {float_para_dinheiro(total)}')
                    while True:
                        print('\nO cliente já é cadastrado? [1. Sim / 2. Não / 0. Cancelar] ')
                        opcao = validar_opcao()

                        vendas = VendaDAO.listar_vendas()

                        id_vendas = gerar_id()
                        for v in vendas:
                            if v.id_venda == id_vendas:
                                id_vendas = gerar_id()
                                break

                        match opcao:
                            case 1:
                                print('\nDigite o CPF do cliente:')
                                cpf = formatar_cpf()
                                cliente = ClienteController.pesquisar_cliente(cpf)
                                if cliente == False:
                                    print('\nCliente não encontrado!')
                                    continue
                                else:
                                    ClienteDAO.atualizar_divida(cpf, total, id_vendas)
                                    print(f'\nDivida atualizada com sucesso!')

                                    ClienteController.pesquisar_cliente(cpf)

                                    CaixaDAO.realizar_venda(venda_temporaria)

                                    VendaController.cadastrar_venda(id_funcionario, produtos, id_caixa, float_para_dinheiro(total), 'Fiado')

                                    venda_temporaria.clear()
                                    produtos.clear()
                                    total = 0

                                    break

                            case 2:
                                print('\nCadastrando cliente...')

                                nome = validar_nome()
                                cpf = formatar_cpf()
                                telefone = formatar_telefone()
                                email = validar_email()
                                endereco = validar_endereco()
                                data_nascimento = formatar_data()
                                divida = float_para_dinheiro(total)
                                
                                if ClienteController.cliente_fiado(nome, cpf, telefone, email, endereco, data_nascimento, divida):
                                     
                                    ClienteController.pesquisar_cliente(cpf)

                                    CaixaDAO.realizar_venda(venda_temporaria)

                                    VendaController.cadastrar_venda(id_funcionario, produtos, id_caixa, float_para_dinheiro(total), 'Fiado', id_vendas)

                                    venda_temporaria.clear()
                                    produtos.clear()
                                    total = 0
                                    break

                            case 0:
                                print('\nCancelando venda...')
                                return
                            case _:
                                print('\nOpção inválida!')
                                continue
            

                    
                    CaixaController.realizar_venda()

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
                global total, id_produto, sair
                print('\nDigite o ID do produto: [0 para ir para o pagamento / V para cancelar]')
                id_produto = validar_id()

                if id_produto == 'v':
                    sair = 'v'
                    venda_temporaria.clear()
                    break
            
                if id_produto == '000000':
                    if total == 0:
                        print('\nNenhum produto adicionado!')
                        continue
                    else:
                        print(f'\nTotal a pagar: {float_para_dinheiro(total)}')
                        meio_pagamento()
                        continue

                produto = ProdutoDAO.pesquisar_produto(id_produto)

                if produto and produto.quantidade > 0:
                    print(f'\nProduto: {produto.nome} | Preço: {produto.preco}')
                    venda_temporaria.append(produto.id_produto)
                    total += dinheiro_para_float(produto.preco)
                    produtos.append(produto.id_produto)
                else:
                    print('\nProduto não encontrado!')
                    continue

                print(f'\nTotal: {float_para_dinheiro(total)}')

        venda_produtos()

        if sair != 'v':
            meio_pagamento()
        else:
            print('\nVoltando para o menu...')
            return True
               
class ClienteController:
    @classmethod
    def cadastrar_cliente(cls):
        nome = validar_nome()
        cpf = formatar_cpf()
        telefone = formatar_telefone()
        email = validar_email()
        endereco = validar_endereco()
        data_nascimento = formatar_data()
        total_divida = formatar_dinheiro()
        id_venda = []

        try:
            cliente = Cliente(nome, cpf, telefone, email, endereco, data_nascimento, total_divida, id_venda)
            ClienteDAO.salvar_cliente(cliente)
            print("\nCliente cadastrado com sucesso!")
        except ValueError as e:
            print(f"\nErro ao cadastrar cliente:\n{e}")
    
    @classmethod
    def listar_clientes(cls):
        clientes = ClienteDAO.listar_clientes()
        if len(clientes) == 0:
            print('\nNenhum cliente cadastrado!')
        else:
            for cliente in clientes:
                print(f'\nID: {cliente.id_cliente} | Nome: {cliente.nome} | CPF: {cliente.cpf} | Telefone: {cliente.telefone} | Email: {cliente.email}, Endereço: {cliente.endereco} | Data de Nascimento: {cliente.data_nascimento} | TOTAL DE DIVIDAS: {cliente.total_divida} | ID DAS COMPRAS: {', ' .join(v for v in cliente.id_venda) if cliente.id_venda else 'Não há dívidas'} \n')


    @classmethod
    def atualizar_cliente(cls, opcao, cpf, dados_venda=None):
        clientes = ClienteDAO.listar_clientes()
        vendas = VendaDAO.listar_vendas()


        for cliente in clientes:

            if cpf == cliente.cpf:
                total_divida = dinheiro_para_float(cliente.total_divida)
                break

        acoes = {
            1: validar_nome,
            2: formatar_telefone,
            3: validar_email,
            4: validar_endereco,
            5: formatar_data,
            6: formatar_dinheiro,
            7: validar_id
        }

        if opcao in acoes:
            if opcao == 7:
                valor = acoes[opcao]()

                for venda in vendas:    
                    if valor in venda.id_venda:
                        compras = dinheiro_para_float(venda.valor_total)
                    
                if dados_venda == 1:
                    for venda in vendas:
                        if valor in venda.id_venda:
                            valor_adicionar = compras + total_divida

                            ClienteDAO.atualizar_cliente(opcao, cpf, valor, dados_venda, float_para_dinheiro(valor_adicionar))
                            return True
                else:
                    for cliente in clientes:
                        if valor in cliente.id_venda:
                            valor_subtrair = total_divida - compras
                            
                            ClienteDAO.atualizar_cliente(opcao, cpf, valor, dados_venda, float_para_dinheiro(valor_subtrair))
                            return True
            else:          
                try:
                    valor = acoes[opcao]()
                    ClienteDAO.atualizar_cliente(opcao, cpf, valor)
                    return True
                except:
                    return False
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
            print(f'\nID: {pesq_cliente.id_cliente} | NOME: {pesq_cliente.nome} | CPF: {pesq_cliente.cpf} | TELEFONE: {pesq_cliente.telefone} | EMAIL: {pesq_cliente.email} | ENDEREÇO: {pesq_cliente.endereco} | DATA DE NASCIMENTO: {pesq_cliente.data_nascimento} | TOTAL DE DIVIDAS: {pesq_cliente.total_divida} | ID DAS COMPRAS: {', ' .join(v for v in pesq_cliente.id_venda) if pesq_cliente.id_venda else 'Não há dívidas'}\n')
            return True
        except:
            print(f"\nCliente com CPF {cpf} não encontrado!")
            return False
    
    @classmethod
    def cliente_fiado(cls, nome, cpf, telefone, email, endereco, data_nascimento, total_divida, id_venda=None):
        try:
            cliente = Cliente(nome, cpf, telefone, email, endereco, data_nascimento, total_divida, id_venda)
            ClienteDAO.salvar_cliente(cliente)
            print("\nCliente cadastrado com sucesso!")
            return True
        except ValueError as e:
            print(f"\nErro ao cadastrar cliente:\n{e}")
            return False

class FuncionarioController:
    @classmethod
    def cadastrar_funcionario(cls):
        nome = validar_nome()
        cpf = formatar_cpf()
        telefone = formatar_telefone()
        email = validar_email()
        senha = gerar_senha()
        endereco = validar_endereco()
        data_nascimento =  formatar_data()
        cargo = validar_cargo()
        salario = formatar_dinheiro()

        try:
            funcionario = Funcionario(nome, cpf, telefone, email, senha, endereco, data_nascimento, cargo, salario)
            FuncionarioDAO.salvar_funcionario(funcionario)
            print("\nFuncionário cadastrado com sucesso!") 
        except ValueError as e:
            print(f"\nErro ao cadastrar funcionário:\n{e}")

    @classmethod
    def listar_funcionarios(cls):
        funcionarios = FuncionarioDAO.listar_funcionarios()
        if len(funcionarios) == 0:
            print('\nNenhum funcionário cadastrado!')
        else:
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
            return True
        except:
            print(f"\nFuncionário com CPF {cpf} não encontrado!")
            return False

class ProdutoController:
    @classmethod
    def cadastrar_produto(cls):
        nome = validar_nome_produto()
        descricao = validar_descricao()
        preco = formatar_dinheiro()
        categoria = validar_categoria()
        quantidade = validar_quantidade()

        try:
            produto = Produto(nome, descricao, preco, categoria, quantidade)
            ProdutoDAO.salvar_produto(produto)
            print("\nProduto cadastrado com sucesso!")
        except ValueError as e:
            print(f"\nErro ao cadastrar produto:\n{e}")

    @classmethod
    def listar_produtos(cls):
        produtos = ProdutoDAO.listar_produtos()
        if len(produtos) == 0:
            print('\nNenhum produto cadastrado!')
        else:
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
            return True
        except:
            print(f"\nProduto com ID {id_produto} não encontrado!")
            return False

class FornecedorController:
    @classmethod
    def cadastrar_fornecedor(cls):
        nome = validar_nome()
        cnpj = formatar_cnpj()
        telefone = formatar_telefone()
        email = validar_email()
        endereco = validar_endereco()

        try:
            fornecedor = Fornecedor(nome, cnpj, telefone, email, endereco)
            FornecedorDAO.salvar_fornecedor(fornecedor)
            print("\nFornecedor cadastrado com sucesso!")
        except ValueError as e:
            print(f"\nErro ao cadastrar fornecedor:\n{e}")

    @classmethod
    def listar_fornecedores(cls):
        fornecedores = FornecedorDAO.listar_fornecedores()
        if len(fornecedores) == 0:
            print('\nNenhum fornecedor cadastrado!')
        else:
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
            return True
        except:
            print(f"\nFornecedor com CNPJ {cnpj} não encontrado!")
            return False

class VendaController:
    @classmethod
    def cadastrar_venda(cls, id_funcionario, id_produtos, id_caixa, valor_total, forma_pagamento, id_venda=None):
        try:
            venda = Venda(id_funcionario, id_produtos, id_caixa, valor_total, forma_pagamento, id_venda)

            VendaDAO.salvar_venda(venda)
            print("\nVenda cadastrada com sucesso!")
        except ValueError as e:
            print(f"\nErro ao cadastrar venda:\n{e}")
    
    @classmethod
    def listar_vendas(cls):
        vendas = VendaDAO.listar_vendas()
        if len(vendas) == 0:
            print('\nNenhuma venda cadastrada!')
        else:
            for venda in vendas:
                print(f'\nID DA VENDA: {venda.id_venda} | ID FUNCIONARIO: {venda.id_funcionario} | ID PRODUTOS: {', ' .join(v for v in venda.id_produtos)} | ID CAIXA: {venda.id_caixa} | VALOR TOTAL: {venda.valor_total} | FORMA DE PAGAMENTO: {venda.forma_pagamento}\n')   
    
    @classmethod
    def pesquisar_venda(cls, id_venda):
        try:
            pesq_venda = VendaDAO.pesquisar_venda(id_venda)
            print(f'\nID DA VENDA: {pesq_venda.id_venda} | ID FUNCIONARIO: {pesq_venda.id_funcionario} | ID PRODUTOS: {', ' .join(v for v in pesq_venda.id_produtos)} | ID CAIXA: {pesq_venda.id_caixa} | VALOR TOTAL: {pesq_venda.valor_total} | FORMA DE PAGAMENTO: {pesq_venda.forma_pagamento}\n')
            return True
        except:
            print(f"\nVenda com ID {id_venda} não encontrada!")
            return False
        
class RelatorioController:
    @classmethod
    def mais_vendidos(cls):
        vendas = VendaDAO.listar_vendas()
        produtos = ProdutoDAO.listar_produtos()
        contador = defaultdict(int)

        if len(vendas) == 0:
            print('\nNenhuma venda cadastrada!')
        else:
            for venda in vendas:
                 for produto in venda.id_produtos:
                    contador[produto] += 1
            mais_vendidos = sorted(contador.items(), key=lambda x: x[1], reverse=True)[0:5]
            print('\nOS 5 PRODUTOS MAIS VENDIDOS:')
            for produto, quantidade in mais_vendidos:
                for prod in produtos:
                    if prod.id_produto == produto:
                        print(f"ID DO PRODUTO: {prod.id_produto} | NOME DO PRODUTO: {prod.nome} | VALOR: {prod.preco} | QUANTIDADE DE VENDAS: {quantidade}")

    @classmethod
    def total_vendas(cls):
        vendas = VendaDAO.listar_vendas()
        total_vendas = total_quantidade = 0
        if len(vendas) == 0:
            print('\nNenhuma venda cadastrada!')
        else:
            for venda in vendas:
                total_vendas += dinheiro_para_float(venda.valor_total)
                total_quantidade += 1
            print(f'\nO TOTAL DE VENDAS FOI: {float_para_dinheiro(total_vendas)} | TOTAL DE VENDAS: {total_quantidade} | VALOR MÉDIO POR VENDA: {float_para_dinheiro(total_vendas / total_quantidade)}')

    @classmethod
    def total_vendas_por_funcionario(cls):
        vendas = VendaDAO.listar_vendas()
        funcionarios = FuncionarioDAO.listar_funcionarios()
        total_vendas = defaultdict(int)
        contador = defaultdict(int)
        if len(vendas) == 0:
            print('\nNenhuma venda cadastrada!')
        else:
            for venda in vendas:
                contador[venda.id_funcionario] += 1
                total_vendas[venda.id_funcionario] += dinheiro_para_float(venda.valor_total)
            print('\nTOTAL DE VENDAS POR FUNCIONÁRIO:')
            for funcionario in funcionarios:
                for id_funcionario, total in total_vendas.items():
                    if funcionario.id_funcionario == id_funcionario:
                        print(f"ID DO FUNCIONÁRIO: {funcionario.id_funcionario} | NOME DO FUNCIONÁRIO: {funcionario.nome} | TOTAL DE VENDAS: {contador[id_funcionario]} | VALOR TOTAL: {float_para_dinheiro(total_vendas[id_funcionario])}")

    @classmethod
    def total_por_pagamento(cls):
        vendas = VendaDAO.listar_vendas()
        total_vendas = defaultdict(int)
        if len(vendas) == 0:
            print('\nNenhuma venda cadastrada!')
        else:
            for venda in vendas:
                total_vendas[venda.forma_pagamento] += dinheiro_para_float(venda.valor_total)
            print('\nTOTAL DE VENDAS POR FORMA DE PAGAMENTO:')
            for forma_pagamento, total in total_vendas.items():
                print(f"FORMA DE PAGAMENTO: {forma_pagamento} | VALOR TOTAL: {float_para_dinheiro(total)}")
    
    @classmethod
    def relatorio_geral(cls):
        vendas = VendaDAO.listar_vendas()
        funcionarios = FuncionarioDAO.listar_funcionarios()
        produtos = ProdutoDAO.listar_produtos()
        fornecedores = FornecedorDAO.listar_fornecedores()
        clientes = ClienteDAO.listar_clientes()

        print(f'\nTOTAL DE VENDAS: {len(vendas)}')
        print(f'TOTAL DE FUNCIONÁRIOS: {len(funcionarios)}')
        print(f'TOTAL DE PRODUTOS: {len(produtos)}')
        print(f'TOTAL DE FORNECEDORES: {len(fornecedores)}')
        print(f'TOTAL DE CLIENTES: {len(clientes)}')

    @classmethod
    def relatorio_mensal(cls, mes, ano):
        vendas = VendaDAO.listar_vendas()
        produtos = ProdutoDAO.listar_produtos()
        funcionarios = FuncionarioDAO.listar_funcionarios()
        contador = defaultdict(int)
        contador_funcionario = defaultdict(int)
        total_vendas_funcionario = defaultdict(int)
        total_vendas_pagamento = defaultdict(int)
        total_vendas_caixa = defaultdict(int)
        total_vendas = total_quantidade = 0

        encontrou_data = any(
                (data := datetime.strptime(venda.data_venda, "%d/%m/%Y %H:%M:%S")).month == mes and
                data.year == ano
                for venda in vendas
            )
        if len(vendas) == 0:
            print('\nNenhuma venda cadastrada!')
        else:
            if not encontrou_data:
                print("Não tem venda nesse mês e ano")
            else:
                for venda in vendas:
                    data = datetime.strptime(venda.data_venda, "%d/%m/%Y %H:%M:%S").date()
                    if data.month == mes and data.year == ano:
                        for produto in venda.id_produtos:
                            contador[produto] += 1

                        contador_funcionario[venda.id_funcionario] += 1
                        total_vendas_funcionario[venda.id_funcionario] += dinheiro_para_float(venda.valor_total)

                        total_vendas += dinheiro_para_float(venda.valor_total)
                        total_quantidade += 1

                        total_vendas_pagamento[venda.forma_pagamento] += dinheiro_para_float(venda.valor_total)

                        total_vendas_caixa[venda.id_caixa] += dinheiro_para_float(venda.valor_total)
                    
                mais_vendidos = sorted(contador.items(), key=lambda x: x[1], reverse=True)[0:5]

                print('\nOS 5 PRODUTOS MAIS VENDIDOS NO MÊS:')
                for produto, quantidade in mais_vendidos:
                    for prod in produtos:
                        if prod.id_produto == produto:
                            print(f"ID DO PRODUTO: {prod.id_produto} | NOME DO PRODUTO: {prod.nome} | VALOR: {prod.preco} | QUANTIDADE DE VENDAS: {quantidade}")

                print('\nTOTAL DE VENDAS POR FUNCIONÁRIO NO MÊS:')
                for funcionario in funcionarios:
                    for id_funcionario, total in total_vendas_funcionario.items():
                        if funcionario.id_funcionario == id_funcionario:
                            print(f"ID DO FUNCIONÁRIO: {funcionario.id_funcionario} | NOME DO FUNCIONÁRIO: {funcionario.nome} | TOTAL DE VENDAS: {contador_funcionario[id_funcionario]} | VALOR TOTAL: {float_para_dinheiro(total_vendas_funcionario[id_funcionario])}")

                print('\nTOTAL DE VENDAS POR FORMA DE PAGAMENTO NO MÊS:')
                for forma_pagamento, total in total_vendas_pagamento.items():
                    print(f"FORMA DE PAGAMENTO: {forma_pagamento} | VALOR TOTAL: {float_para_dinheiro(total)}")

                print('\nTOTAL DE VENDAS POR CAIXA NO MÊS:')
                for caixa, total in total_vendas_caixa.items():
                    print(f"ID DA CAIXA: {caixa.replace('00000', '0')} | VALOR TOTAL: {float_para_dinheiro(total)}")
                
                print(f'\nO TOTAL DE VENDAS NO MÊS FOI: {float_para_dinheiro(total_vendas)} | TOTAL DE VENDAS: {total_quantidade} | VALOR MÉDIO POR VENDA: {float_para_dinheiro(total_vendas / total_quantidade)}')
