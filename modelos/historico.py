from api.steam import requisicao
from bancodados.banco import bancoDados
from datetime import date
import pandas as pd

conn = bancoDados()
conn.conectar()


class Historico():
    def __init__(self, conexao):
        self.conexao = conexao


    
    def novoRegistro(self):
        try:
            appids_banco = pd.read_sql("SELECT * FROM jogos", self.conexao)
            chaves_appids = appids_banco["appid"]

            for chave in chaves_appids:
                preco_jogo = requisicao(chave)
                valores = (chave, date.today(), preco_jogo["preco"])
                registro_historico = "INSERT INTO historico (appid, data_analise, preco) VALUES (%s, %s, %s)"
                self.conexao.executar(registro_historico, valores)

        except Exception as e:
            print(f"Ocorreu algo inesperado: {e}")

    def verHistorico(self):
        ver = pd.read_sql("SELECT * FROM historico", self.conexao)
        print(ver)
    

