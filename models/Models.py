class Pessoa:
    def __init__(self, nome, cpf, telefone, email, endereco, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.data_nascimento = data_nascimento

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, telefone, email, endereco, data_nascimento, cargo, salario, id_funcionario=None):
        super().__init__(nome, cpf, telefone, email, endereco, data_nascimento)
        self.cargo = cargo
        self.salario = salario
        self.id_funcionario = id_funcionario

class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, email, endereco, data_nascimento, id_cliente=None):
        super().__init__(nome, cpf, telefone, email, endereco, data_nascimento)
        self.id_cliente = id_cliente


class Produto:
    def __init__(self, nome ,descricao, preco,categoria, quantidade, id_produto=None):
        self.id_produto = id_produto
        self.nome = nome
        self.descricao = descricao
        self.preco = preco
        self.categoria = categoria
        self.quantidade = quantidade

class Fornecedor:
    def __init__(self, nome, cnpj, telefone, email, endereco, id_fornecedor=None):
        self.id_fornecedor = id_fornecedor
        self.nome = nome
        self.cnpj = cnpj
        self.telefone = telefone
        self.email = email
        self.endereco = endereco

class Venda:
    def __init__(self, id_venda, id_cliente, id_funcionario, produtos, data_venda):
        self.id_venda = id_venda
        self.cliente = id_cliente
        self.funcionario = id_funcionario
        self.produtos = produtos 
        self.data_venda = data_venda

class Estoque:
    def __init__(self, id_estoque, id_produto, quantidade):
        self.id_estoque = id_estoque
        self.id_produto = id_produto
        self.quantidade = quantidade

class Categoria:
    def __init__(self, id_categoria, nome_categoria):
        self.id_categoria = id_categoria
        self.nome_categoria = nome_categoria

class Caixa:
    def __init__(self, id_caixa, id_funcionario, data_abertura, data_fechamento):
        self.id_caixa = id_caixa
        self.id_funcionario = id_funcionario
        self.data_abertura = data_abertura
        self.data_fechamento = data_fechamento

class Pagamento:
    def __init__(self, id_pagamento, id_venda, id_caixa, valor, forma_pagamento):
        self.id_pagamento = id_pagamento
        self.id_venda = id_venda
        self.id_caixa = id_caixa
        self.valor = valor
        self.forma_pagamento = forma_pagamento