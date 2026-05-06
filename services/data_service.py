# services/data_service.py
# Responsabilidade ÚNICA: I/O de dados.
# Quando migrarmos para banco de dados (Etapa B), só este arquivo muda.

import pandas as pd
from config import CAMINHO_EXCEL

def carregar_clientes() -> pd.DataFrame:
    """Lê a planilha e retorna um DataFrame."""
    return pd.read_excel(CAMINHO_EXCEL)

def salvar_clientes(df: pd.DataFrame) -> None:
    """Persiste o DataFrame atualizado na planilha."""
    df.to_excel(CAMINHO_EXCEL, index=False)
    print(f"[✓] Planilha '{CAMINHO_EXCEL}' atualizada com sucesso.")