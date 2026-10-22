from pymongo import MongoClient

def usar_conexao_mongo(acao, url="mongodb://localhost:27017/", dbname="dbven"):
    with MongoClient(url) as client:
        db = client[dbname]
        print(f"Conectado a {url} / db={dbname}")
        return acao(db)
