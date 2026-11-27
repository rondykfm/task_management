from fastapi_mail import FastMail, MessageSchema, ConnectionConfig, MessageType
from pydantic import EmailStr, BaseModel
from typing import List


conf = ConnectionConfig(
    MAIL_USERNAME = "rondykfm@gmail.com",
    MAIL_PASSWORD = "nnja zhfa nqpc ozxc",
    MAIL_FROM = "rondykfm@email.com",
    MAIL_PORT = 587,
    MAIL_SERVER = "rondykfm.gmail.com",
    MAIL_FROM_NAME="Desired Name",
    MAIL_STARTTLS = True,
    MAIL_SSL_TLS = False,
    USE_CREDENTIALS = True,
    VALIDATE_CERTS = True
)



async def send_mail(emails: List[str]):
    html = """<p>Hi, thanks for Registration. </p> """

    message = MessageSchema(
        subject="Registration confirmation",
        recipients=emails,
        body=html,
        subtype=MessageType.html)

    fm = FastMail(conf)
    await fm.send_message(message)
    print({"message":"email has been sent "})
    ##return {"message":"email has been sent "}
    