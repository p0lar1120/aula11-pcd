## Liste os clientes que possuem status Silver ou Platinum. Apresente: cliente, sexo, status.

from conexao import usar_conexao_mongo

def clientes_silver_platinum(db):
    clientes = list(db.clientes.find({"status": {"$in": ["Silver", "Platinum"]}}).sort("_id", 1))

    print()
    print(f"{'ID':>4}  {'Cliente':<30} {'Sexo':<4}  {'Status':<10}")
    print("-" * 58)
    for c in clientes:
        print(
            f"{c.get('_id', ''):>4}  {c.get('cliente', ''):<30}  "
            f"{c.get('sexo', ''):<4}  {c.get('status', ''):<10}"
        )
    print("-" * 58)
    print(f"Total de clientes: {len(clientes)}")

usar_conexao_mongo(clientes_silver_platinum)
