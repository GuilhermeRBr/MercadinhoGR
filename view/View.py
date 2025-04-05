import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from controller.Controller import PessoaController

nome = "João"
cpf = "12345678901" 
telefone = "11987654321"
email = "joao2@example.com"
endereco = "Rua A, 123"


PessoaController.cadastrar_pessoa(nome, cpf, telefone, email, endereco)