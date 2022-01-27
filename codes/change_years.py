def changeYears(arquivo, caso):
    with open(arquivo, "r") as myfile:
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
            
    with open(arquivo, 'w') as myfile:
        myfile.write(filedata)

def main():
    changeYears("D:\\mndzvd\\Documentos\\GitHub\\tarefas-fgv-simulacoes\\deck_newave_seco\\DSVAGUA.DAT", "SECO")
        
if __name__ == "__main__":
    main()   
        