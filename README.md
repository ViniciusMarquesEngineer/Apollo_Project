# 🚀 Apollo Logística — Sistema Completo

Sistema de gestão de estoque com backend Python (Flask) + banco de dados SQLite + frontend integrado.

---

## 📁 Estrutura do Projeto

```
apollo-full/
├── app.py                  ← Servidor Flask (backend principal)
├── setup.py                ← Script de instalação automática
├── requirements.txt        ← Dependências Python
├── apollo.db               ← Banco de dados SQLite (criado ao iniciar)
├── templates/
│   ├── apollo-landing.html    ← Página inicial / cadastro / login
│   ├── apollo-dashboard.html  ← Dashboard do funcionário
│   └── apollo-admin.html      ← Painel do administrador
└── static/                 ← Arquivos estáticos (CSS/JS extras, se necessário)
```

---

## ⚙️ Como Rodar (Primeira Vez)

### Pré-requisitos
- Python 3.8 ou superior instalado
- Pip instalado

### Passo a Passo

**1. Instale as dependências:**
```bash
pip install -r requirements.txt
```

Ou rode o setup automático:
```bash
python setup.py
```

**2. Inicie o servidor:**
```bash
python app.py
```

**3. Acesse no navegador:**
```
http://localhost:5000
```

> **Recomendamos o Google Chrome** para melhor compatibilidade com a câmera QR Code.

---

## 🔑 Como Usar

### Criando a primeira conta
1. Acesse `http://localhost:5000`
2. Preencha o formulário de **Cadastro**
3. Escolha o perfil:
   - 👷 **Funcionário** → acessa o Dashboard de movimentações
   - 🛡️ **Administrador** → acessa o Painel Admin com relatórios Excel
4. Digite o código de verificação enviado ao e-mail
5. Você será redirecionado automaticamente para o painel correto

### Funcionário (`/dashboard`)
- Registrar **entradas** e **saídas** de produtos
- Usar a **câmera** (botão azul no canto inferior direito) para ler QR Codes
- Visualizar movimentações e alertas de estoque baixo
- Cada movimentação gera automaticamente um **QR Code PNG** para download

### Administrador (`/admin`)
- Tudo que o funcionário faz, mais:
- **Aba Alertas** → ver produtos críticos e cadastrar fornecedores
- **Aba Produtos** → lista completa com edição de fornecedores
- **Aba Usuários** → ver todos os cadastros do sistema
- **Aba Relatórios** → gerar planilha **Excel real (.xlsx)** com:
  - Movimentações (com filtro de período)
  - Estoque atual
  - Produtos críticos
  - Usuários cadastrados

---

## 📷 Câmera / QR Code

O sistema usa a câmera do navegador (sem instalar nada extra):

1. Clique no botão de câmera 📷 no canto inferior direito
2. Autorize o acesso à câmera quando o browser pedir
3. Aponte para o QR Code do produto
4. O sistema detecta automaticamente e:
   - Mostra os dados do produto (nome, código, categoria, estoque atual)
   - Oferece os botões **Registrar Entrada** ou **Registrar Saída**
   - Ao clicar, vai direto ao formulário com os campos preenchidos

---

## 📊 Relatório Excel

Gerado pelo servidor Python usando **openpyxl** com:
- Formatação profissional (cores, bordas, larguras de coluna ajustadas)
- Aba de Movimentações com histórico completo
- Aba de Estoque com status (OK ✅ / Baixo ⚠️ / Zerado 🔴)
- Aba de Alertas com produtos críticos
- Aba de Usuários com perfis

> O botão de gerar Excel **só aparece no painel Admin**.

---

## 🗄️ Banco de Dados

O banco `apollo.db` (SQLite) é criado automaticamente ao rodar `python app.py`.  
Não precisa instalar nenhum banco de dados externo.

**Tabelas:**
| Tabela | Descrição |
|--------|-----------|
| `usuarios` | Contas cadastradas com hash de senha |
| `codigos_verificacao` | Códigos temporários de e-mail |
| `estoque` | Produtos e quantidades atuais |
| `movimentacoes` | Histórico de entradas e saídas |

---

## 🌐 Rotas da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET  | `/` | Página inicial |
| GET  | `/dashboard` | Dashboard funcionário |
| GET  | `/admin` | Painel admin |
| POST | `/api/auth/cadastro/solicitar` | Etapa 1 do cadastro |
| POST | `/api/auth/cadastro/verificar` | Verificar código e criar conta |
| POST | `/api/auth/cadastro/reenviar` | Reenviar código |
| POST | `/api/auth/login` | Login |
| POST | `/api/auth/logout` | Logout |
| GET  | `/api/auth/sessao` | Verificar sessão ativa |
| GET  | `/api/resumo` | Cards do dashboard |
| POST | `/api/movimentacao` | Registrar entrada/saída |
| GET  | `/api/movimentacoes` | Listar movimentações |
| GET  | `/api/estoque` | Listar todos os produtos |
| GET  | `/api/estoque/<codigo>` | Buscar produto por código |
| PUT  | `/api/estoque/fornecedor` | Atualizar fornecedor (admin) |
| GET  | `/api/alertas` | Produtos com estoque baixo |
| GET  | `/api/usuarios` | Listar usuários (admin) |
| GET  | `/api/relatorio/excel` | Gerar planilha Excel (admin) |
| POST | `/api/qrcode/gerar` | Gerar QR Code PNG |

---

## 📧 E-mail de Verificação (EmailJS)

O sistema usa **EmailJS** para enviar o código de verificação no cadastro.  
As chaves já estão configuradas no `apollo-landing.html`.

Se o e-mail não chegar, o código também aparece no **terminal do servidor** (linha `[Apollo] Código de verificação para ...`), útil para testes.

---

## 👥 Equipe

| Nome | Função |
|------|--------|
| José Reis | Front-end |
| Vinicius Marques | Full-stack |
| Carla Rio | Back-end / Banco de dados |
| Lauro Aguiar | Back-end / excel|
| Pedro Antônio | Back-end / Visão Computacional |

---

## 🛠️ Tecnologias

- **Backend:** Python 3 + Flask
- **Banco de dados:** SQLite (via módulo `sqlite3`)
- **Planilha Excel:** openpyxl
- **QR Code:** qrcode + Pillow (servidor) / jsQR (browser)
- **Autenticação:** Werkzeug password hashing + Flask sessions
- **E-mail:** EmailJS (verificação de cadastro)
- **Frontend:** HTML5 + CSS3 + JavaScript puro (sem frameworks)

---

*© 2026 Apollo Logística — PIEC-1*
