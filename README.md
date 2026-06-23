# 🚀 Apollo Logística — Sistema Completo

Sistema de gestão de estoque com backend Python (Flask) + banco de dados SQLite + frontend integrado.

---

## 📁 Estrutura do Projeto

```
apollo-full/
├── app.py                  ← Servidor Flask (backend principal)
├── setup.py                ← Script de instalação automática
├── promover_admin.py       ← Script para promover usuário a administrador
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

> **Recomendamos o Google Chrome ou Microsoft Edge** para melhor compatibilidade com a câmera e leitura de QR Code.

---

## 🔑 Como Usar

### Criando a primeira conta
1. Acesse `http://localhost:5000`
2. Preencha o formulário de **Cadastro** (usuário, e-mail e senha)
3. A senha deve conter: mínimo 8 caracteres, 1 letra maiúscula e 1 caractere especial
4. Digite o código de 6 dígitos enviado ao e-mail para verificar a conta
5. Você será redirecionado automaticamente para o painel correto

### Promovendo um Administrador
Contas novas são sempre criadas como **Funcionário**. Para promover a Administrador, rode o script no terminal do servidor:
```bash
python promover_admin.py
```
O script lista os usuários cadastrados e solicita confirmação antes de promover.

### Funcionário (`/dashboard`)
- Registrar **entradas** e **saídas** de produtos com código, nome, categoria, quantidade, data, estoque mínimo e dados do fornecedor
- Usar a **câmera** (botão azul no canto inferior direito) para ler QR Codes e preencher o formulário automaticamente
- Gerar **QR Code PNG** de etiqueta para cada produto — ao escanear, todos os campos são preenchidos automaticamente
- Visualizar movimentações do dia e alertas de estoque baixo

### Administrador (`/admin`)
- Tudo que o funcionário faz, mais:
- **Aba Alertas** → ver produtos críticos e cadastrar fornecedores
- **Aba Produtos** → lista completa com edição de fornecedores
- **Aba Usuários** → ver todos os cadastros do sistema
- **Aba Relatórios** → gerar relatório **.xlsx** com nome automático baseado no período selecionado, além de atalhos rápidos para relatórios **Semanal**, **Mensal**, **Trimestral** e **Anual**

---

## 📷 Câmera / QR Code

A leitura de QR Code é feita diretamente no navegador do usuário, sem nenhuma dependência extra no servidor:

1. Clique no botão de câmera 📷 no canto inferior direito do dashboard
2. Autorize o acesso à câmera quando o browser solicitar
3. Aponte para o QR Code do produto
4. O sistema detecta automaticamente e preenche todos os campos do formulário:
   - Código, nome, categoria, estoque mínimo
   - Fornecedor, e-mail e telefone do fornecedor
5. Informe apenas a **quantidade** e clique em Registrar Entrada ou Saída

> A câmera traseira é priorizada em dispositivos móveis para facilitar a leitura.

### Gerando QR Codes
- Preencha o formulário com os dados do produto e clique em **Gerar QR Code**
- O QR Code é gerado pelo servidor (qrcode + Pillow) e baixado como PNG
- Cole a etiqueta na embalagem — ao escanear futuramente, todos os campos são preenchidos automaticamente

---

## 🔐 Segurança de Senha

O sistema valida a senha em duas camadas:

- **Frontend:** indicador visual de força com checklist em tempo real (barras coloridas)
- **Backend:** rejeita senhas com menos de 8 caracteres, sem letra maiúscula ou sem caractere especial

---

## 📊 Relatórios

Gerados pelo servidor Python usando **openpyxl** com formatação profissional:
- Aba de Movimentações com histórico completo e coluna de fornecedor
- Aba de Estoque com status (OK ✅ / Baixo ⚠️ / Zerado 🔴)
- Aba de Alertas com produtos críticos
- Aba de Usuários com perfis

**Nome do arquivo gerado automaticamente:** `Relatório DD/MM - DD/MM.xlsx`

**Atalhos rápidos disponíveis:** Semanal · Mensal · Trimestral · Anual

---

## 🗄️ Banco de Dados

O banco `apollo.db` (SQLite) é criado automaticamente ao iniciar o servidor.  
Não é necessário instalar nenhum banco de dados externo.

**Tabelas:**
| Tabela | Descrição |
|--------|-----------|
| `usuarios` | Contas cadastradas com hash de senha |
| `codigos_verificacao` | Códigos temporários de e-mail (expiram em 10 min) |
| `estoque` | Produtos, quantidades e dados de fornecedor |
| `movimentacoes` | Histórico de entradas e saídas com fornecedor |

---

## 🌐 Rotas da API

| Método | Rota | Descrição |
|--------|------|-----------|
| GET  | `/` | Página inicial |
| GET  | `/dashboard` | Dashboard funcionário |
| GET  | `/admin` | Painel admin |
| POST | `/api/auth/cadastro/solicitar` | Etapa 1 do cadastro |
| POST | `/api/auth/cadastro/verificar` | Verificar código e criar conta |
| POST | `/api/auth/cadastro/reenviar` | Reenviar código de verificação |
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
| GET  | `/api/relatorio/excel` | Gerar relatório Excel (admin) |
| POST | `/api/qrcode/gerar` | Gerar QR Code PNG (servidor) |

---

## 📧 E-mail de Verificação (EmailJS)

O sistema usa **EmailJS** para enviar o código de verificação no cadastro.  
As chaves já estão configuradas no `apollo-landing.html`.

Se o e-mail não chegar, o código também aparece no **terminal do servidor** (linha `[Apollo] Código de verificação para ...`), útil para testes locais.

---

## 👥 Equipe

| Nome | Função |
|------|--------|
| José Reis | Front-end |
| Vinicius Marques | Full-stack |
| Carla Rios | Back-end / Excel |
| Lauro Aguiar | Back-end / Banco de dados |
| Pedro Antônio | Visão Computacional |

---

## 🛠️ Tecnologias

- **Backend:** Python 3 + Flask + Gunicorn
- **Banco de dados:** SQLite (via módulo `sqlite3`)
- **Relatório Excel:** openpyxl
- **QR Code geração:** qrcode + Pillow
- **QR Code leitura:** jsQR + BarcodeDetector API (browser)
- **Autenticação:** Werkzeug password hashing + Flask sessions
- **E-mail:** EmailJS (verificação de cadastro)
- **Frontend:** HTML5 + CSS3 + JavaScript puro (sem frameworks)

---

*© 2026 Apollo Logística — PIEC-1*
