# services/rules_service.py
# Responsabilidade ÚNICA: aplicar as regras de negócio sobre os dados.
# Não sabe nada sobre Excel, e-mail ou terminal.

import pandas as pd
from config import THRESHOLD_URGENTE, THRESHOLD_ALERTA, STATUS_URGENTE, STATUS_ALERTA, STATUS_OK

def calcular_status(df: pd.DataFrame) -> pd.DataFrame:
    """
    Recebe um DataFrame com coluna 'Vencimento' e retorna o mesmo
    DataFrame com as colunas 'Dias Restantes' e 'Status' preenchidas.
    """
    hoje = pd.Timestamp.today().normalize()
    df["Vencimento"] = pd.to_datetime(df["Vencimento"])
    df["Dias Restantes"] = (df["Vencimento"] - hoje).dt.days

    def definir_status(dias):
        if dias < THRESHOLD_URGENTE:
            return STATUS_URGENTE
        elif dias <= THRESHOLD_ALERTA:
            return STATUS_ALERTA
        else:
            return STATUS_OK

    df["Status"] = df["Dias Restantes"].apply(definir_status)
    return df

def filtrar_criticos(df: pd.DataFrame) -> pd.DataFrame:
    """Retorna apenas os clientes em situação URGENTE ou ALERTA."""
    return df[df["Status"].isin([STATUS_URGENTE, STATUS_ALERTA])]