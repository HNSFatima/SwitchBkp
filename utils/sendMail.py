import smtplib
from email.mime.text import MIMEText

class mail:
    def __init__(self, msg:str, assunto:str):
        pass
        remetente = 'suporte2.tasy@hnsf.com.br'
        destinatario = 'suporte2.tasy@hnsf.com.br'
        
        mail = MIMEText(msg)
        mail['Subject'] = assunto
        mail['From'] = remetente
        mail['To'] = destinatario

        servidor = smtplib.SMTP('smtp.gmail.com',587)
        servidor.starttls()
        servidor.login('suporte2.tasy@hnsf.com.br','rxhbyqsbriukrorq')

        servidor.send_message(mail)
        servidor.quit()