import json
from datetime import datetime
from storage import carregar_dados, salvar_dados
from validators import pedir_data, pedir_mes_ano, pedir_texto, pedir_valor
from reports import consultar, filtrar_categoria, filtrar, filtrar_mes, filtrar_tipo, relatorio_mensal
from transactions import cadastrar, calcular_saldo

ARQUIVO = "data/transactions.json"


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







while True:

    menu()

    escolha = input("Escolha uma opção: ")

    if escolha == "1":

        valor = pedir_valor()

        categoria = pedir_texto("Categoria: ")

        data = pedir_data()

        descricao = pedir_texto("Descrição: ")

        cadastrar("Receita", valor, categoria, data, descricao, dados, ARQUIVO)


    elif escolha == "2":

        valor = pedir_valor()

        categoria = pedir_texto("Categoria: ")

        data = pedir_data()

        descricao = pedir_texto("Descrição: ")

        cadastrar("Despesa", valor, categoria, data, descricao, dados, ARQUIVO)


    elif escolha == "3":

        consultar(dados)


    elif escolha == "4":

        saldo = calcular_saldo(dados)

        print(f"Saldo atual: R$ {saldo:.2f}")


    elif escolha == "5":

        filtrar(dados)


    elif escolha == "6":

        relatorio_mensal(dados)


    elif escolha == "0":

        print("Programa encerrado.")
        break


    else:

        print("Opção inválida.")

