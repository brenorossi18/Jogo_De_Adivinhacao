import forca
import adivinhacao

def escolher_jogo():
    print("*********************************")
    print("***** Escolha o seu Jogo *****")
    print("*********************************")

    print(" Forca (1) Adivinhação(2)")

    jogo = int(input("Qual é o seu Jogo?"))

    if (jogo == 1):
        print('Jogando Forca')
        forca.jogar_forca()
    elif(jogo == 2):
        print('Jogando Forca')
        adivinhacao.jogar_adivinhacao()

if (__name__=="__main__"):
    escolher_jogo()