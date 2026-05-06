# 📊 CND Tracker (Gestor de Vencimentos de CND)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Status](https://img.shields.io/badge/Status-Operacional-success?style=for-the-badge)

Gestor automatizado de vencimentos de Certidões Negativas de Débitos (CND).

## Problema

No setor contábil, perder o prazo de uma CND pode causar a exclusão de clientes
do Simples Nacional. O controle manual em planilhas é ineficiente e propenso a erros.

## Solução

Automação em Python que lê uma base de clientes em Excel, classifica os vencimentos
por nível de risco e envia alertas automáticos por e-mail para a equipe contábil.

## Stack

- Python 3.13
- pandas, openpyxl — leitura e escrita de planilhas
- smtplib, email — envio de notificações (nativo Python)
- python-dotenv — gerenciamento seguro de credenciais

## Estrutura do Projeto

```
cnd-tracker/
├── monitor_cnd.py          # Ponto de entrada — orquestra os serviços
├── config.py               # Configurações centralizadas (thresholds, caminhos)
├── services/
│   ├── data_service.py     # I/O de dados (Excel)
│   ├── rules_service.py    # Regras de negócio (cálculo de status)
│   └── email_service.py    # Envio de notificações por e-mail
├── .env.example            # Modelo de variáveis de ambiente
├── .gitignore
└── requirements.txt
```

## Regras de Negócio

| Status | Critério |
|---|---|
| 🔴 URGENTE | CND vencida (dias restantes < 0) |
| 🟡 ALERTA | Vence em até 15 dias |
| 🟢 OK | Vence em mais de 15 dias |

## Como Executar

### 1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/cnd-tracker.git
cd cnd-tracker
```

### 2. Instale as dependências
```bash
pip install -r requirements.txt
```

### 3. Configure as variáveis de ambiente
```bash
cp .env.example .env
# Edite o .env com suas credenciais
```

### 4. Execute
```bash
python monitor_cnd.py
```

## Configuração do .env

Crie um arquivo `.env` na raiz do projeto baseado no `.env.example`:

```env
EMAIL_REMETENTE=seu_email@gmail.com
EMAIL_APP_PASSWORD=sua_app_password_sem_espacos
EMAIL_DESTINATARIO=destinatario@email.com
```

> O Gmail exige uma **App Password** (não sua senha normal).
> Gere em: https://myaccount.google.com/apppasswords

## Roadmap

- [x] **Etapa A** — Notificações automáticas por e-mail (smtplib)
- [ ] **Etapa B** — Migração para banco de dados relacional (SQLite → PostgreSQL)
- [ ] **Etapa C** — Dashboard / interface gráfica de acompanhamento

