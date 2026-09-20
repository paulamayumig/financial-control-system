from src.reports import relatorio_mensal


def test_relatorio_mensal(capsys, monkeypatch):

    dados = [
        {
            "tipo": "Receita",
            "valor": 100,
            "categoria": "Salário",
            "data": "10/09/2026",
            "descricao": "Pagamento"
        },
        {
            "tipo": "Despesa",
            "valor": 30,
            "categoria": "Alimentação",
            "data": "15/09/2026",
            "descricao": "Almoço"
        },
        {
            "tipo": "Despesa",
            "valor": 50,
            "categoria": "Transporte",
            "data": "10/10/2026",
            "descricao": "Uber"
        }
    ]

    entradas = iter(["09", "2026"])

    monkeypatch.setattr("builtins.input", lambda _: next(entradas))

    relatorio_mensal(dados)

    resultado = capsys.readouterr().out

    assert "Total de receitas: R$ 100.00" in resultado
    assert "Total de despesas: R$ 30.00" in resultado
    assert "Saldo: R$ 70.00" in resultado