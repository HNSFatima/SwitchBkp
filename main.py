import os
import pandas as pd
import ssh_method as ssh
import md_x1052
from utils.deleteFiles import DeleteFile

def main():
    path = r".\data\switches.xlsx"
    # Criar o arquivo, caso não exista
    if not os.path.exists(path):
        sheet = pd.DataFrame([],columns=["Modelo","IP","User","Senha"])
        sheet.to_excel(path,index=False)
        print(fr"⚠️  Preencha o arquivo {path}")
        return

    file = pd.read_excel(path)

    # Verifica se existe dados dentro do arquivo
    if len(file.index) <= 0:
        print(fr"⚠️  Preencha o arquivo {path}")
        return

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


if __name__ == "__main__":
    main()