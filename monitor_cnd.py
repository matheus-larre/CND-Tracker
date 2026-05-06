import pandas as pd
import datetime

def verificar_vencimentos_excel():
    hoje = datetime.datetime.today()
    alerta_dias = 15

    print("="*60)
    print("SISTEMA DE MONITORAMENTO DE CNDs - LEITURA E GRAVAÇÃO")
    print("="*60)

    try:
        # Lê a planilha do Excel
        df = pd.read_excel('clientes_cnd.xlsx')
        df['Vencimento'] = pd.to_datetime(df['Vencimento'])
        
        # Cria a coluna 'Status' se ela ainda não existir na planilha
        if 'Status' not in df.columns:
            df['Status'] = ''

        for index, row in df.iterrows():
            nome = row['Nome']
            cnpj = row['CNPJ']
            vencimento = row['Vencimento']

            # Calcula os dias restantes
            dias_restantes = (vencimento - hoje).days

            # Define a mensagem de status e imprime no terminal
            if dias_restantes < 0:
                status = f"VENCEU há {abs(dias_restantes)} dias"
                print(f"[URGENTE] {cnpj} | {nome} | {status}")
            elif dias_restantes <= alerta_dias:
                status = f"Vence em {dias_restantes} dias"
                print(f"[ALERTA]  {cnpj} | {nome} | {status}")
            else:
                status = "Regular"
                print(f"[OK]      {cnpj} | {nome} | {status} ({dias_restantes} dias restantes)")
            
            # Grava o status na linha correspondente dentro do DataFrame (memória)
            df.at[index, 'Status'] = status

        # Salva o DataFrame atualizado de volta no arquivo Excel
        # index=False evita que o pandas crie uma coluna extra de numeração
        df.to_excel('clientes_cnd.xlsx', index=False)
        
        print("-" * 60)
        print("Planilha 'clientes_cnd.xlsx' atualizada e salva com sucesso!")
                
    except FileNotFoundError:
        print("[ERRO] O arquivo 'clientes_cnd.xlsx' não foi encontrado.")
    except Exception as e:
        print(f"[ERRO] Ocorreu um problema: {e}")

    print("="*60)

if __name__ == "__main__":
    verificar_vencimentos_excel()