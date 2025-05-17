from playwright.sync_api import sync_playwright

from utils import getFileName

class Switch:
    def __init__(self, model:str, ip:str, user:str, password:str):
        self.model = model
        self.ip = ip
        self.user = user
        self.password = password
    
    def run(self):
        print(f"⏳ Conectando ao switch Dell {self.model} - {self.ip}...", end="\r",flush=True)
        try:
            with sync_playwright() as p:
                IP = self.ip

                navegador = p.chromium.launch(headless=False)
                pagina = navegador.new_page()
                url = f"http://{IP}"            

                pagina.goto(url)
                pagina.wait_for_selector('xpath=//*[@id="aemphButton"]')

                # Preencher UserName
                # //*[@id="userName$query"]
                pagina.fill('xpath=//*[@id="userName$query"]', self.user )

                # Preencher password            
                pagina.fill('xpath=//*[@id="password$query"]', self.password )

                # clicar em "Log in"
                pagina.locator('xpath=//*[@id="aemphButton"]').click()

                pagina.wait_for_selector('xpath=//*[@id="BandDescText"]')
                
                # clicar menu "Switch Management"
                pagina.locator('xpath=//*[@id="ui-id-50"]').click()
                

                # clicar submenu "Switch Management"
                pagina.locator('xpath=//*[@id="ui-id-57"]').click()
                
                # clica no "edit" de "Backup Files"
                pagina.wait_for_selector('xpath=//*[@id="backup_files"]/span/div/div[2]').click()

                
                # clica no "Ok"
                with pagina.expect_download() as download_info:
                    pagina.wait_for_selector('xpath=//*[@id="btnApply"]/div').click()
                
                download = download_info.value
                file_name = getFileName.GetFileName(self.ip).get()
                download.save_as(rf".\{file_name}")
                # D:\repos\switches\md_x1052.py

                #aguarda download
                print(f"✅ Configuração obtida e salva em {file_name}")
                pagina.wait_for_timeout(1000)
        except Exception as e:
            print(f"❌ Erro ao conectar ao switch: {e}")