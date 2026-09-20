# Financial Control System

Sistema de controle financeiro desenvolvido em Python para cadastro e gerenciamento de receitas e despesas por meio do terminal.

O projeto foi desenvolvido com foco em prática de programação, organização de código e construção de um projeto completo para portfólio, utilizando persistência de dados em JSON, validação de entradas e separação do código em módulos.

## Funcionalidades

* Cadastro de receitas
* Cadastro de despesas
* Categorização das movimentações
* Registro de data e descrição
* Consulta de movimentações cadastradas
* Cálculo do saldo atual
* Filtro de movimentações por:

  * tipo
  * categoria
  * mês

* Relatório mensal com:

  * total de receitas
  * total de despesas
  * saldo do mês

* Persistência dos dados em arquivo JSON
* Validação dos valores informados
* Validação de datas
* Validação de mês e ano
* Validação de campos de texto
* Tratamento de entradas inválidas

## Tecnologias utilizadas

* **Python** — linguagem principal do projeto
* **JSON** — armazenamento e persistência dos dados
* **Git** — controle de versão
* **GitHub** — hospedagem e gerenciamento do projeto
* **pytest** — testes automatizados

## Estrutura do projeto

## Estrutura do projeto


financial-control-system/

│
├── src/
│   ├── main.py
│   ├── transactions.py
│   ├── reports.py
│   ├── storage.py
│   └── validators.py
│
├── data/
│   └── transactions.json
│
├── tests/
│   ├── test_reports.py
│   ├── test_transactions.py
│   ├── test_validators.py
│   └── test_storage.py
│
├── .gitignore
└── README.md



### Organização dos módulos

**main.py**

Responsável pelo fluxo principal do programa e pelo menu de interação com o usuário.

**transactions.py**

Contém as funções relacionadas às movimentações financeiras, como cadastro e cálculo do saldo.

**reports.py**

Responsável pela consulta, filtragem e geração de relatórios das movimentações.

**storage.py**

Responsável pela leitura e gravação dos dados no arquivo JSON.

**validators.py**

Contém as funções responsáveis pela validação das entradas fornecidas pelo usuário.

**data/transactions.json**

Arquivo utilizado para armazenar as movimentações cadastradas e manter os dados após o encerramento do programa.

**tests/**

Diretório destinado aos testes automatizados do projeto.

## Como executar

### 1. Clone o repositório

bash
git clone URL_DO_REPOSITORIO


### 2. Acesse a pasta do projeto

bash
cd financial-control-system


### 3. Crie um ambiente virtual

No Windows:

bash
python -m venv .venv


### 4. Ative o ambiente virtual

No PowerShell:

bash
.venv\Scripts\Activate.ps1


### 5. Instale as dependências

bash
pip install -r requirements.txt


### 6. Execute o programa

bash
python src/main.py


## Armazenamento dos dados

O sistema utiliza um arquivo JSON para armazenar as movimentações.

Cada movimentação possui as seguintes informações:

json
{
    "tipo": "Receita",
    "valor": 100.0,
    "categoria": "Salário",
    "data": "19/09/2026",
    "descricao": "Exemplo de receita"
}


O arquivo é carregado quando o programa é iniciado e atualizado sempre que uma nova movimentação é cadastrada.

A escolha do JSON foi feita para manter o projeto simples nesta etapa, permitindo trabalhar com persistência de dados sem a necessidade de configurar um banco de dados.

## Validação de dados

O sistema realiza verificações para evitar entradas inválidas, incluindo:

* valores que não sejam números;
* valores menores ou iguais a zero;
* datas inexistentes;
* formatos de data inválidos;
* meses fora do intervalo de 01 a 12;
* anos fora do formato esperado;
* campos de texto vazios.

Essas validações ajudam a evitar que dados inválidos sejam armazenados no sistema.

## Exemplo de uso

Ao iniciar o programa, o usuário encontra o menu principal:

text
MENU PRINCIPAL

1 - Cadastrar receita

2 - Cadastrar despesa

3 - Consultar informações

4 - Ver saldo

5 - Filtrar dados

6 - Relatório mensal

0 - Sair


A partir do menu, é possível cadastrar movimentações, consultar os dados armazenados, calcular o saldo, utilizar filtros e gerar um relatório mensal.

## Objetivos de aprendizado

Este projeto foi desenvolvido para praticar e consolidar conceitos de desenvolvimento em Python, incluindo:

* variáveis e tipos de dados;
* estruturas condicionais;
* estruturas de repetição;
* funções;
* listas e dicionários;
* manipulação de arquivos;
* leitura e escrita de JSON;
* tratamento de exceções;
* validação de dados;
* organização de código em módulos;
* importação entre arquivos Python;
* controle de versão com Git;
* testes automatizados.

## Próximas melhorias

Algumas funcionalidades podem ser adicionadas futuramente, conforme a evolução do projeto:

* melhorar a cobertura dos testes automatizados;
* adicionar novas formas de consulta e relatório;
* aprimorar a validação e organização dos dados;
* permitir edição e exclusão de movimentações;
* substituir o armazenamento em JSON por um banco de dados;
* desenvolver uma interface ou API em uma etapa futura.

## Status do projeto

**Em desenvolvimento.**

O projeto atualmente possui as principais funcionalidades de cadastro, consulta, filtragem, cálculo de saldo, relatório mensal, persistência em JSON, validação de entradas e organização do código em módulos.
