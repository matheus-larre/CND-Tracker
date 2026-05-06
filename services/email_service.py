# services/email_service.py
# Responsabilidade ÚNICA: construir e enviar e-mails de notificação.

import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv
import pandas as pd

load_dotenv()  # Carrega as variáveis do arquivo .env

SMTP_HOST = "smtp.gmail.com"
SMTP_PORT = 587

def _construir_corpo_html(df_criticos: pd.DataFrame) -> str:
    """
    Monta o corpo do e-mail em HTML com uma tabela dos clientes críticos.
    Separar a construção do HTML do envio facilita testes futuros.
    """
    linhas_html = ""
    for _, row in df_criticos.iterrows():
        linhas_html += f"""
        <tr>
            <td style="padding:8px; border:1px solid #ddd;">{row['Nome']}</td>
            <td style="padding:8px; border:1px solid #ddd;">{row['CNPJ']}</td>
            <td style="padding:8px; border:1px solid #ddd;">{row['Vencimento'].strftime('%d/%m/%Y')}</td>
            <td style="padding:8px; border:1px solid #ddd;">{row['Dias Restantes']} dias</td>
            <td style="padding:8px; border:1px solid #ddd;">{row['Status']}</td>
        </tr>
        """

    return f"""
    <html><body>
    <h2 style="color:#c0392b;">⚠️ Alerta de Vencimento de CNDs</h2>
    <p>Os seguintes clientes requerem atenção imediata:</p>
    <table style="border-collapse:collapse; width:100%; font-family:Arial, sans-serif;">
        <thead>
            <tr style="background-color:#2c3e50; color:white;">
                <th style="padding:8px;">Nome</th>
                <th style="padding:8px;">CNPJ</th>
                <th style="padding:8px;">Vencimento</th>
                <th style="padding:8px;">Dias Restantes</th>
                <th style="padding:8px;">Status</th>
            </tr>
        </thead>
        <tbody>{linhas_html}</tbody>
    </table>
    <p style="color:#7f8c8d; font-size:12px;">Mensagem gerada automaticamente pelo CND-Tracker.</p>
    </body></html>
    """

def enviar_alerta(df_criticos: pd.DataFrame) -> None:
    """
    Envia o e-mail de alerta se houver clientes críticos.
    Lê as credenciais exclusivamente do .env — nunca hardcoded.
    """
    if df_criticos.empty:
        print("[✓] Nenhum cliente crítico. E-mail não enviado.")
        return

    remetente  = os.getenv("EMAIL_REMETENTE")
    senha      = os.getenv("EMAIL_APP_PASSWORD")
    destinatario = os.getenv("EMAIL_DESTINATARIO")

    # Validação defensiva: aborta se as credenciais não estiverem configuradas
    if not all([remetente, senha, destinatario]):
        raise EnvironmentError(
            "Credenciais de e-mail ausentes. Verifique o arquivo .env."
        )

    msg = MIMEMultipart("alternative")
    msg["Subject"] = f"⚠️ CND-Tracker: {len(df_criticos)} cliente(s) com CND crítica"
    msg["From"]    = remetente
    msg["To"]      = destinatario

    corpo_html = _construir_corpo_html(df_criticos)
    msg.attach(MIMEText(corpo_html, "html"))

    try:
        with smtplib.SMTP(SMTP_HOST, SMTP_PORT) as servidor:
            servidor.ehlo()
            servidor.starttls()          # Criptografa a conexão
            servidor.login(remetente, senha)
            servidor.sendmail(remetente, destinatario, msg.as_string())
        print(f"[✓] E-mail de alerta enviado para {destinatario}.")
    except smtplib.SMTPAuthenticationError:
        print("[✗] Falha de autenticação. Verifique a App Password no .env.")
    except smtplib.SMTPException as e:
        print(f"[✗] Erro ao enviar e-mail: {e}")