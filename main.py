from bancodados.banco import bancoDados
from layout.menu import menu_historico
from layout.menu import menu_jogo
from layout.layout import *

connObj = bancoDados()
connObj.conectar()

while True:
    escolha = int(input("------------ INICIANDO SISTEMA ------------\nEscolha uma opção para começar\n > 1 - Jogo\n > 2 - Historico\n > 0 - Sair \nResposta: "))
    if escolha == 1:
        menu_jogo(connObj)

    elif escolha == 2:
        menu_historico(connObj)

    elif escolha == 0:
        encerrando()
        break
    