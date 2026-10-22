## Liste todas as vendas cujo valor total seja superior a R$ 6.000,00.

from conexao import usar_conexao_mongo

def vendas_superior(db):
    vendas = list(db.vendas.aggregate([
        {"$match": {"total": {"$gt": 6000}}},
        {"$sort": {"_id": 1}},
        {"$lookup": {
            "from": "vendedores",
            "localField": "idVendedor",
            "foreignField": "_id",
            "as": "vendedor",
        }},
        {"$set": {"vendedor": {"$first": "$vendedor.nome"}}},
    ]))
    print ()
    print(f"{'ID':>4}  {'Vendedor':<30}  {'Total':>10}")
    print("-" * 48)
    for v in vendas:
        print(
            f"{v.get('_id', ''):>4}  {v.get('vendedor', ''):<30}  "
            f"{v.get('total', 0):>10.2f}"
        )
    print("-" * 48)
    print(f"Total de vendas: {len(vendas)}")

usar_conexao_mongo(vendas_superior)