from src.storage import carregar_dados


def test_carregar_dados(tmp_path):

    arquivo = tmp_path / "dados.json"

    dados = [
        {
            "tipo": "Receita",
            "valor": 100
        }
    ]

    arquivo.write_text('''[
        {
            "tipo": "Receita",
            "valor": 100
        }
    ]''')

    resultado = carregar_dados(arquivo)

    assert resultado == dados