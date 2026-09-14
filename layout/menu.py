from modelos.historico import Historico
from modelos.jogo import Jogo
from layout.layout import *
from bancodados.banco import bancoDados


connObj = bancoDados()
connObj.conectar()

def menu_jogo(connObj):
    while True:
        try:
            print("")
            resposta = int(input("\033[36m------- MENU JOGO -------\033[m \n1 - Adicionar novo jogo \n2 - Excluir jogo \n3 - Listar jogos \n0 - Voltar menu \nResposta: "))
            if resposta == 1:
                print("")
                info_appid = int(input("Digite o APPID do jogo: "))

                jogo = Jogo(connObj, info_appid)
                jogo.novoJogo()

            elif resposta == 2:
                print("")
                info_appid = input("Digite o APPID do jogo para exclusão: ")
                jogo = Jogo(connObj, info_appid)
                jogo.excluirJogo(info_appid)

            elif resposta == 3:
                print("")
                carregando()
                Jogo.listarJogas(connObj)

            elif resposta == 0:
                print("")
                voltando()
                break

            else:
                print("")
                print("ERRO: Ação não reconhecida, informe uma ação válida.")
                print("")
                continue

        except Exception as e:
            print(f"Algo deu errado: {e}")


def menu_historico(connObj):
    while True:
        try:
            print("")
            resposta = int(input("\033[36m------- HISTORICO -------\033[m \n1 - Atualizar historico \n2 - Ver historico \n0 - Voltar menu \nResposta: "))
            if resposta == 1:
                print("")
                historico = Historico(connObj)
                historico.novoRegistro()
                carregando()

            elif resposta == 2:
                print("")
                carregando()
                Historico.verHistorico(connObj)

            elif resposta == 0:
                print("")
                voltando()
                break

            else:
                print("")
                print("ERRO: Ação não reconhecida, informe uma ação válida.")
                print("")
                continue
 
        except Exception as e:
            print(f"Algo deu errado: {e}")