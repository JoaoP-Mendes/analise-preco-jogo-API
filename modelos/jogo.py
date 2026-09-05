from api.steam import requisicao
from bancodados.banco import bancoDados
import pymysql

conn = bancoDados()
conn.conectar()


class Jogo():
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

        except pymysql.err.IntegrityError:
            print(f"O jogo com essa appid {self.appid} já está informado nos registros, informe um novo appid")   
        except Exception as e:
            print(f"Ocorreu algo insperado:{e}")


    def excluirJogo(self, quem):
        try:
            deletando = "DELETE FROM jogos WHERE appid = %s"
            self.conexao.executar(deletando, quem)

        except Exception as e:
            print(f"Aconteceu algo: {e}")


while True:
    info = int(input("appid: "))
    jofo = Jogo(conn, info)
    jofo.novoJogo()