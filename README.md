# Aula 11 - Programação para Ciência de Dados

Exercícios de consulta ao MongoDB (banco `dbven`) usando Python e PyMongo.

## Pré-requisitos

- Python 3 com `pymongo` instalado
- MongoDB rodando em `mongodb://localhost:27017/` com o banco `dbven` carregado

A conexão é feita por `conexao.py` (`usar_conexao_mongo`), usada por todos os exercícios.

## Lista de exercícios

| # | Arquivo | Enunciado |
|---|---------|-----------|
| 01 | [exercicio-01.py](exercicio-01.py) | Consultar e apresentar todos os clientes cadastrados na coleção `clientes`. |
| 02 | [exercicio-02.py](exercicio-02.py) | Apresentar apenas nome, sexo e status dos clientes com status Silver. |
| 03 | [exercicio-03.py](exercicio-03.py) | Listar os clientes com status Silver ou Platinum (cliente, sexo, status). |
| 04 | [exercicio-04.py](exercicio-04.py) | Listar os clientes cujo nome contenha a sequência "Alb". |
| 05 | [exercicio-05.py](exercicio-05.py) | Listar todas as vendas com valor total superior a R$ 6.000,00. |
| 06 | [exercicio-06.py](exercicio-06.py) | Listar as vendas com total entre R$ 6.000,00 e R$ 8.000,00. |
| 07 | [exercicio-07.py](exercicio-07.py) | Informar a quantidade total de vendas existentes. |
| 08 | [exercicio-08.py](exercicio-08.py) | Informar quantas vendas possuem valor superior a R$ 6.000,00. |
| 09 | [exercicio-09.py](exercicio-09.py) | Calcular e mostrar quantas vendas cada vendedor realizou. |
| 10 | [exercicio-10.py](exercicio-10.py) | Calcular o valor total das vendas de um vendedor específico (ex.: ID = 3). |
| 11 | [exercicio-11.py](exercicio-11.py) | Listar os diferentes status de clientes, sem valores repetidos. |
| 12 | [exercicio-12.py](exercicio-12.py) | Apresentar o nome do vendedor e o total vendido por ele, do maior para o menor. |

## Como executar

```bash
python exercicio-01.py
```
