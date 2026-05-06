import pandas as pd
import datetime

def verificar_vencimentos_excel():
    hoje = datetime.datetime.today()
    alerta_dias = 15

    print("="*55)
    print("SISTEMA DE MONITORAMENTO DE CNDs - INTEGRAÇÃO EXCEL")
    print("="*55)

    try:
        # Lê a planilha do Excel
        df = pd.read_excel('clientes_cnd.xlsx')

        # Converte a coluna 'Vencimento' para o formato datetime do pandas
        df['Vencimento'] = pd.to_datetime(df['Vencimento'])

        for index, row in df.iterrows():
            nome = row['Nome']
            cnpj = row['CNPJ']
            vencimento = row['Vencimento']

            # Calcula os dias restantes
            dias_restantes = (vencimento - hoje).days

            if dias_restantes < 0:
                print(f"[URGENTE] CNPJ: {cnpj} | A CND de '{nome}' VENCEU há {abs(dias_restantes)} dias!")
            elif dias_restantes <= alerta_dias:
                print(f"[ALERTA] CNPJ: {cnpj} | A CND de '{nome}' vence em {dias_restantes} dias.")
            else:
                print(f"[OK] CNPJ: {cnpj} | A CND de '{nome}' está regular ({dias_restantes} dias restantes).")
                
    except FileNotFoundError:
        print("[ERRO] O arquivo 'clientes_cnd.xlsx' não foi encontrado. Verifique se ele está na mesma pasta do script.")
    except Exception as e:
        print(f"[ERRO] Ocorreu um problema ao ler os dados: {e}")

    print("="*55)

if __name__ == "__main__":
    verificar_vencimentos_excel()