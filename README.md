# 📊 CND Tracker (Gestor de Vencimentos de CND)

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)
![Excel](https://img.shields.io/badge/Microsoft_Excel-217346?style=for-the-badge&logo=microsoft-excel&logoColor=white)
![Status](https://img.shields.io/badge/Status-Operacional-success?style=for-the-badge)

## 🎯 O Problema
No ambiente contábil e financeiro, a perda do prazo de validade de uma Certidão Negativa de Débitos (CND) pode resultar em desenquadramentos tributários graves (como a exclusão do Simples Nacional) e retenções de pagamentos. O controle manual em planilhas exige muito tempo e é suscetível a falhas humanas.

## 💡 A Solução
O **CND Tracker** é uma automação em Python desenvolvida para mitigar o risco de conformidade fiscal. O script ingere a base de clientes a partir de arquivos `.xlsx`, processa as datas de vencimento em frações de segundo, alerta via terminal quais documentos estão em risco e escreve o status atualizado de volta na planilha de forma autônoma.

---

## ⚙️ Funcionalidades
- **Leitura Otimizada:** Ingestão de dados via biblioteca `pandas`.
- **Análise Lógica:** Cálculo em tempo real da diferença entre a data atual e o vencimento do documento.
- **Alertas Dinâmicos:** Classificação de status em três níveis:
  - 🔴 `URGENTE` (Vencido)
  - 🟡 `ALERTA` (Vence em menos de 15 dias)
  - 🟢 `OK` (Regular)
- **Escrita Automatizada:** Atualização do arquivo Excel com os novos status sem intervenção manual.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
Certifique-se de ter o Python instalado e o instalador de pacotes `pip` disponível.

1. Clone o repositório:
```bash
git clone [https://github.com/SEU-USUARIO/CND-Tracker.git](https://github.com/SEU-USUARIO/CND-Tracker.git)
cd CND-Tracker
```

2. Instale as dependências necessárias:
```bash
pip install pandas openpyxl
```
3. Configure sua base de dados:
Crie um arquivo chamado `clientes_cnd.xlsx` na raiz do projeto com as seguintes colunas obrigatórias na linha 1:

- Nome

- CNPJ

- Vencimento (formato data)


4. Execute a automação:
```bash
python monitor_cnd.py
```



## 📂 Estrutura do Repositório
📦 CND-Tracker
 ┣ 📜 monitor_cnd.py        # Script principal com a lógica de automação
 ┣ 📜 .gitignore            # Bloqueio de segurança para dados sensíveis (planilhas)
 ┗ 📜 README.md             # Documentação do projeto
 
_Nota: O arquivo clientes_cnd.xlsx não é versionado por motivos de LGPD e segurança da informação._



## 📈 Backlog & Próximos Passos (Roadmap)
Como um projeto em evolução, as seguintes melhorias estão mapeadas para futuras iterações:

    [ ] Implementação de notificações automáticas por E-mail usando smtplib.

    [ ] Transição da fonte de dados de .xlsx para um banco de dados relacional.

    [ ] Criação de um dashboard visual para acompanhamento dos status.
