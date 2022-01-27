import os 

def changeYears(agrint, caso):
    with open (agrint, "r") as myfile:
        filedata = myfile.read()
        if caso == "seco" or caso == "SECO":
            filedata = filedata.replace("2020", "2017")
            filedata = filedata.replace("2021", "2018")
            filedata = filedata.replace("2022", "2019")
            filedata = filedata.replace("2023", "2020")
            filedata = filedata.replace("2024", "2021")
        else:
            filedata = filedata.replace("2020", "2015")
            filedata = filedata.replace("2021", "2016")
            filedata = filedata.replace("2022", "2017")
            filedata = filedata.replace("2023", "2018")
            filedata = filedata.replace("2024", "2019")
            
    with open(agrint, 'w') as myfile:
        myfile.write(filedata)
        
def changeMonths(agrint, caso):
    with open (agrint, "r") as myfile:
        first_part = []
        for line in myfile:
            first_part.append(line)
            if "999" in line:
                filedata = myfile.read()
                if caso == "seco" or caso == "SECO":
                    filedata = filedata.replace(" 10 ", " 12 ")
                    filedata = filedata.replace(" 11 ", " 1 ")
                    filedata = filedata.replace(" 9 ", " 11 ")
                    filedata = filedata.replace(" 8 ", " 10 ")
                    # filedata = "".join((filedata[:3], filedata[4:].replace(" 9 ", " 11 ")))
                    # filedata = "".join((filedata[:3], filedata[4:].replace(" 10 ", " 12 ")))
                    # filedata = "".join((filedata[:3], filedata[4:].replace(" 11 ", " 1 ")))
        filedata = "".join(first_part) + filedata
    with open(agrint, 'w') as myfile:
        myfile.write(filedata)

changeYears("D:\\mndzvd\\Documentos\\GitHub\\tarefas-fgv-simulacoes\\deck_newave_seco\\AGRINT.DAT", "SECO")
# changeMonths("D:\\mndzvd\\Documentos\\GitHub\\tarefas-fgv-simulacoes\\deck_newave_seco\\AGRINT.DAT", "SECO")

def main():
     while True:
        print("--- PROGRAMA DE ALTERAÇÃO DO AGRINT DO NEWAVE ---")
        print("Digite a opção desejada")
        print(" 1 - Transformar ANOS")
        print(" 2 - Transformar MESES")
        print(" 3 - Sair")
        ans = input()
        print("")
        
        if ans == '3':
            break
        
        if ans == '1':
            while True:
                print("Digite o caminho completo de onde está o arquivo:")
                caminho = input()
                print("Digite se o arquivo é do caso SECO ou ÚMIDO:")
                caso = input()
                
                arquivo = os.path.join(caminho, "AGRINT.DAT")

                if os.path.exists(arquivo):
                    changeYears(arquivo, caso)
                    print("Anos do AGRINT atualizado com sucesso! \n")    
                    break
                else:
                    print("O arquivo informado não existe! \n")
                    
        else:
            while True:
                print("Digite o caminho completo de onde está o arquivo:")
                caminho = input()
                print("Digite se o arquivo é do caso SECO ou ÚMIDO:")
                caso = input()
                
                arquivo = os.path.join(caminho, "AGRINT.DAT")

                if os.path.exists(arquivo):
                    changeMonths(arquivo, caso)
                    print("Meses do AGRINT atualizado com sucesso! \n")    
                    break
                else:
                    print("O arquivo informado não existe! \n")
        
# if __name__ == "__main__":
#     main()   