import json
import os
import sys
from formatters import formatar_id
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from models.Models import Cliente, Funcionario, Produto

class ClienteDAO:
    @classmethod
    def salvar_cliente(cls, cliente: Cliente):
        erros = []
        clientes = []
        try:
            with open('data/clientes.json', 'r', encoding='utf-8') as arq:
                clientes = json.load(arq)
        except FileNotFoundError:
            clientes = []

        ids_usados = sorted(int(c['id_cliente']) for c in clientes)
        id_cliente = 1
        for id_existente in ids_usados:
            if id_existente == id_cliente:
                id_cliente += 1
            else:
                break

        for c in clientes:
            if c['cpf'] == cliente.cpf:
                erros.append(f"Erro: CPF '{cliente.cpf}' já cadastrado.")
            if c['telefone'] == cliente.telefone:
                erros.append(f"Erro: Telefone '{cliente.telefone}' já cadastrado.")
            if c['email'] == cliente.email:
                erros.append(f"Erro: E-mail '{cliente.email}' já cadastrado.")
        if erros:
            raise ValueError('\n'.join(erros))
        
        clientes.append({
            'id_cliente': formatar_id(str(id_cliente)),
            'nome': cliente.nome,
            'cpf': cliente.cpf,
            'telefone': cliente.telefone,
            'email': cliente.email,
            'endereco': cliente.endereco,
            'data_nascimento': cliente.data_nascimento,
        })

        with open('data/clientes.json', 'w', encoding='utf-8') as arq:
            json.dump(clientes, arq, indent=4, ensure_ascii=False)

    @classmethod
    def listar_clientes(cls):
        with open('data/clientes.json', 'r', encoding='utf-8') as arq:
            clientes = json.load(arq)
            lista_clientes = []
            for c in clientes:
                id_cliente, nome,  cpf, telefone, email, endereco, data_nascimento= c.values()
                cliente = Cliente(nome, cpf, telefone, email, endereco, data_nascimento, id_cliente)
                lista_clientes.append(cliente)

            return lista_clientes
        
    @classmethod
    def atualizar_cliente(cls, opcao, cpf, dados):   
        with open('data/clientes.json', 'r', encoding='utf-8') as arq:
            clientes = json.load(arq)

        for c in clientes:
            if c['cpf'] == cpf:
                    match opcao:
                        case 1:
                            c['nome'] = dados
                        case 2:
                            c['telefone'] = dados
                        case 3:
                            c['email'] = dados
                        case 4:
                            c['endereco'] = dados
                        case 5:
                            c['data_nascimento'] = dados
        
        with open('data/clientes.json', 'w', encoding='utf-8') as arq:
            json.dump(clientes, arq, indent=4)


    @classmethod        
    def excluir_cliente(cls, cpf):
        with open('data/clientes.json', 'r', encoding='utf-8') as arq:
            clientes = json.load(arq)
            
        for i, cliente in enumerate(clientes):
            if cliente['cpf'] == cpf:
                del clientes[i]
                with open('data/clientes.json', 'w', encoding='utf-8') as arq:
                    json.dump(clientes, arq, indent=4, ensure_ascii=False)
                return True
            else:
                return False

    @classmethod
    def pesquisar_cliente(cls, cpf):
        with open('data/clientes.json', 'r', encoding='utf-8') as arq:
            clientes = json.load(arq)
        
        for c in clientes:
            if c['cpf'] == cpf:
                id_cliente, nome, cpf, telefone, email, endereco, data_nascimento = c.values()
                return Cliente(nome, cpf, telefone, email, endereco, data_nascimento, id_cliente)

class FuncionarioDAO:
    @classmethod
    def salvar_funcionario(cls, funcionario: Funcionario):
        erros = []
        funcionarios = []
        try:
            with open('data/funcionarios.json', 'r', encoding='utf-8') as arq:
                funcionarios = json.load(arq)
        except FileNotFoundError:
            funcionarios = []

        ids_usados = sorted(int(f['id_funcionario']) for f in funcionarios)
        id_funcionario = 1
        for id_exitente in ids_usados:
            if id_exitente == id_funcionario:
                id_funcionario += 1
            else:
                break
        
        for f in funcionarios:
            if f['cpf'] == funcionario.cpf:
                erros.append(f'Erro: CPF {funcionario.cpf} já cadastrado.')
            if f['telefone'] == funcionario.telefone:
                erros.append(f'Erro: Telefone {funcionario.telefone} já cadastrado.')
            if f['email'] == funcionario.email:
                    erros.append(f'Erro: E-mail {funcionario.email} já cadastrado.')
        if erros:
            raise ValueError('\n'.join(erros))

        funcionarios.append({
            'id_funcionario': formatar_id(str(id_funcionario)),
            'nome': funcionario.nome,
            'cpf': funcionario.cpf,
            'telefone': funcionario.telefone,
            'email': funcionario.email,
            'endereco': funcionario.endereco,
            'data_nascimento': funcionario.data_nascimento,
            'cargo': funcionario.cargo,
            'salario': funcionario.salario,
        })

        with open('data/funcionarios.json', 'w', encoding='utf-8') as arq:
            json.dump(funcionarios, arq, indent=4, ensure_ascii=False)

    @classmethod
    def listar_funcionarios(cls):
        with open('data/funcionarios.json', 'r', encoding='utf-8') as arq:
            funcionarios = json.load(arq)
            lista_funcionarios = []
            
            for f in funcionarios:
                id_funcionario, nome, cpf, telefone, email, endereco, data_nascimento, cargo, salario = f.values()
                funcionario = Funcionario(nome, cpf, telefone, email, endereco, data_nascimento, cargo, salario, id_funcionario)
                lista_funcionarios.append(funcionario)

            return lista_funcionarios
        
    @classmethod
    def atualizar_funcionario(cls, opcao, cpf, dados):
        with open('data/funcionarios.json', 'r', encoding='utf-8') as arq:
            funcionarios = json.load(arq)
        for f in funcionarios:
            if f['cpf'] == cpf:
                    match opcao:
                        case 1:
                            f['nome'] = dados
                        case 2:
                            f['telefone'] = dados
                        case 3:
                            f['email'] = dados
                        case 4:
                            f['endereco'] = dados
                        case 5:
                            f['data_nascimento'] = dados
                        case 6:
                            f['cargo'] = dados
                        case 7:
                            f['salario'] = dados

        with open('data/funcionarios.json', 'w', encoding='utf-8') as arq:
            json.dump(funcionarios, arq, indent=4)

    @classmethod
    def excluir_funcionario(cls, cpf):
        with open('data/funcionarios.json', 'r', encoding='utf-8') as arq:
            funcionarios = json.load(arq)
        
        for i, funcionario in enumerate(funcionarios):
            if funcionario['cpf'] == cpf:
                del funcionarios[i]
                with open('data/funcionarios.json', 'w', encoding='utf-8') as arq:
                    json.dump(funcionarios, arq, indent=4, ensure_ascii=False)
                return True
            else:
                return False

    @classmethod
    def pesquisar_funcionario(cls, cpf):
        with open('data/funcionarios.json', 'r', encoding='utf-8') as arq:
            funcionarios = json.load(arq)

        for f in funcionarios:
            if f['cpf'] == cpf:
                id_funcionario, nome, cpf, telefone, email, endereco, data_nascimento, cargo, salario = f.values()
                
                return Funcionario(nome, cpf, telefone, email, endereco, data_nascimento, cargo, salario, id_funcionario)
            
class ProdutoDAO:
    @classmethod
    def salvar_produto(cls, produto: Produto):
        erros = []
        produtos = []
        try:
            with open('data/produtos.json', 'r', encoding='utf-8') as arq:
                produtos = json.load(arq)
        except FileNotFoundError:
            produtos = []

        ids_usados = sorted(int(p['id_produto']) for p in produtos)
        id_produto = 1
        for id_exitente in ids_usados:
            if id_exitente == id_produto:
                id_produto += 1
            else:
                break
        for p in produtos:
            if p['descricao'] == produto.descricao:
                erros.append(f'Erro: Descrição {produto.descricao} já cadastrada.')
        if erros:
            raise ValueError('\n'.join(erros))
        
        produtos.append({
            'id_produto': formatar_id(str(id_produto)),
            'nome': produto.nome,
            'descricao': produto.descricao,
            'preco': produto.preco,
            'quantidade': produto.quantidade
        })

        with open('data/produtos.json', 'w', encoding='utf-8') as arq:
            json.dump(produtos, arq, indent=4, ensure_ascii=False)

    @classmethod
    def listar_produtos(cls):
        with open('data/produtos.json', 'r', encoding='utf-8') as arq:
            produtos = json.load(arq)
            lista_produtos = []

            for p in produtos:
                id_produto, nome, descricao, preco, quantidade = p.values()
                produto = Produto(nome, descricao, preco, quantidade, id_produto)
                lista_produtos.append(produto)

            return lista_produtos
        

    @classmethod
    def atualizar_produto(cls, opcao, id_produto, dados):
        with open('data/produtos.json', 'r', encoding='utf-8') as arq:
            produtos = json.load(arq)

        for p in produtos:
            if p['id_produto'] == id_produto:
                    match opcao:
                        case 1:
                            p['nome'] = dados
                        case 2:
                            p['descricao'] = dados
                        case 3:
                            p['preco'] = dados
                        case 4:
                            p['quantidade'] = dados
            
        with open('data/produtos.json', 'w', encoding='utf-8') as arq:
            json.dump(produtos, arq, indent=4)

    
    @classmethod
    def pesquisar_produto(cls, id_produto):
        with open('data/produtos.json', 'r', encoding='utf-8') as arq:
            produtos = json.load(arq)
        
        for p in produtos:
            if p['id_produto'] == id_produto:
                id_produto, nome, descricao, preco, quantidade = p.values()

                return Produto(nome, descricao, preco, quantidade, id_produto)
               