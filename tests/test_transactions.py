from src.transactions import calcular_saldo

def test_calcular_saldo():
    dados = [
        {
            "tipo": "Receita",
            "valor": 100,
            "categoria": "Salário",
            "data": "19/09/2026",
            "descricao": "Pagamento"
        },
        {
            "tipo": "Despesa",
            "valor": 30,
            "categoria": "Alimentação",
            "data": "19/09/2026",
            "descricao": "Almoço"
        }
    ]

    resultado = calcular_saldo(dados)

    assert resultado == 70

