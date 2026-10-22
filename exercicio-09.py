## Calcule e mostre quantas vendas cada vendedor realizou.

from conexao import usar_conexao_mongo

def total_vendas_por_vendedor(db):
    vendas_por_vendedor = list(db.vendas.aggregate([
        {"$group": {"_id": "$idVendedor", "total_vendas": {"$sum": 1}}},
        {"$sort": {"_id": 1}},
        {"$lookup": {
            "from": "vendedores",
            "localField": "_id",
            "foreignField": "_id",
            "as": "vendedor",
        }},
        {"$set": {"vendedor": {"$first": "$vendedor.nome"}}},
    ]))
    print()
    print(f"{'ID':>4}  {'Vendedor':<30}  {'Total de Vendas':>15}")
    print("-" * 55)
    for v in vendas_por_vendedor:
        print(
            f"{v.get('_id', ''):>4}  {v.get('vendedor', ''):<30}  "
            f"{v.get('total_vendas', 0):>15}"
        )
    print("-" * 55)
usar_conexao_mongo(total_vendas_por_vendedor)