from modelos.historico import Historico
from modelos.jogo import Jogo
from layout.layout import *


def menu_jogo(connObj):
    while True:
        try:
            resposta = int(input("\033[36m----- MENU JOGO -----\033[m \n1 - Adicionar novo jogo \n2 - Excluir jogo \n0 - Voltar menu \nResposta: "))
            if resposta == 1:
                print("")
                info_appid = input("Digite o APPID do jogo: ")

                jogo = Jogo(connObj, info_appid)
                jogo.novoJogo()

            elif resposta == 2:
                print("")
                info_appid = input("Digite o APPID do jogo para exclusão: ")
                Jogo.excluirJogo(connObj, info_appid)

            elif resposta == 0:
                print("")
                voltando()

            else:
                print("")
                print("ERRO: Ação não reconhecida, informe uma ação válida.")
                print("")
                continue

        except Exception as e:
            print(f"Algo deu errado: {e}")

