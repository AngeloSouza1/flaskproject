import urllib.request
import json

def resultado_filmes(tipo):
    # Dicionário de tipos com os URLs correspondentes
    urls = {
        'Populares': 'https://api.themoviedb.org/3/discover/movie?sort_by=popularity.desc&api_key=8e0c5130f5d00dd74f764af4153b5e6f',
        'Animação': 'https://api.themoviedb.org/3/discover/movie?certification_country=US&certification.lte=G&sort_by=popularity.desc&api_key=8e0c5130f5d00dd74f764af4153b5e6f',
        '2010': 'https://api.themoviedb.org/3/discover/movie?primary_release_year=2010&sort_by=vote_average.desc&api_key=8e0c5130f5d00dd74f764af4153b5e6f'
    }

    # Verifica se o tipo fornecido é válido
    if tipo not in urls:
        print(f"Tipo '{tipo}' inválido. Os tipos disponíveis são: {', '.join(urls.keys())}")
        return []

    url = urls[tipo]

    try:
        # Faz a requisição à API
        resposta = urllib.request.urlopen(url)
        dados = resposta.read()
        dados_json = json.loads(dados)

        # Processa os dados para extrair os campos necessários
        filmes = [
            {
                "title": filme.get("title"),
                "backdrop_path": filme.get("backdrop_path"),
                "overview": filme.get("overview"),
                "vote_average": filme.get("vote_average")
            }
            for filme in dados_json.get("results", [])
        ]

        return filmes

    except Exception as e:
        print(f"Erro ao buscar filmes: {e}")
        return []
