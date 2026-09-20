import json
from datetime import datetime

ARQUIVO = "data/transactions.json"


def carregar_dados(ARQUIVO):

    with open(ARQUIVO, "r") as arquivo:
        return json.load(arquivo)


def salvar_dados(ARQUIVO, dados):

    with open(ARQUIVO, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)


dados = carregar_dados(ARQUIVO)


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


def pedir_valor() -> float:

    while True:

        try:
            valor = float(input("Valor: "))

            if valor <= 0:
                print("Valor inválido! Digite um valor acima de 0.")
                continue

            return valor

        except ValueError:
            print("Valor inválido. Digite um número válido.")


def pedir_texto(mensagem: str) -> str:

    while True:

        texto = input(mensagem).strip()

        if texto == "":
            print("Este campo não pode ficar vazio.")
            continue

        return texto


def pedir_data() -> str:

    while True:

        data = input("Data (DD/MM/AAAA): ")

        try:
            datetime.strptime(data, "%d/%m/%Y")
            return data

        except ValueError:
            print("Data inválida. Digite uma data válida no formato DD/MM/AAAA.")


def pedir_mes_ano():

    while True:

        mes = input("Digite o mês (MM): ")

        if not mes.isdigit() or len(mes) != 2 or not 1 <= int(mes) <= 12:
            print("Mês inválido. Digite um mês entre 01 e 12.")
            continue

        break

    while True:

        ano = input("Digite o ano (AAAA): ")

        if not ano.isdigit() or len(ano) != 4:
            print("Ano inválido. Digite o ano com 4 números.")
            continue

        break

    return mes, ano


def cadastrar(tipo: str, valor: float, categoria: str, data: str, descricao: str) -> None:

    registro = {
        "tipo": tipo,
        "valor": valor,
        "categoria": categoria,
        "data": data,
        "descricao": descricao
    }

    dados.append(registro)

    salvar_dados(ARQUIVO, dados)


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


while True:

    menu()

    escolha = input("Escolha uma opção: ")

    if escolha == "1":

        valor = pedir_valor()

        categoria = pedir_texto("Categoria: ")

        data = pedir_data()

        descricao = pedir_texto("Descrição: ")

        cadastrar("Receita", valor, categoria, data, descricao)


    elif escolha == "2":

        valor = pedir_valor()

        categoria = pedir_texto("Categoria: ")

        data = pedir_data()

        descricao = pedir_texto("Descrição: ")

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

