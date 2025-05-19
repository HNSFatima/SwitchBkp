import logging
import os

class Logger:
    def __init__(self):        
        self.type = type

        path = r"..\logs"
        if not os.path.exists(path):
            os.mkdir(path)

        logging.basicConfig(
            filename= self.path + rf'\logs.log',
            level=logging.DEBUG,
            format='%(asctime)s - %(levelname)s - %(name)s - %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )
        self.logger = logging.getLogger('switch')

    def info(self, msg:str):
        self.message = f'💡 {msg}'
        self.logger.info(msg)

    def erro(self, msg:str):
        self.message = f'❌ {msg}'
        self.logger.error(msg)

    def warning(self, msg:str):
        self.message = f"⚠️ {msg}"
        self.logger.warning(msg)