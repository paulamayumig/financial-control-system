dados = []


def menu() -> None:
    print('''
MENU PRINCIPAL

1 - Cadastrar receita
2 - Cadastrar despesa
3 - Consultar informações
0 - Sair
''')


def cadastrar(tipo: str, valor: float) -> None:
    registro = {
        "tipo": tipo,
        "valor": valor
    }

    dados.append(registro)


def consultar() -> None:
    print(dados)


while True:
    menu()

    escolha = int(input("Escolha uma opção: "))

    if escolha == 1:
        valor = float(input("Valor da receita: "))
        cadastrar("Receita", valor)

    elif escolha == 2:
        valor = float(input("Valor da despesa: "))
        cadastrar("Despesa", valor)

    elif escolha == 3:
        consultar()

    elif escolha == 0:
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")