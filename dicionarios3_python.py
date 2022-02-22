d1 = {
    "str" : "Alan Angeli",
    123: "Outro Valor",
    (1,2,3,4,5) : "Tupla",

}

d1["naoexiste"] = "Agora existe"
if "naoexiste" in d1:
    print(d1["naoexiste"])

####outra forma:

d1["nomedachave"] = "Nova chave"
if d1.get("nomedachave"):
    print(d1.get("nomedachave"))