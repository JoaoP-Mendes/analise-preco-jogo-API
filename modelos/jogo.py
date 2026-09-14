from api.steam import requisicao
from bancodados.banco import bancoDados
from layout.layout import *
import pymysql
import pandas as pd

conn = bancoDados()
conn.conectar()


class Jogo():
    """
Cria um novo jogo para encaminhar para o banco de dados.

Link para pegar a appid: https://steamdb.info/apps/
    """
    def __init__(self, conexao, appid):
        self.conexao = conexao
        self.appid = appid


    def novoJogo(self): 
        try:
            dados_requisicao = requisicao(self.appid)
            valores = (self.appid, dados_requisicao["nome"], dados_requisicao["desenvolvedora"], 
                       dados_requisicao["publicadora"], dados_requisicao["genero"], dados_requisicao["gratuito"] )

            inserindo = "INSERT INTO jogos (appid, nome, desenvolvedora, publicadora, genero, gratuito) VALUES(%s, %s, %s, %s, %s, %s)"
            self.conexao.executar(inserindo, valores)
            cadastrando()

        except pymysql.err.IntegrityError:
            print(f"Jogo já informado com essa appid {self.appid}, informe um para seguir")  

        except Exception as e:
            print(f"Ocorreu algo insperado:{e}")

    def excluirJogo(self, quem):
        try:
            deletando = "DELETE FROM jogos WHERE appid = %s"
            self.conexao.executar(deletando, quem)
            excluido()

        except pymysql.err.IntegrityError:
            print(f"Não é possível excluir esse jogo, o jogo possui histórico cadastrado")

        except Exception as e:
            print(f"Aconteceu algo: {e}")

    def listarJogas(self):
        try:
            listando = pd.read_sql("SELECT * FROM jogos", self.conexao)
            print(listando)

        except Exception as e:
            print(f"Aconteceu algo: {e}")


