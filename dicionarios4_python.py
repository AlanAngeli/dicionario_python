d1 = {
    "str" : "Valor",
    123 : "Outro valor",
    (1,2,3,4,5) : "Tupla"
}

d1.update({"nova_chave" : "novo_valor"})

if d1.get("nova_chave") is not None:
    print(d1.get("nova_chave"))

print(123)