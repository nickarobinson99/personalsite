from fastapi_mail import ConnectionConfig
import os

mail_config = ConnectionConfig(
    MAIL_USERNAME=os.environ.get('EMAIL_USERNAME'),
    MAIL_PASSWORD=os.environ.get('EMAIL_PASSWORD'),
    MAIL_FROM=os.environ.get('EMAIL_SENDER'),
    MAIL_PORT=587,
    MAIL_SERVER='smtp.office365.com',
    MAIL_FROM_NAME='Personal Site Mail',
    MAIL_STARTTLS=True,
    MAIL_SSL_TLS=False,
    USE_CREDENTIALS=True,
    VALIDATE_CERTS=True,
)