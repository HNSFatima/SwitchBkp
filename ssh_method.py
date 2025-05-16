from netmiko import ConnectHandler

from utils import getFileName


class Switch:
    def __init__(self, model:str, ip:str, user:str, password:str):
        self.model = model
        self.ip = ip
        self.user = user
        self.password = password
    
    def run(self):
        

        # Dados do switch Dell
        switch = {
            'device_type': 'dell_os10',  # ou 'dell_os10' para OS10
            'ip': self.ip,
            'username': self.user,
            'password': self.password,
        }
        try:
            print(f"⏳ Conectando ao switch Dell {self.model} - {switch["ip"]}...", end="\r",flush=True)
            conexao = ConnectHandler(**switch)            
            
            file_name = getFileName.GetFileName(switch["ip"]).get()
           
            # Comando para obter a configuração
            configuracao = conexao.send_command("show running-config")
            # Salva em um arquivo
            with open(file_name, "w") as f:
                f.write(configuracao)

            print(f"✅ Configuração obtida e salva em {file_name}")
            # conexao.disconnect()

        except Exception as e:
            print(f"❌ Erro ao conectar ao switch: {e}")
        finally:
            conexao.disconnect()
        



