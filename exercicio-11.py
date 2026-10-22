## Liste os diferentes status existentes na tabela clientes, sem apresentar valores repetidos.

from conexao import usar_conexao_mongo

def listar_status_distintos(db):
    status_distintos = db.clientes.distinct("status")
    print()
    print("Status distintos encontrados na tabela clientes:")
    for status in status_distintos:
        print(f"- {status}")
    print(f"Total de status distintos: {len(status_distintos)}")

usar_conexao_mongo(listar_status_distintos)
