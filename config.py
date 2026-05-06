# config.py
# Centraliza todas as configurações do sistema.
# Vantagem: para mudar um threshold, você altera em UM lugar.

CAMINHO_EXCEL = "clientes_cnd.xlsx"

THRESHOLD_URGENTE = 0   # Dias restantes < 0
THRESHOLD_ALERTA  = 15  # Dias restantes <= 15

STATUS_URGENTE = "🔴 URGENTE"
STATUS_ALERTA  = "🟡 ALERTA"
STATUS_OK      = "🟢 OK"