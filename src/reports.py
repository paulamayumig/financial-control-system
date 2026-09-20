#ARQUIVO PARA RELATÓRIOS


def consultar(dados) -> None:

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


def filtrar_tipo(dados) -> None:

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


def filtrar_categoria(dados) -> None:

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


def filtrar_mes(dados) -> None:

    mes, ano = pedir_mes_ano()

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


def filtrar(dados) -> None:

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
            filtrar_tipo(dados)

        elif escolha == "2":
            filtrar_categoria(dados)

        elif escolha == "3":
            filtrar_mes(dados)

        elif escolha == "0":
            break

        else:
            print("Opção inválida.")


def relatorio_mensal(dados) -> None:

    mes, ano = pedir_mes_ano()

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