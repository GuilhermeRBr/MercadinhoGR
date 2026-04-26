# 🚀 Mercadinho GR - Plano de Desenvolvimento Fullstack

## ✅ PROGRESSO ATUAL

### STEP 1 - Setup do Projeto Frontend ✓ CONCLUÍDO
- [x] Next.js 14 configurado com TypeScript
- [x] Tailwind CSS configurado
- [x] Estrutura de pastas organizada
- [x] Layout base (Sidebar + Header) implementado
- [x] Páginas base criadas
- [x] Documentação completa

**📄 Ver detalhes:** `docs/STEP1_SUMMARY.md`

### STEP 2 - Integração Base com API ✓ CONCLUÍDO
- [x] Axios configurado com interceptors
- [x] React Query Provider configurado
- [x] Camada de serviços (ProductService)
- [x] Custom hooks (useProducts)
- [x] Tipos TypeScript criados
- [x] Utilitários (formatters, errorHandler, constants)
- [x] Página de teste funcionando
- [x] Integração testada com backend

**📄 Ver detalhes:** `docs/STEP2_SUMMARY.md`

### STEP 3 - Autenticação ✓ CONCLUÍDO
- [x] Tela de login implementada
- [x] Integração com /api/auth/login
- [x] JWT armazenado no localStorage
- [x] Proteção de rotas (ProtectedRoute)
- [x] Refresh token automático
- [x] Logout funcional
- [x] AuthContext global
- [x] Persistência de sessão

**📄 Ver detalhes:** `docs/STEP3_SUMMARY.md`

### STEP 4 - Produtos (CRUD) ✓ CONCLUÍDO
- [x] Listagem de produtos com tabela
- [x] Criação de produtos
- [x] Edição de produtos
- [x] Busca por nome e código de barras
- [x] Filtros por status (ativo/inativo)
- [x] Soft delete (ativar/desativar)
- [x] Validação de formulários
- [x] Componentes reutilizáveis

**📄 Ver detalhes:** `docs/STEP4_SUMMARY.md`

### STEP 5 - Usuários ✓ CONCLUÍDO
- [x] Listagem de usuários
- [x] Cadastro de funcionários
- [x] Soft delete (ativar/desativar)
- [x] Diferenciação de roles (Dono/Funcionário)
- [x] Validação de senha e confirmação
- [x] Proteção contra auto-desativação
- [x] Indicador visual de usuário atual
- [x] Componentes reutilizáveis

**📄 Ver detalhes:** `docs/STEP5_SUMMARY.md`

### STEP 6 - Caixa (Vendas) ✓ CONCLUÍDO
- [x] Tela de PDV (Ponto de Venda)
- [x] Listagem de produtos disponíveis
- [x] Busca de produtos em tempo real
- [x] Adicionar produtos ao carrinho
- [x] Controle de quantidade (+/-)
- [x] Remover itens do carrinho
- [x] Cálculo automático de total
- [x] Verificação de estoque
- [x] Finalizar venda
- [x] Histórico de vendas
- [x] Cancelamento de vendas

**📄 Ver detalhes:** `docs/STEP6_SUMMARY.md`

### STEP 7 - Pagamentos ✓ CONCLUÍDO
- [x] Backend: Módulo de pagamentos completo
- [x] Frontend: Tela de seleção de pagamento
- [x] Métodos: PIX, Crédito, Débito, Dinheiro, Outro
- [x] Interface visual com ícones coloridos
- [x] Integração com vendas
- [x] Registro de pagamento no banco
- [x] Fluxo completo: Carrinho → Pagamento → Finalização
- [x] Validação de método selecionado

**📄 Ver detalhes:** `docs/STEP7_SUMMARY.md`

### STEP 8 - Dashboard ✓ CONCLUÍDO
- [x] Cards principais com estatísticas
- [x] Receita total e vendas hoje
- [x] Contadores de produtos e usuários
- [x] Alertas de estoque (sem estoque, estoque baixo)
- [x] Resumo de vendas (concluídas/canceladas)
- [x] Top produtos com indicadores visuais
- [x] Cálculos otimizados com useMemo
- [x] Loading states e design responsivo

**📄 Ver detalhes:** `docs/STEP8_SUMMARY.md`

---

## 🎉 PROJETO COMPLETO!

Todos os 8 steps foram concluídos com sucesso. O sistema Mercadinho GR está pronto para uso em produção!

---

Crie uma aplicação fullstack moderna, escalável e bem estruturada, seguindo boas práticas de arquitetura, organização e código limpo.

📌 Contexto do Projeto
Já existe um backend quase completo desenvolvido com:
FastAPI
Banco de dados PostgreSQL
Arquitetura modularizada
Validações implementadas
API REST funcional já criada
🚨 IMPORTANTE
As seguintes APIs já estão implementadas no backend e DEVEM ser consumidas no frontend:
📦 Products
GET /api/products/
POST /api/products/
GET /api/products/search
GET /api/products/{id}
PATCH /api/products/{id}
💰 Sales
GET /api/sales/
POST /api/sales/
GET /api/sales/{id}
PATCH /api/sales/{id} (cancelamento)
👥 Users
POST /api/users/register
GET /api/users/
GET /api/users/{id}
PATCH /api/users/{id}
🔐 Auth
POST /api/auth/login
POST /api/auth/refresh-token
POST /api/auth/logout

⚠️ Regra CRÍTICA de Negócio
❌ NÃO existe remoção física (DELETE)
✔️ Implementar soft delete:
Usuários → campo is_active
Vendas → campo is_active
Produtos → opcional (recomendado)
Regras:
"Remover" = desativar (is_active = false)
Pode reativar (is_active = true)
Nenhum dado deve ser apagado do banco

🎯 Objetivo
1. FRONTEND
Desenvolver frontend completo utilizando:
Next.js (App Router)
TypeScript
Tailwind CSS

🧩 Funcionalidades do Front
🔐 Autenticação
Login com JWT
Refresh token
Proteção de rotas
Diferenciar dono e funcionário

📦 Produtos
Listar
Criar
Editar
Buscar
Ativar/Inativar (soft delete)

👥 Usuários
Cadastro de funcionários
Listagem
Edição
Ativar/Inativar

💰 Caixa (PDV)
Adicionar produtos na venda
Calcular total automaticamente
Finalizar venda

💳 Pagamentos
Escolher tipo:
Pix
Cartão crédito
Cartão débito
Dinheiro
Outros
Permitir múltiplos pagamentos na mesma venda
UI simples e rápida (foco em caixa)

🧱 Arquitetura Frontend
Separar por domínio:
app/
 (auth)/
 dashboard/
 produtos/
 usuarios/
 vendas/
 caixa/

components/
services/
hooks/
contexts/
types/
utils/

🔌 Integração com Backend
Criar camada de serviços (API)
Separar lógica da UI
Tratar erros corretamente
Utilizar:
Axios
React Query

🎨 UI
Interface moderna e responsiva
Componentes reutilizáveis
Pode usar:
Shadcn UI

⚙️ Boas práticas (FRONT)
Clean Code
Tipagem forte
Hooks customizados
Sem lógica de negócio em componentes
Separação clara de responsabilidades

🧠 BACKEND (COMPLEMENTAÇÃO)
Criar e organizar código dentro da pasta:
/server
Seguindo arquitetura modular:
/server
 /modules
   /auth
   /users
   /products
   /sales
   /payments
 /schemas
 /models
 /services
 /repositories
 /core
 /config

💳 Módulo de Pagamentos (NOVO)
Implementar:
Registro de pagamento
Relacionamento com venda
Tipos:
Pix
Crédito
Débito
Dinheiro
Outros
Campos:
id
sale_id
type
amount
created_at

🧠 Regras Backend
Usar FastAPI com boas práticas
Separar:
Controller (routes)
Service (regras de negócio)
Repository (acesso ao banco)
Validação com Pydantic
Código modularizado
Mensagens de erro claras
Tratamento global de exceções

🔒 Segurança
JWT bem estruturado
Refresh token funcional
Proteção de rotas
Validação de permissões

🚀 Extras
Dashboard com:
Total de vendas
Produtos mais vendidos
Atualização automática de estoque
Feedback visual (loading, erro, sucesso)

📌 Resultado Esperado
Frontend completo e funcional
Backend com módulo de pagamentos implementado
Integração total com APIs existentes
Código limpo, modular e escalável
Pronto para produção
ura, organização e código limpo.

📌 Contexto do Projeto
Já existe um backend quase completo desenvolvido com:
FastAPI
Banco de dados PostgreSQL
Arquitetura modularizada
Validações implementadas
API REST funcional já criada
🚨 IMPORTANTE
As seguintes APIs já estão implementadas no backend e DEVEM ser consumidas no frontend:
📦 Products
GET /api/products/
POST /api/products/
GET /api/products/search
GET /api/products/{id}
PATCH /api/products/{id}
💰 Sales
GET /api/sales/
POST /api/sales/
GET /api/sales/{id}
PATCH /api/sales/{id} (cancelamento)
👥 Users
POST /api/users/register
GET /api/users/
GET /api/users/{id}
PATCH /api/users/{id}
🔐 Auth
POST /api/auth/login
POST /api/auth/refresh-token
POST /api/auth/logout

⚠️ Regra CRÍTICA de Negócio
❌ NÃO existe remoção física (DELETE)
✔️ Implementar soft delete:
Usuários → campo is_active
Vendas → campo is_active
Produtos → opcional (recomendado)
Regras:
"Remover" = desativar (is_active = false)
Pode reativar (is_active = true)
Nenhum dado deve ser apagado do banco

🎯 Objetivo
1. FRONTEND
Desenvolver frontend completo utilizando:
Next.js (App Router)
TypeScript
Tailwind CSS

🧩 Funcionalidades do Front
🔐 Autenticação
Login com JWT
Refresh token
Proteção de rotas
Diferenciar dono e funcionário

📦 Produtos
Listar
Criar
Editar
Buscar
Ativar/Inativar (soft delete)

👥 Usuários
Cadastro de funcionários
Listagem
Edição
Ativar/Inativar

💰 Caixa (PDV)
Adicionar produtos na venda
Calcular total automaticamente
Finalizar venda

💳 Pagamentos
Escolher tipo:
Pix
Cartão crédito
Cartão débito
Dinheiro
Outros
Permitir múltiplos pagamentos na mesma venda
UI simples e rápida (foco em caixa)

🧱 Arquitetura Frontend
Separar por domínio:
app/
 (auth)/
 dashboard/
 produtos/
 usuarios/
 vendas/
 caixa/

components/
services/
hooks/
contexts/
types/
utils/

🔌 Integração com Backend
Criar camada de serviços (API)
Separar lógica da UI
Tratar erros corretamente
Utilizar:
Axios
React Query

🎨 UI
Interface moderna e responsiva
Componentes reutilizáveis
Pode usar:
Shadcn UI

⚙️ Boas práticas (FRONT)
Clean Code
Tipagem forte
Hooks customizados
Sem lógica de negócio em componentes
Separação clara de responsabilidades

🧠 BACKEND (COMPLEMENTAÇÃO)
Criar e organizar código dentro da pasta:
/server
Seguindo arquitetura modular:
/server
 /modules
   /auth
   /users
   /products
   /sales
   /payments
 /schemas
 /models
 /services
 /repositories
 /core
 /config

💳 Módulo de Pagamentos (NOVO)
Implementar:
Registro de pagamento
Relacionamento com venda
Tipos:
Pix
Crédito
Débito
Dinheiro
Outros
Campos:
id
sale_id
type
amount
created_at

🧠 Regras Backend
Usar FastAPI com boas práticas
Separar:
Controller (routes)
Service (regras de negócio)
Repository (acesso ao banco)
Validação com Pydantic
Código modularizado
Mensagens de erro claras
Tratamento global de exceções

🔒 Segurança
JWT bem estruturado
Refresh token funcional
Proteção de rotas
Validação de permissões

🚀 Extras
Dashboard com:
Total de vendas
Produtos mais vendidos
Atualização automática de estoque
Feedback visual (loading, erro, sucesso)

📌 Resultado Esperado
Frontend completo e funcional
Backend com módulo de pagamentos implementado
Integração total com APIs existentes
Código limpo, modular e escalável
Pronto para produção
flowchart TD

%% ================= FRONTEND =================
subgraph FRONTEND [Next.js Frontend]
    UI[UI - Pages & Components]
    AUTH_UI[Auth Pages]
    DASH[Dashboard]
    PROD[Produtos]
    USER[Usuários]
    SALES[Caixa / Vendas]

    UI --> AUTH_UI
    UI --> DASH
    UI --> PROD
    UI --> USER
    UI --> SALES

    HOOKS[Custom Hooks]
    SERVICES[API Services (Axios + React Query)]

    AUTH_UI --> HOOKS
    DASH --> HOOKS
    PROD --> HOOKS
    USER --> HOOKS
    SALES --> HOOKS

    HOOKS --> SERVICES
end

%% ================= BACKEND =================
subgraph BACKEND [FastAPI Backend]
    
    ROUTES[Routes / Controllers]
    SERVICES_B[Services Layer]
    REPO[Repositories]
    DB[(PostgreSQL)]

    ROUTES --> SERVICES_B
    SERVICES_B --> REPO
    REPO --> DB

end

%% ================= MODULES =================
subgraph MODULES [Backend Modules]

    AUTH[Auth Module]
    USERS[Users Module]
    PRODUCTS[Products Module]
    SALES_B[Sales Module]
    PAYMENTS[Payments Module]

    AUTH --> ROUTES
    USERS --> ROUTES
    PRODUCTS --> ROUTES
    SALES_B --> ROUTES
    PAYMENTS --> ROUTES

end

%% ================= AUTH FLOW =================
AUTH_UI -->|Login Request| SERVICES
SERVICES -->|POST /auth/login| ROUTES
ROUTES --> AUTH
AUTH --> SERVICES_B
SERVICES_B --> REPO
REPO --> DB
DB --> SERVICES_B
SERVICES_B -->|JWT Token| ROUTES
ROUTES --> SERVICES
SERVICES -->|Store Token| AUTH_UI

%% ================= PRODUCTS FLOW =================
PROD -->|CRUD Produtos| SERVICES
SERVICES -->|/api/products| ROUTES
ROUTES --> PRODUCTS
PRODUCTS --> SERVICES_B
SERVICES_B --> REPO
REPO --> DB

%% ================= USERS FLOW =================
USER -->|CRUD Usuários| SERVICES
SERVICES -->|/api/users| ROUTES
ROUTES --> USERS
USERS --> SERVICES_B
SERVICES_B --> REPO
REPO --> DB

%% ================= SALES FLOW =================
SALES -->|Criar Venda| SERVICES
SERVICES -->|POST /api/sales| ROUTES
ROUTES --> SALES_B
SALES_B --> SERVICES_B
SERVICES_B --> REPO
REPO --> DB

%% ================= PAYMENT FLOW =================
SALES -->|Selecionar Pagamento| SERVICES
SERVICES -->|POST /api/payments| ROUTES
ROUTES --> PAYMENTS
PAYMENTS --> SERVICES_B
SERVICES_B --> REPO
REPO --> DB

%% ================= SOFT DELETE =================
SERVICES_B -->|is_active = false| REPO
REPO --> DB

%% ================= SECURITY =================
SERVICES -->|JWT Token| ROUTES
ROUTES -->|Validate Token| AUTH
AUTH --> SERVICES_B

%% ================= STOCK UPDATE =================
SALES_B -->|Atualiza Estoque| PRODUCTS

%% ================= RESPONSE =================
DB --> REPO
REPO --> SERVICES_B
SERVICES_B --> ROUTES
ROUTES --> SERVICES
SERVICES --> UI

