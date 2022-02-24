perguntas = {
    "Pergunta 1" : {
        "Pergunta": "Quanto é 2+2?",
        "respostas": {"a":"1", "b":"4", "c":"5"},
        "resposta_certa:": "b",

    },
    "Pergunta 2": {
        "Pergunta": "Quanto é 3*2?",
        "respostas": {"a": "4", "b": "10", "c": "6"},
        "resposta_certa:": "c",

    },
}
print()

respostas_certas = 0
for pkey, pvalue in perguntas.items():
    print(f'{pkey}:{pvalue["Pergunta"]}')
    print("Respostas")

    for rkey, rvalue in pvalue["respostas"].items():
        print(f'[{rkey}]:{rvalue}')


    print()
    resposta_usuario = input("Sua resposta: ")
    print()

    if resposta_usuario == pvalue["resposta_certa:"]:
        print("Você acertou!")
        respostas_certas +=1
    else:
        print("Você errou!")

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100

print(f'Você acertou {respostas_certas} respostas')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%')
        
    else:
        print("Você errou!")

qtd_perguntas = len(perguntas)
porcentagem_acerto = respostas_certas / qtd_perguntas * 100  #conversão em porcentagem

print(f'Você acertou {respostas_certas} respostas')
print(f'Sua porcentagem de acerto foi {porcentagem_acerto}%')
        
        
