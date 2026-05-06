import datetime

# Base de dados simulada (Na Fase 2, faremos isso ler do seu Excel)
clientes = [
    {
        "nome": "Cliente Jaboatão (Lucro Presumido)", 
        "cnpj": "12.345.678/0001-90", 
        "vencimento_cnd": "2026-05-10" # Data próxima ao vencimento
    },
    {
        "nome": "Clínica Saúde LTDA (Simples Nacional)", 
        "cnpj": "98.765.432/0001-10", 
        "vencimento_cnd": "2026-08-20"
    }
]

def verificar_vencimentos():
    hoje = datetime.date.today()
    alerta_dias = 15 # Configuração: Avisar com 15 dias de antecedência

    print("="*45)
    print("SISTEMA DE MONITORAMENTO DE CNDs - STATUS")
    print("="*45)

    for cliente in clientes:
        vencimento = datetime.datetime.strptime(cliente["vencimento_cnd"], "%Y-%m-%d").date()
        dias_restantes = (vencimento - hoje).days

        if dias_restantes < 0:
            print(f"[URGENTE] CNPJ: {cliente['cnpj']} | A CND de '{cliente['nome']}' VENCEU há {abs(dias_restantes)} dias!")
        elif dias_restantes <= alerta_dias:
            print(f"[ALERTA] CNPJ: {cliente['cnpj']} | A CND de '{cliente['nome']}' vence em {dias_restantes} dias.")
        else:
            print(f"[OK] CNPJ: {cliente['cnpj']} | A CND de '{cliente['nome']}' está regular ({dias_restantes} dias restantes).")
    print("="*45)

if __name__ == "__main__":
    verificar_vencimentos()