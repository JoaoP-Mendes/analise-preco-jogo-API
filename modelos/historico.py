from api.steam import requisicao
from bancodados.banco import bancoDados
from datetime import date

conn = bancoDados()
conn.conectar()


class Historico():
    def __init__(self, conexao, appid):
        self.conexao = conexao
        self.appid = appid

    def novoRegistro(self):
        try:
            dia_historico = date.today()
            dados_historico = requisicao(self.appid)
            valores = (self.appid, dia_historico, dados_historico["preco"])

            registro_historico = "INSERT INTO historico (appid, data_analise, preco) VALUES (%s, %s, %s)"
            self.conexao.executar(registro_historico, valores)

        except Exception as e:
            print(f"Ocorreu algo inesperado: {e}")
    

hit = Historico(conn, 440)
hit.novoRegistro()