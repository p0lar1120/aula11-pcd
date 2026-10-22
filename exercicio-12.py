## Apresente o nome do vendedor e o valor total vendido por ele. Ordene do maior total para o menor.

from conexao import usar_conexao_mongo

def total_vendas_por_vendedor(db):
    vendas_por_vendedor = list(db.vendas.aggregate([
        {"$group": {"_id": "$idVendedor", "total_vendas": {"$sum": "$total"}}},
        {"$sort": {"total_vendas": -1}},
        {"$lookup": {
            "from": "vendedores",
            "localField": "_id",
            "foreignField": "_id",
            "as": "vendedor",
        }},
        {"$set": {"vendedor": {"$first": "$vendedor.nome"}}},
    ]))
    print()
    print(f"{'ID':>4}  {'Vendedor':<30}  {'Total Vendido':>15}")
    print("-" * 55)
    for v in vendas_por_vendedor:
        print(
            f"{v.get('_id', ''):>4}  {v.get('vendedor', ''):<30}  "
            f"R$ {v.get('total_vendas', 0):>14,.2f}"
        )
    print("-" * 55)
usar_conexao_mongo(total_vendas_por_vendedor)