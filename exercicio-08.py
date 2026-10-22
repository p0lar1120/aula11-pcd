## Informe quantas vendas possuem valor superior a R$ 6.000,00.

from conexao import usar_conexao_mongo

def total_vendas_superior(db):
    total = db.vendas.count_documents({"total": {"$gt": 6000}})
    print()
    print(f"Total de vendas com valor superior a R$ 6.000,00: {total}")

usar_conexao_mongo(total_vendas_superior)