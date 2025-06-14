class Pessoa:
    def __init__(self, nome, cpf, telefone, email, endereco, data_nascimento):
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.data_nascimento = data_nascimento

class Funcionario(Pessoa):
    def __init__(self, nome, cpf, telefone, email, senha, endereco, data_nascimento, cargo, salario, id_funcionario=None):
        super().__init__(nome, cpf, telefone, email, endereco, data_nascimento)
        self.cargo = cargo
        self.salario = salario
        self.senha = senha
        self.id_funcionario = id_funcionario

class Cliente(Pessoa):
    def __init__(self, nome, cpf, telefone, email, endereco, data_nascimento,total_divida, id_venda=None, id_cliente=None):
        super().__init__(nome, cpf, telefone, email, endereco, data_nascimento)
        self.id_cliente = id_cliente
        self.total_divida = total_divida
        self.id_venda = id_venda


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
    def __init__(self, id_funcionario, id_produtos, id_caixa, valor_total, forma_pagamento, id_venda=None, data_venda=None, id_pagamento=None):
        self.id_funcionario = id_funcionario
        self.id_produtos = id_produtos 
        self.id_caixa = id_caixa
        self.valor_total = valor_total
        self.forma_pagamento = forma_pagamento
        self.data_venda = data_venda
        self.id_venda = id_venda
        self.id_pagamento = id_pagamento

class Caixa:
    def __init__(self, id_caixa, id_funcionario, data_abertura, data_fechamento):
        self.id_caixa = id_caixa
        self.id_funcionario = id_funcionario
        self.data_abertura = data_abertura
        self.data_fechamento = data_fechamento
