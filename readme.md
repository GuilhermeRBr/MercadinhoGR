# 🛒 Mercadinho GR

Bem-vindo ao **Mercadinho Gr**, um sistema de gerenciamento de mercado simples, funcional e bem estruturado!  
Este projeto foi desenvolvido com foco em organização, boas práticas e validação completa de dados, ideal para uso acadêmico ou para quem deseja entender na prática como funciona a arquitetura **MVC** com persistência em **arquivos JSON**.

---

## 📌 Sobre o Projeto

O **Mercadinho Gr** simula a estrutura básica de um sistema de mercado, onde é possível:

- Cadastrar, editar e remover **produtos**, **categorias**, **clientes**, **fornecedores** e **funcionários**.
- Registrar vendas e controlar o **caixa**.
- Gerar **relatórios completos**, como:
  - Vendas gerais
  - Vendas por data
  - Produtos mais vendidos
  - Vendas por meio de pagamento
  - Vendas por funcionário

---

## 🧱 Arquitetura Utilizada

O projeto segue o padrão de arquitetura **MVC (Model - View - Controller)**, que garante:

- Separação de responsabilidades
- Código mais limpo e modular
- Facilidade para manutenção e expansão

A persistência dos dados é feita utilizando **arquivos JSON**, simulando um banco de dados leve e acessível.

---

## ✅ Validações e Segurança

Todos os campos do sistema passam por **verificações e validações rigorosas**, como:

- Verificação de campos obrigatórios
- Tipos de dados corretos (números, textos, datas, etc.)
- Impedimento de duplicidades e inconsistências
- Mensagens de erro claras e objetivas

---

## 💻 Tecnologias Utilizadas

- **Python**
- Estrutura **MVC**
- Armazenamento com **JSON**

---

## 🚀 Como Rodar o Projeto

```bash

git clone https://github.com/GuilhermeRBr/MercadinhoGR

# Acesse a pasta do projeto
cd mercadinhoGR

# Execute o sistema
python view/View.py
