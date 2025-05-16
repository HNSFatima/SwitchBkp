import pandas as pd
import ssh_method as ssh
import md_x1052
from utils.deleteFiles import DeleteFile

file = pd.read_excel(r".\data\switches.xlsx")


for index, row in file.iterrows() :
    model = str( row["Modelo"])
    ip = str( row["IP"])
    user = str( row["User"])
    pwd = str( row["Senha"])
    
    if model == "X1052":
        md_x1052.Switch(model=model, ip=ip, user=user, password=pwd).run()
    elif model == "2824":
        # print(model,index, "teste2")
        pass
    elif (model == "S3148") :
        ssh.Switch(model=model, ip=ip, user=user, password=pwd).run()
        
DeleteFile().remove()
    