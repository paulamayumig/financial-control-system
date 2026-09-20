#ARQUIVO PARA FUNÇOES JSON E CONEXÕES

import json 

def carregar_dados(ARQUIVO):

    with open(ARQUIVO, "r") as arquivo:
        return json.load(arquivo)


def salvar_dados(ARQUIVO, dados):

    with open(ARQUIVO, "w") as arquivo:
        json.dump(dados, arquivo, indent=4)
