from datetime import datetime

class GetFileName:
    def __init__(self, ip:str):
        self.ip = ip
        
    def get(self) :
        now = datetime.now()
        date = now.strftime("%d%m%Y%H%M%S")
        path = r".\backup_files"
        file_name = f'SW-{self.ip}-{date}.txt'
        return rf'{path}\{file_name}'

    # def get(self) -> str: