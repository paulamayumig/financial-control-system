dados = []


def menu() -> None:
    print('''
MENU PRINCIPAL

1 - Cadastrar receita
2 - Cadastrar despesa
3 - Consultar informações
4 - Ver saldo
5 - Filtrar dados
6 - Relatório mensal
0 - Sair
''')


def cadastrar(tipo: str, valor: float, categoria: str, data: str, descricao: str) -> None:
    registro = {
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria,
        "data": data,
        "descricao": descricao
    }

    dados.append(registro)


def calcular_saldo() -> float:
    saldo = 0

    for registro in dados:
        if registro["tipo"] == "Receita":
            saldo += registro["valor"]

        elif registro["tipo"] == "Despesa":
            saldo -= registro["valor"]

    return saldo


def consultar() -> None:
    if len(dados) == 0:
        print("Nenhuma movimentação cadastrada.")
        return

    print("\n===== MOVIMENTAÇÕES =====")

    for registro in dados:
        print(f'''
Tipo: {registro["tipo"]}
Valor: R$ {registro["valor"]:.2f}
Categoria: {registro["categoria"]}
Data: {registro["data"]}
Descrição: {registro["descricao"]}
------------------------
''')


def filtrar_tipo() -> None:
    tipo = input("Digite o tipo (Receita ou Despesa): ")

    encontrou = False

    for registro in dados:
        if registro["tipo"].lower() == tipo.lower():
            print(f'''
Tipo: {registro["tipo"]}
Valor: R$ {registro["valor"]:.2f}
Categoria: {registro["categoria"]}
Data: {registro["data"]}
Descrição: {registro["descricao"]}
------------------------
''')
            encontrou = True

    if not encontrou:
        print("Nenhuma movimentação encontrada.")


def filtrar_categoria() -> None:
    categoria = input("Digite a categoria: ")

    encontrou = False

    for registro in dados:
        if registro["categoria"].lower() == categoria.lower():
            print(f'''
Tipo: {registro["tipo"]}
Valor: R$ {registro["valor"]:.2f}
Categoria: {registro["categoria"]}
Data: {registro["data"]}
Descrição: {registro["descricao"]}
------------------------
''')
            encontrou = True

    if not encontrou:
        print("Nenhuma movimentação encontrada.")


def filtrar_mes() -> None:
    mes = input("Digite o mês (MM): ")
    ano = input("Digite o ano (AAAA): ")

    encontrou = False

    for registro in dados:
        data = registro["data"]

        if len(data) == 10 and data[3:5] == mes and data[6:10] == ano:
            print(f'''
Tipo: {registro["tipo"]}
Valor: R$ {registro["valor"]:.2f}
Categoria: {registro["categoria"]}
Data: {registro["data"]}
Descrição: {registro["descricao"]}
------------------------
''')
            encontrou = True

    if not encontrou:
        print("Nenhuma movimentação encontrada.")


def filtrar() -> None:
    while True:
        print('''
===== FILTRAR DADOS =====

1 - Por tipo
2 - Por categoria
3 - Por mês
0 - Voltar
''')

        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            filtrar_tipo()

        elif escolha == "2":
            filtrar_categoria()

        elif escolha == "3":
            filtrar_mes()

        elif escolha == "0":
            break

        else:
            print("Opção inválida.")


def relatorio_mensal() -> None:
    mes = input("Digite o mês (MM): ")
    ano = input("Digite o ano (AAAA): ")

    total_receitas = 0
    total_despesas = 0

    for registro in dados:
        data = registro["data"]

        if len(data) == 10 and data[3:5] == mes and data[6:10] == ano:

            if registro["tipo"] == "Receita":
                total_receitas += registro["valor"]

            elif registro["tipo"] == "Despesa":
                total_despesas += registro["valor"]

    saldo = total_receitas - total_despesas

    print(f'''
===== RELATÓRIO MENSAL =====

Mês: {mes}/{ano}

Total de receitas: R$ {total_receitas:.2f}
Total de despesas: R$ {total_despesas:.2f}
Saldo: R$ {saldo:.2f}
''')


while True:
    menu()

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        valor = float(input("Valor da receita: "))
        categoria = input("Categoria: ")
        data = input("Data (DD/MM/AAAA): ")
        descricao = input("Descrição: ")

        cadastrar("Receita", valor, categoria, data, descricao)

    elif escolha == "2":
        valor = float(input("Valor da despesa: "))
        categoria = input("Categoria: ")
        data = input("Data (DD/MM/AAAA): ")
        descricao = input("Descrição: ")

        cadastrar("Despesa", valor, categoria, data, descricao)

    elif escolha == "3":
        consultar()

    elif escolha == "4":
        saldo = calcular_saldo()
        print(f"Saldo atual: R$ {saldo:.2f}")

    elif escolha == "5":
        filtrar()

    elif escolha == "6":
        relatorio_mensal()

    elif escolha == "0":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")