import json
from generator import gerar_id
from models.Models import Cliente, Funcionario, Produto, Fornecedor


class CaixaDAO:
    @classmethod
    def login_funcionario(cls, id, senha):
        with open('data/funcionarios.json', 'r', encoding='utf-8') as arq:
            funcionarios = json.load(arq)
        
        for f in funcionarios:
            if f['id_funcionario'] == id and f['senha'] == senha:
                return True
    
    @classmethod
    def desbloquear_caixa(cls, id, senha):
        with open('data/funcionarios.json', 'r', encoding='utf-8') as arq:
            funcionarios = json.load(arq)

        for f in funcionarios:
            if f['cargo'].lower() == 'gerente':
                if f['id_funcionario'] == id and f['senha'] == senha:
                    return True
    
    @classmethod
    def realizar_venda(cls, id_produto):
        with open ('data/produtos.json', 'r', encoding='utf-8') as arq:
            produtos = json.load(arq)
            venda = []
        for p in produtos:
            if p['id_produto'] == id_produto:
                p['quantidade'] -= 1
                id_produto, nome, descricao, preco, categoria, quantidade = p.values()
                produto = Produto(nome, descricao, preco, categoria, quantidade, id_produto)
                venda.append(produto)
                return venda

        with open('data/produtos.json', 'w', encoding='utf-8') as arq:
            json.dump(produtos, arq, indent=4)

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

        id_cliente = gerar_id()
        for c in clientes:
            if c['id_cliente'] == id_cliente:
                id_cliente = gerar_id()
            if c['cpf'] == cliente.cpf:
                erros.append(f"Erro: CPF '{cliente.cpf}' já cadastrado.")
            if c['telefone'] == cliente.telefone:
                erros.append(f"Erro: Telefone '{cliente.telefone}' já cadastrado.")
            if c['email'] == cliente.email:
                erros.append(f"Erro: E-mail '{cliente.email}' já cadastrado.")
        if erros:
            raise ValueError('\n'.join(erros))
        
        clientes.append({
            'id_cliente': id_cliente,
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

        id_funcionario = gerar_id()
        for f in funcionarios:
            if f['id_funcionario'] == id_funcionario:
                id_funcionario = gerar_id()
            if f['cpf'] == funcionario.cpf:
                erros.append(f'Erro: CPF {funcionario.cpf} já cadastrado.')
            if f['telefone'] == funcionario.telefone:
                erros.append(f'Erro: Telefone {funcionario.telefone} já cadastrado.')
            if f['email'] == funcionario.email:
                    erros.append(f'Erro: E-mail {funcionario.email} já cadastrado.')
        if erros:
            raise ValueError('\n'.join(erros))

        funcionarios.append({
            'id_funcionario': id_funcionario,
            'nome': funcionario.nome,
            'cpf': funcionario.cpf,
            'telefone': funcionario.telefone,
            'email': funcionario.email,
            'senha': funcionario.senha,
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
                id_funcionario, nome, cpf, telefone, email, senha, endereco, data_nascimento, cargo, salario = f.values()
                funcionario = Funcionario(nome, cpf, telefone, email, senha, endereco, data_nascimento, cargo, salario, id_funcionario)
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
                id_funcionario, nome, cpf, telefone, email, senha, endereco, data_nascimento, cargo, salario = f.values()
                
                return Funcionario(nome, cpf, telefone, email, senha, endereco, data_nascimento, cargo, salario, id_funcionario)
            
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

        id_produto = gerar_id()
        for p in produtos:
            if p['id_produto'] == id_produto:
                id_produto = gerar_id()
            if p['descricao'] == produto.descricao:
                erros.append(f'Erro: Descrição {produto.descricao} já cadastrada.')
        if erros:
            raise ValueError('\n'.join(erros))
        
        produtos.append({
            'id_produto': id_produto,
            'nome': produto.nome,
            'descricao': produto.descricao,
            'preco': produto.preco,
            'categoria': produto.categoria,
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
                id_produto, nome, descricao, preco, categoria, quantidade = p.values()
                produto = Produto(nome, descricao, preco, categoria, quantidade, id_produto)
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
    def excluir_produto(cls, id_produto):
        with open('data/produtos.json', 'r', encoding='utf-8') as arq:
            produtos = json.load(arq)
        
        for i, produto in enumerate(produtos):
            if produto['id_produto'] == id_produto:
                del produtos[i]
                with open('data/produtos.json', 'w', encoding='utf-8') as arq:
                    json.dump(produtos, arq, indent=4, ensure_ascii=False)
                return True
            else:
                return False

    @classmethod
    def pesquisar_produto(cls, id_produto):
        with open('data/produtos.json', 'r', encoding='utf-8') as arq:
            produtos = json.load(arq)
        
        for p in produtos:
            if p['id_produto'] == id_produto:
                id_produto, nome, descricao, preco, categoria, quantidade = p.values()

                return Produto(nome, descricao, preco, categoria, quantidade, id_produto)

class FornecedorDAO:
    @classmethod
    def salvar_fornecedor(cls, fornecedor: Fornecedor):
        erros = []
        fornecedores = []
        try:
            with open('data/fornecedores.json', 'r', encoding='utf-8') as arq:
                fornecedores = json.load(arq)
        except FileNotFoundError:
            fornecedores = []

        id_fornecedor = gerar_id()
        for f in fornecedores:
            if f['id_fornecedor'] == id_fornecedor:
                id_fornecedor = gerar_id()
            if f['cnpj'] == fornecedor.cnpj:
                erros.append(f'Erro: CNPJ {fornecedor.cnpj} já cadastrado.')
            if f['telefone'] == fornecedor.telefone:
                erros.append(f'Erro: Telefone {fornecedor.telefone} já cadastrado.')
            if f['email'] == fornecedor.email:
                erros.append(f'Erro: E-mail {fornecedor.email} já cadastrado.')
        
        if erros:
            raise ValueError('\n'.join(erros))
        
        fornecedores.append({
            'id_fornecedor': id_fornecedor,
            'nome': fornecedor.nome,
            'cnpj': fornecedor.cnpj,
            'telefone': fornecedor.telefone,
            'email': fornecedor.email,
            'endereco': fornecedor.endereco
        })

        with open('data/fornecedores.json', 'w', encoding='utf-8') as arq:
            json.dump(fornecedores, arq, indent=4, ensure_ascii=False)

    @classmethod
    def listar_fornecedores(cls):
        with open('data/fornecedores.json', 'r', encoding='utf-8') as arq:
            fornecedores = json.load(arq)
            lista_fornecedores = []
        
        for f in fornecedores:
                id_fornecedor, nome, cnpj, telefone, email, endereco = f.values()
                fornecedor = Fornecedor(nome, cnpj, telefone, email, endereco, id_fornecedor)
                lista_fornecedores.append(fornecedor)

        return lista_fornecedores
    
    @classmethod
    def atualizar_fornecedor(cls, opcao, cnpj, dados):
        with open('data/fornecedores.json', 'r', encoding='utf-8') as arq:
            fornecedores = json.load(arq)
            for f in fornecedores:
                if f['cnpj'] == cnpj:
                        match opcao:
                            case 1:
                                f['nome'] = dados
                            case 2:
                                f['telefone'] = dados
                            case 3:
                                f['email'] = dados
                            case 4:
                                f['endereco'] = dados

        with open('data/fornecedores.json', 'w', encoding='utf-8') as arq:
            json.dump(fornecedores, arq, indent=4, ensure_ascii=False)


    @classmethod
    def excluir_fornecedor(cls, cnpj):
        with open('data/fornecedores.json', 'r', encoding='utf-8') as arq:
            fornecedores = json.load(arq)

        for i, fornecedor in enumerate(fornecedores):
            if fornecedor['cnpj'] == cnpj:
                del fornecedores[i]
                with open('data/fornecedores.json', 'w', encoding='utf-8') as arq:
                    json.dump(fornecedores, arq, indent=4, ensure_ascii=False)
                return True
            else:
                return False

    @classmethod
    def pesquisar_fornecedor(cls, cnpj):
        with open('data/fornecedores.json', 'r', encoding='utf-8') as arq:
            fornecedores = json.load(arq)

        for f in fornecedores:
            if f['cnpj'] == cnpj:
                id_fornecedor, nome, cnpj, telefone, email, endereco = f.values()

                return Fornecedor(nome, cnpj, telefone, email, endereco, id_fornecedor)
            
    


