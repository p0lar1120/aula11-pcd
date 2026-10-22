## 01 - Crie um programa Python que consulte e apresente todos os clientes cadastrados na tabela clientes.

from conexao import usar_conexao_mongo

def listar_clientes(db):
    clientes = list(db.clientes.find().sort("_id", 1))

    print()
    print(f"{'ID':>4}  {'Cliente':<30}  {'UF':<2}  {'Sexo':<4}  {'Status':<10}")
    print("-" * 58)
    for c in clientes:
        print(
            f"{c.get('_id', ''):>4}  {c.get('cliente', ''):<30}  "
            f"{c.get('estado', ''):<2}  {c.get('sexo', ''):<4}  {c.get('status', ''):<10}"
        )
    print("-" * 58)
    print(f"Total de clientes: {len(clientes)}")

usar_conexao_mongo(listar_clientes)