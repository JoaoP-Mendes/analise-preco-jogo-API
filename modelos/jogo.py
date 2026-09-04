from api.steam import requisicao
from bancodados.banco import bancoDados

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
            
        except Exception as e:
            print(f"Ocorreu algo insperado:{e}")

jofo = Jogo(conn, "10")
jofo.novoJogo()