#ARQUIVO PARA TRANSFERENCIAS

def cadastrar(tipo: str, valor: float, categoria: str, data: str, descricao: str, dados, ARQUIVO) -> None:

    registro = {
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria,
        "data": data,
        "descricao": descricao
    }

    dados.append(registro)

    salvar_dados(ARQUIVO, dados)


def calcular_saldo(dados) -> float:

    saldo = 0

    for registro in dados:

        if registro["tipo"] == "Receita":
            saldo += registro["valor"]

        elif registro["tipo"] == "Despesa":
            saldo -= registro["valor"]

    return saldo

