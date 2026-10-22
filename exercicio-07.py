## Informe a quantidade total de vendas existentes na tabela vendas.

from conexao import usar_conexao_mongo

def total_vendas(db):
    total = db.vendas.count_documents({})
    print()
    print(f"Total de vendas: {total}")

usar_conexao_mongo(total_vendas)
