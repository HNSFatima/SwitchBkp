from playwright.sync_api import sync_playwright

from utils import getFileName,logger as log, sendMail

class Switch:
    def __init__(self, model:str, ip:str, user:str, password:str):
        self.model = model
        self.ip = ip
        self.user = user
        self.password = password
    
    def run(self):
        logs = log.Logger()
        print(f"⏳ Conectando ao switch Cisco {self.model} - {self.ip}...", end="\r",flush=True)
        try:
            with sync_playwright() as p:
                IP = self.ip
                navegador = p.chromium.launch(headless=False)
                pagina = navegador.new_page(ignore_https_errors=True, locale='en-US')
                url = f"http://{IP}"            

                pagina.goto(url)
                
                pagina.wait_for_selector('xpath=//*[@id="btnLogin"]')

                # Preencher UserName
                # //*[@id="userName$query"]
                pagina.fill('xpath=//*[@id="userName$query"]', self.user )

                # Preencher password       
                pagina.fill('xpath=//*[@id="password"]', self.password )

                # clicar em "Log in"
                pagina.locator('xpath=//*[@id="btnLogin"]').click()

                pagina.wait_for_selector('xpath=//*[@id="bodyTree"]/tbody')
                
                # clicar menu "Administration"
                pagina.locator('xpath=//*[@id="span_1620"]').click()
                

                # clicar submenu "File Management"
                pagina.wait_for_selector('xpath=//*[@id="a_2070"]')
                pagina.locator('xpath=//*[@id="a_2070"]').click()
                

                # clicar submenu "File Operations"
                pagina.wait_for_selector('xpath=//*[@id="./filemgmt/file_operations_jq.htm"]')
                pagina.locator('xpath=//*[@id="./filemgmt/file_operations_jq.htm"]').click()

                # Aguardar carregamento da tela
                pagina.wait_for_selector('xpath=//*[@id="mainFrame"]')
                frame = pagina.frame_locator('xpath=//*[@id="mainFrame"]')
                # //*[@id="lblOperTypeUpdate"]
                frame.locator('xpath=//*[@id="tdOperTypeBackup"]').click()


                # clica no "Ok"
                with pagina.expect_download() as download_info:
                    frame.locator('xpath=//*[@id="defaultButton"]').click()
                
                download = download_info.value
                file_name = getFileName.GetFileName(self.ip).get()
                download.save_as(rf".\{file_name}")
                # D:\repos\switches\md_x1052.py

                #aguarda download
                print(f"✅ Configuração obtida e salva em {file_name}")
                logs.info(f"Conexão com switch {IP} foi bem sucessida. Log salvo em {file_name}")
                pagina.wait_for_timeout(1000)
        except Exception as e:
            print(f"❌ Erro ao conectar ao switch: {e}")
            logs.erro(f"Erro ao conectar ao switch{IP}. Erro: {e}")
            sendMail.mail(f"Erro ao conectar ao switch{IP}. Erro: {e}","Erro")