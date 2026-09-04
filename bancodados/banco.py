import pymysql.connections as mysql
from config.config import BD_CONFIG

class bancoDados():
    def __init__(self):
        self.conexao = None

    def conectar(self):
        try:
            self.conexao = mysql.Connection(**BD_CONFIG)

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e} ")

    def desconectar(self):
        try:
            self.conexao.close()

        except Exception as e:
            print(f"Ocorreu um erro inesperado: {e}")


    def executar(self, query, valor = ()):
        try:
            cursor = self.conexao.cursor()
            cursor.execute(query, valor)

            if query.strip().upper().startswith("SELECT"):
                resultado = cursor.fetchall()
                return resultado

            else:
                self.conexao.commit()
                return cursor.lastrowid

        except Exception as e:
            raise