from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Text, DateTime, create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from datetime import datetime


import os
from dotenv import load_dotenv
load_dotenv()

engine = create_engine(os.getenv("DATABASE_URL"), echo=True)
Session = sessionmaker(bind=engine) 
session = Session()

Base = declarative_base()


# class Pessoa:
#     def __init__(self, nome, cpf, telefone, email, endereco, data_nascimento):
#         self.nome = nome
#         self.cpf = cpf
#         self.telefone = telefone
#         self.email = email
#         self.endereco = endereco
#         self.data_nascimento = data_nascimento

# class Funcionario(Pessoa):
#     def __init__(self, nome, cpf, telefone, email, senha, endereco, data_nascimento, cargo, salario, id_funcionario=None):
#         super().__init__(nome, cpf, telefone, email, endereco, data_nascimento)
#         self.cargo = cargo
#         self.salario = salario
#         self.senha = senha
#         self.id_funcionario = id_funcionario

# class Cliente(Pessoa):
#     def __init__(self, nome, cpf, telefone, email, endereco, data_nascimento,total_divida, id_venda=None, id_cliente=None):
#         super().__init__(nome, cpf, telefone, email, endereco, data_nascimento)
#         self.id_cliente = id_cliente
#         self.total_divida = total_divida
#         self.id_venda = id_venda

# class Produto:
#     def __init__(self, nome ,descricao, preco,categoria, quantidade, id_produto=None):
#         self.id_produto = id_produto
#         self.nome = nome
#         self.descricao = descricao
#         self.preco = preco
#         self.categoria = categoria
#         self.quantidade = quantidade

# class Fornecedor:
#     def __init__(self, nome, cnpj, telefone, email, endereco, id_fornecedor=None):
#         self.id_fornecedor = id_fornecedor
#         self.nome = nome
#         self.cnpj = cnpj
#         self.telefone = telefone
#         self.email = email
#         self.endereco = endereco

# class Venda:
#     def __init__(self, id_funcionario, id_produtos, id_caixa, valor_total, forma_pagamento, id_venda=None, data_venda=None, id_pagamento=None):
#         self.id_funcionario = id_funcionario
#         self.id_produtos = id_produtos 
#         self.id_caixa = id_caixa
#         self.valor_total = valor_total
#         self.forma_pagamento = forma_pagamento
#         self.data_venda = data_venda
#         self.id_venda = id_venda
#         self.id_pagamento = id_pagamento

# class Caixa:
#     def __init__(self, id_caixa, id_funcionario, data_abertura, data_fechamento):
#         self.id_caixa = id_caixa
#         self.id_funcionario = id_funcionario
#         self.data_abertura = data_abertura
#         self.data_fechamento = data_fechamento



class Pessoa(Base):
    __tablename__ = 'pessoas'
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cpf = Column(String(14), unique=True, nullable=False)
    telefone = Column(String(20))
    email = Column(String(100))
    endereco = Column(Text)
    data_nascimento = Column(Date)

class Funcionario(Base):
    __tablename__ = 'funcionarios'
    
    id_funcionario = Column(Integer, primary_key=True, autoincrement=True)
    id_pessoa = Column(Integer, ForeignKey('pessoas.id'), nullable=False)
    cargo = Column(String(50), nullable=False)
    salario = Column(Float, nullable=False)
    senha = Column(String(255), nullable=False)
    
    pessoa = relationship("Pessoa")
    caixas = relationship("Caixa", back_populates="funcionario")
    vendas = relationship("Venda", back_populates="funcionario")

class Cliente(Base):
    __tablename__ = 'clientes'
    
    id_cliente = Column(Integer, primary_key=True)
    id_pessoa = Column(Integer, ForeignKey('pessoas.id'), nullable=False)
    total_divida = Column(Float, default=0.0)
    id_venda = Column(Integer, nullable=True)
    
    pessoa = relationship("Pessoa")
    vendas = relationship("Venda", back_populates="cliente", foreign_keys="Venda.id_cliente")

    def __init__(self, nome, cpf, telefone, email, endereco, data_nascimento,total_divida, id_venda=None, id_cliente=None):
        self.id_cliente = id_cliente
        self.total_divida = total_divida
        self.id_venda = id_venda
        self.pessoa = Pessoa(nome=nome, cpf=cpf, telefone=telefone, email=email, endereco=endereco, data_nascimento=data_nascimento)
class Produto(Base):
    __tablename__ = 'produtos'
    
    id_produto = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    descricao = Column(Text)
    preco = Column(Float, nullable=False)
    categoria = Column(String(50))
    quantidade = Column(Integer, nullable=False, default=0)

class Fornecedor(Base):
    __tablename__ = 'fornecedores'
    
    id_fornecedor = Column(Integer, primary_key=True, autoincrement=True)
    nome = Column(String(100), nullable=False)
    cnpj = Column(String(18), unique=True, nullable=False)
    telefone = Column(String(20))
    email = Column(String(100))
    endereco = Column(Text)

class Venda(Base):
    __tablename__ = 'vendas'
    
    id_venda = Column(Integer, primary_key=True)
    id_funcionario = Column(Integer, ForeignKey('funcionarios.id_funcionario'), nullable=False)
    id_caixa = Column(Integer, ForeignKey('caixas.id_caixa'), nullable=False)
    id_cliente = Column(Integer, ForeignKey('clientes.id_cliente'), nullable=True)
    valor_total = Column(Float, nullable=False)
    forma_pagamento = Column(String(50), nullable=False)
    data_venda = Column(DateTime, default=datetime.utcnow)
    id_pagamento = Column(Integer, nullable=True)
    
    funcionario = relationship("Funcionario", back_populates="vendas")
    caixa = relationship("Caixa", back_populates="vendas")
    cliente = relationship("Cliente", back_populates="vendas", foreign_keys=[id_cliente])

class Caixa(Base):
    __tablename__ = 'caixas'
    
    id_caixa = Column(Integer, primary_key=True, autoincrement=True)
    id_funcionario = Column(Integer, ForeignKey('funcionarios.id_funcionario'), nullable=False)
    data_abertura = Column(DateTime, nullable=False, default=datetime.utcnow)
    data_fechamento = Column(DateTime, nullable=True)
    
    funcionario = relationship("Funcionario", back_populates="caixas")
    vendas = relationship("Venda", back_populates="caixa")

Base.metadata.create_all(engine)
