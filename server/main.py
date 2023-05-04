import os
from typing import Optional

import httpx
from email_config import mail_config
from fastapi import FastAPI
from fastapi_mail import FastMail, MessageSchema, MessageType
from pydantic import BaseModel, EmailStr

FRIENDLY_CAPTCHA_URL = "https://api.friendlycaptcha.com/api/v1/siteverify"

class Email(BaseModel):
    organization: Optional[str] = None
    name: str
    email: EmailStr
    subject: str
    body: str
    frc_captcha_solution: str


app = FastAPI()


    
@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/contact_form')
async def contact(email: Email):
    captcha_response = await validate_captcha(email.frc_captcha_solution)
    return_message = {"message": "success"}
    if (not handle_captcha_response(captcha_response)):
        return_message = {"message": "failure"}
        return return_message
    
    mail_response = await send_mail(email)

    
    return return_message

async def validate_captcha(captcha_solution: str):
    async with httpx.AsyncClient() as client:
        post_data = {"solution": captcha_solution, "secret": os.environ.get("FRIENDLY_KEY")}
        response = await client.post(FRIENDLY_CAPTCHA_URL, data=post_data)
        return response

def handle_captcha_response(captcha_response):
    if (captcha_response.status_code == 200):
        return captcha_response.json()["success"]
    else:
        # Per the documentation, if the response code != 200, let the user through
        # as it is most likely not a captcha fail, but a server error
        return True
    
async def send_mail(email: Email):
    html="""<p>Test</p>"""
    fm = FastMail(mail_config)
    message = MessageSchema(
        subject=email.subject,
        recipients=[os.environ.get('EMAIL_RECIPIENT')],
        body=html,
        subtype=MessageType.html
    )
    response = await fm.send_message(message)
    return response