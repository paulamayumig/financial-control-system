from datetime import datetime

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
