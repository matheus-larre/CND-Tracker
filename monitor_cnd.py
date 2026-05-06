# monitor_cnd.py
# Ponto de entrada da aplicação. Função: ORQUESTRAR.
# Não tem lógica de negócio — apenas chama os serviços na ordem certa.

from services.data_service  import carregar_clientes, salvar_clientes
from services.rules_service import calcular_status, filtrar_criticos
from services.email_service import enviar_alerta

def main():
    print("=" * 50)
    print("  CND-Tracker — Iniciando monitoramento...")
    print("=" * 50)

    # 1. Carregar dados
    df = carregar_clientes()

    # 2. Aplicar regras de negócio
    df = calcular_status(df)

    # 3. Exibir resumo no terminal
    print(df[["Nome", "Vencimento", "Dias Restantes", "Status"]].to_string(index=False))

    # 4. Persistir resultados
    salvar_clientes(df)

    # 5. Notificar sobre críticos
    df_criticos = filtrar_criticos(df)
    enviar_alerta(df_criticos)

    print("=" * 50)
    print("  Monitoramento concluído.")
    print("=" * 50)

if __name__ == "__main__":
    main()