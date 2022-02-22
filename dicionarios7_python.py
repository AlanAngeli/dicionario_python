"""

Criando dicionários dentro de dicionários

"""

clientes = {
    "Cliente_1" : {
        "Nome" : "Alan",
        "Sobrenome" : "Angeli",
    },
    "Cliente_2" : {
        "Nome" : "Eloisa",
        "Sobrenome" : "Estrela",
    },
}

for clientes_key, clientes_value in clientes.items():
    print(f'Exibindo {clientes_key}')
    for dados_key, dados_value in clientes_value.items():
        print(f'\t{dados_key} = {dados_value}') #\t é tab

