## Calcule o valor total das vendas realizadas por um vendedor específico, por exemplo: ID = 3.

from conexao import usar_conexao_mongo

def total_vendas_por_vendedor(db, id_vendedor):
    total = db.vendas.aggregate([
        {"$match": {"idVendedor": id_vendedor}},
        {"$group": {"_id": "$idVendedor", "total_vendas": {"$sum": "$total"}}},
    ])
    total_vendas = list(total)
    if total_vendas:
        print()
        print(f"Total de vendas do vendedor {id_vendedor}: R$ {total_vendas[0]['total_vendas']:.2f}")
    else:
        print()
        print(f"Não há vendas registradas para o vendedor {id_vendedor}.")

usar_conexao_mongo(lambda db: total_vendas_por_vendedor(db, 3))