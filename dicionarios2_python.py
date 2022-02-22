dicionario = {1: "primeiro valor", 2: "segundo valor", 3: "terceiro valor"}
print(dicionario)
print(dicionario[3])
print()

dic2 = {
    "str" : "Valor",
    123: "Outro valor",
    (1,2,3,4,5) : "Tupla",
}

print(dic2)
print(dic2[1,2,3,4,5])
print(dic2[123])
print(dic2["str"])
