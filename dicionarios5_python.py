d1 = {
    "str" : "Valor",
    123 : "Outro valor",
    (1,2,3,4,5) : "Tupla"
}

print(d1)

del d1["str"] #Deletar um valor

print(d1)
print(len(d1)) #quantos valores têm no dicionário