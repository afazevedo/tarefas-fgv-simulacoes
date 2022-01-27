import os
import pandas as pd

def leCONFHD(caminho):
    df = pd.read_fwf(os.path.join(caminho, 'CONFHD.DAT')).iloc[1:]
    df.to_excel(os.path.join(caminho, 'CONFHD.xlsx'), index=False)

def escreveCONFHD(caminho, arquivo=""):
    if arquivo == "":
        arquivo = os.path.join(caminho, "CONFHD.xlsx")
    
    df = pd.read_excel(arquivo)
    df['NOME'] = [" ".join([j for j in i.split(' ') if len(j) > 0]) for i in df['NOME'].values]
    s = " {:4} {:12} {:4}  {:4} {:4} {:6.2f} {:4}   {:4}     {:4}     {:4}\n"

    saida = " NUM  NOME         POSTO JUS   REE V.INIC U.EXIS MODIF INIC.HIST FIM HIST\n"
    saida += " XXXX XXXXXXXXXXXX XXXX  XXXX XXXX XXX.XX XXXX   XXXX     XXXX     XXXX\n"
    for i in df.iterrows():
        saida += s.format(*(i[1][:6]), i[1][6].rjust(4), *(i[1][7:]))
    
    with open(os.path.join(caminho, "CONFHD.DAT"), 'w') as f:
        f.writelines(saida)

def main():
    while True:
        print("--- PROGRAMA DE ALTERAÇÃO DO CONFHD DO NEWAVE ---")
        print("Digite a opção desejada")
        print(" 1 - Transformar CONFHD.DAT em XLSX")
        print(" 2 - Transformar CONFHD.XLSX em DAT")
        print(" 3 - Sair")
        ans = input()
        print("")

        if ans == '3':
            break
        
        if ans not in ['1', '2']:
            continue

        while True:
            print("Digite o caminho completo para a pasta do caso:")
            caminho = input()
            if os.path.exists(caminho):
                break
            print("O caminho informado não existe! \n")
        print("")

        if ans == '2':
            while True:
                print("Digite o caminho completo para o arquivo Excel com o CONFHD (deixe em branco para usar o da pasta do caso):")
                arquivo = input()

                if arquivo == "":
                    arquivo = os.path.join(caminho, "CONFHD.xlsx")

                if os.path.exists(arquivo):
                    break
                print("O arquivo informado não existe! \n")

            escreveCONFHD(caminho, arquivo)
            print("CONFHD atualizado com sucesso! \n")
        else:
            leCONFHD(caminho)
            print("CONFHD lido com sucesso! \n")

main()