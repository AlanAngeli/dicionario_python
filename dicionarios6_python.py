d1 = {
    "Chave1" : "Valor",
    "Chave2" : "Segundo Valor",
    "Chave3" : "Terceiro Valor",
}

for variavel_valores in d1.values():
    print(variavel_valores)

print()

for variavel_itens in d1.items():
    print(variavel_itens)

print()

for variavel_itens in d1.items():
    print(variavel_itens[0], variavel_itens[1])

    
##ou:


print()

for chave, valor in d1.items():
    print(chave, valor)