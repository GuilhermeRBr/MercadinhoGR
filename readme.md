# Mercadinho GR

Bem-vindo ao **Mercadinho Gr**, um sistema de gerenciamento de mercado simples, funcional e bem estruturado!
Este projeto esta sendo desenvolvido com foco em organização, boas práticas e validação completa de dados, ideal para uso acadêmico ou ate mesmo em caixas pequenos de mercearias e pequenos mercados.

# -- AINDA EM DESENVOLVIMENTO --

## Como Rodar o Projeto

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
    uvicorn server.main app --reload #debug on
    uvicorn server.main app #debug off


