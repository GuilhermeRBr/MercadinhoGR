# Mercadinho GR

Bem-vindo ao **Mercadinho Gr**, um sistema de gerenciamento de mercado simples, funcional e bem estruturado!
Este projeto esta sendo desenvolvido com foco em organização, boas práticas e validação completa de dados, ideal para uso acadêmico ou ate mesmo em caixas pequenos de mercearias e pequenos mercados.

---

## 📌 Sobre o Projeto

O **Mercadinho GR** simula a estrutura básica de um sistema de mercado, onde é possível:

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

1. Clone este repositório:
   ```bash
    git clone https://github.com/GuilhermeRBr/MercadinhoGR
    cd MercadinhoGR
2. Crie e ative um ambiente virtual:
    ```bash
    python -m venv venv
    source venv/bin/activate   # Linux/Mac
    venv\Scripts\activate      # Windows

3. Instale as dependêndias:
    ```bash
    pip install -r requirements.txt

4. Configure as variáveis de ambiente no arquivo **.env**:
    ```bash
    DATABASE_URL=postgresql+psycopg2://usuario:senha@localhost:5432/mercadinhGR

5. Execute o aplicativo:
    ```bash
    python main.py

