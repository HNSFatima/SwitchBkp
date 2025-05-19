import pandas as pd
import os
from pathlib import Path
from utils import logger as log

class DeleteFile():
    def __init__(self):        
        pass

    def remove(self):
        path = Path("./backup_files")
        
        if not path.exists():
            os.mkdir("./backup_files")

        files = [f.name for f in path.iterdir() if f.is_file()]
        files = pd.DataFrame(files, columns=['SW'])
        files["ip"] = files["SW"].str.split("-").str[1]
        files["data"] = files["SW"].str.split("-").str[2]
        files["data"] = files["data"].str.split(".").str[0]
        files["data"] = pd.to_datetime(files["data"].astype(str), format='%d%m%Y%H%M%S')
        files = files[["SW","ip","data"]].sort_values(["ip","data"],ascending=True)

        grouped = files[["ip",'SW']].groupby(['ip']).count()
        grouped = grouped[grouped['SW'] > 3 ]

        for idx,row in grouped.iterrows():
            sw = files[files["ip"]== idx].sort_values(['data'],ascending=False).reset_index().iloc[3:]
            sw = sw['SW'].values
            for f in sw:
                file = path.joinpath(f)
                os.remove(file)
        if len(grouped.index) > 0:
            logs = log.Logger()
            logs.info("Os arquivos antigos de backup foram removidos")