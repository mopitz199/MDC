from django.conf import settings
import sendgrid
import os
from sendgrid.helpers.mail import *

def sendEmail(fromEmail=None, toEmail=None, sub="", msg=""):
    key = getattr(settings, 'SENGRID_KEY', None)
    if key and toEmail:
        sg = sendgrid.SendGridAPIClient(apikey=key)
        from_email = Email(fromEmail if fromEmail else 'mopitz199@gmail.com')
        to_email = Email(toEmail)
        subject = sub
        content = Content("text/plain", msg)
        mail = Mail(from_email, subject, to_email, content)
        response = sg.client.mail.send.post(request_body=mail.get())
        if response.status_code==202:
            return [True, u'El correo se envio exitosamente']
        else:
            return [True, u'No se pudo enviar el correo']
    else:
        return [False, u'No se pudo enviar el correo']
