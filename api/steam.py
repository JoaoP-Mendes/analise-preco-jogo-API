import requests

def requisicao(appids):
    try:
        url = f"https://store.steampowered.com/api/appdetails?appids={appids}"
        busca = requests.get(url)
        dados = busca.json()

        if busca.status_code == 200:
            dados_requisicao = dados[f"{appids}"]["data"]

            retorno_requisicao = {
                "game":dados_requisicao["type"],
                "nome":dados_requisicao["name"],
                "appidsteam":dados_requisicao["steam_appid"],
                "desenvolvedora":dados_requisicao["developers"][0],
                "publicadora":dados_requisicao["publishers"][0],
                "genero":dados_requisicao["genres"][0]["description"],
                "gratuito":dados_requisicao["is_free"]
            }
            if dados_requisicao["is_free"]:
                retorno_requisicao["preco"] = 0.00
            else:
                retorno_requisicao["preco"] = round(dados_requisicao["price_overview"]["initial"] / 100, 2)
            return retorno_requisicao

        else:
            print(f"Algo de errado aconteceu: {busca.status_code}")


    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")


requisicao(440)
