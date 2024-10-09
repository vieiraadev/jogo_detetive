import random

personagens = [
    "João", "Alexandre", "Ana", "Beatriz", 
    "Gabriel", "Marcos", "Fernanda"
]

cenarios_de_morte = {
    "Jardim": [
        "foi encontrado(a) morto(a) no jardim, às 19:30 horas.",
        [
            "Se {suspeito1} estava no jardim, então ele é inocente.",
            "Se {suspeito2} não estava no jardim, então {suspeito3} e {suspeito4} estavam juntos em outro lugar.",
            "Se {suspeito5} estava no jardim e não viu Fernanda, então ele é o suspeito.",
            "Se {suspeito6} estava na sala de estar, então ele não estava no jardim.",
            "Se {suspeito4} estava cuidando das plantas, então ela não pode ser a assassina.",
            "Se {suspeito3} estava com {suspeito2} na sala, então eles não estavam no jardim.",
            "Se {suspeito1} viu alguém no jardim, e essa pessoa não for {suspeito5}, então {suspeito1} é o suspeito."
        ]
    ],
    "Sala de Estar": [
        "foi encontrado(a) morto(a) na sala de estar, às 20:00 horas.",
        [
            "Se {suspeito1} estava na sala de estar, então ele não pode ser o assassino.",
            "Se {suspeito2} estava na cozinha, então {suspeito3} e {suspeito4} estavam na sala.",
            "Se {suspeito5} estava na sala e não viu ninguém, então ele é um suspeito.",
            "Se {suspeito6} estava no convés, então ele não estava na sala.",
            "Se {suspeito4} estava conversando com {suspeito3}, então eles não eram cúmplices.",
            "Se {suspeito2} estava na sala, então ela não pode ser a assassina.",
            "Se {suspeito1} ouviu um barulho, então ele pode ter visto o assassinato."
        ]
    ],
    "Cozinha": [
        "foi encontrado(a) morto(a) na cozinha, às 21:15 horas.",
        [
            "Se {suspeito1} estava na cozinha, então ele é inocente.",
            "Se {suspeito2} estava preparando o jantar, então ele não pode ser o assassino.",
            "Se {suspeito3} estava na sala, então ele não estava na cozinha.",
            "Se {suspeito4} viu a vítima, então ele deve ser interrogado.",
            "Se {suspeito5} estava em outra área, então ele não é suspeito.",
            "Se {suspeito6} não tinha motivos, então ele não pode ser o culpado.",
            "Se {suspeito1} tem um álibi, então ele é inocente."
        ]
    ],
    "Piscina": [
        "foi encontrado(a) afogado(a) na piscina, às 22:30 horas.",
        [
            "Se {suspeito1} estava na piscina, então ele é inocente.",
            "Se {suspeito2} não estava lá, então {suspeito3} e {suspeito4} estavam próximos.",
            "Se {suspeito5} viu a vítima antes do incidente, ele deve ser interrogado.",
            "Se {suspeito6} estava no bar, então ele não estava na piscina.",
            "Se {suspeito1} estava tomando sol, então ele não é o assassino.",
            "Se {suspeito2} não ouviu gritos, então ele não pode ser o culpado.",
            "Se {suspeito3} estava com {suspeito4}, então eles são inocentes."
        ]
    ],
    "Cabine de Comando": [
        "foi encontrado(a) morto(a) na cabine de comando, às 23:00 horas.",
        [
            "Se {suspeito1} estava na cabine, então ele é inocente.",
            "Se {suspeito2} estava no convés, então ele não estava na cabine.",
            "Se {suspeito3} estava fora da cabine, então ele não é o assassino.",
            "Se {suspeito4} estava lá e viu algo, ele deve ser interrogado.",
            "Se {suspeito5} estava com {suspeito6}, então eles são inocentes.",
            "Se {suspeito1} ouviu uma discussão, então ele é uma testemunha chave.",
            "Se {suspeito2} não estava lá, então ele pode ser suspeito."
        ]
    ],
    "Suíte": [
        "foi encontrado(a) morto(a) na suíte, às 00:30 horas.",
        [
            "Se {suspeito1} estava na suíte, então ele é inocente.",
            "Se {suspeito2} estava no bar, então ele não estava na suíte.",
            "Se {suspeito3} entrou e saiu rapidamente, ele deve ser interrogado.",
            "Se {suspeito4} viu alguém, então ele pode ser um testemunho importante.",
            "Se {suspeito5} não tinha motivos, então ele não pode ser o culpado.",
            "Se {suspeito6} estava com {suspeito1}, então eles são inocentes.",
            "Se {suspeito2} foi visto na área, então ele é suspeito."
        ]
    ],
    "Sauna": [
        "foi encontrado(a) inconsciente na sauna, às 17:00 horas.",
        [
            "Se {suspeito1} estava na sauna, então ele é inocente.",
            "Se {suspeito2} estava na sala de estar, então ele não estava na sauna.",
            "Se {suspeito3} entrou e não viu ninguém, ele deve ser interrogado.",
            "Se {suspeito4} estava esperando para entrar, então ele não pode ser o assassino.",
            "Se {suspeito5} não ouviu nada, então ele não é o culpado.",
            "Se {suspeito6} estava com {suspeito1}, então eles são inocentes.",
            "Se {suspeito2} estava lá, então ele pode ser um suspeito."
        ]
    ],
    "Deck": [
        "foi encontrado(a) caindo do deck, às 15:00 horas.",
        [
            "Se {suspeito1} estava no deck, então ele é inocente.",
            "Se {suspeito2} estava jogando, então ele não é o assassino.",
            "Se {suspeito3} estava em outro lugar, então ele não pode ser culpado.",
            "Se {suspeito4} viu a queda, ele deve ser interrogado.",
            "Se {suspeito5} estava com {suspeito6}, então eles são inocentes.",
            "Se {suspeito1} ouviu algo, então ele é uma testemunha chave.",
            "Se {suspeito2} estava lá, então ele pode ser suspeito."
        ]
    ],
    "Enfermaria": [
        "foi encontrado(a) morto(a) na enfermaria, às 16:00 horas.",
        [
            "Se {suspeito1} estava na enfermaria, então ele é inocente.",
            "Se {suspeito2} estava em outro lugar, então ele não pode ser o assassino.",
            "Se {suspeito3} entrou e não viu ninguém, ele deve ser interrogado.",
            "Se {suspeito4} estava esperando para ser atendido, então ele não pode ser o culpado.",
            "Se {suspeito5} não ouviu nada, então ele não é culpado.",
            "Se {suspeito6} estava com {suspeito1}, então eles são inocentes.",
            "Se {suspeito2} estava na área, então ele pode ser suspeito."
        ]
    ],
    "Sala de Jogos": [
        "foi encontrado(a) morto(a) na sala de jogos, às 14:00 horas.",
        [
            "Se {suspeito1} estava na sala de jogos, então ele é inocente.",
            "Se {suspeito2} estava jogando com {suspeito3}, então eles não são cúmplices.",
            "Se {suspeito4} saiu rapidamente, ele deve ser interrogado.",
            "Se {suspeito5} viu algo, então ele é um testemunho importante.",
            "Se {suspeito6} estava esperando, então ele não pode ser o culpado.",
            "Se {suspeito1} estava com {suspeito2}, então eles são inocentes.",
            "Se {suspeito3} estava na área, então ele pode ser suspeito."
        ]
    ]
}

def sortear_assassino(personagens):
    assassino = random.choice(personagens)
    vitima_suspeita = random.choice([p for p in personagens if p != assassino])
    return assassino, vitima_suspeita

def listar_suspeitos(personagens, morto):
    suspeitos = [p for p in personagens if p != morto]
    print("\n" + "-" * 50)
    print("Lista de Suspeitos:")
    for suspeito in suspeitos:
        print(f"{suspeito}")
        print('-' * 50)
    return suspeitos

def gerar_dica(assassino, suspeitos, titulo_cenario):
    random_suspects = random.sample(suspeitos, min(len(suspeitos), 7))
    descricao_cenario = cenarios_de_morte[titulo_cenario][0]
    dicas_base = cenarios_de_morte[titulo_cenario][1]
    dicas_formatadas = []
    
    for base in dicas_base:
        dica_formatada = base.format(
            suspeito1=random_suspects[0] if len(random_suspects) > 0 else "",
            suspeito2=random_suspects[1] if len(random_suspects) > 1 else "",
            suspeito3=random_suspects[2] if len(random_suspects) > 2 else "",
            suspeito4=random_suspects[3] if len(random_suspects) > 3 else "",
            suspeito5=random_suspects[4] if len(random_suspects) > 4 else "",
            suspeito6=random_suspects[5] if len(random_suspects) > 5 else "",
            suspeito7=random_suspects[6] if len(random_suspects) > 6 else ""
        )
        dicas_formatadas.append(dica_formatada)
    return dicas_formatadas, descricao_cenario

def boas_vindas():
    print("+" + "-" * 48 + "+")
    print("|" + " " * 48 + "|")
    print("|" + " " * 10 + "Seja Bem Vindo(a)" + " " * 10 + "|")
    print("|" + " " * 10 + "Lancha de Luxo “Oásis do Mar”" + " " * 10 + "|")
    print("|" + " " * 48 + "|")
    print("+" + "-" * 48 + "+")

def placar_total_acumulado(pontuacao_total):
    print("+" + "-" * 48 + "+")
    print("|" + " " * 48 + "|")
    print(f"|{' Placard Total Acumulado ':^48}|")
    print("|" + " " * 48 + "|")
    print(f"|{' Total de Pontos: ' + str(pontuacao_total):^48}|")
    print("|" + " " * 48 + "|")
    print("+" + "-" * 48 + "+")

def jogo_detetive():
    pontuacao_total = 0

    boas_vindas() 

    while True:
        print("\n" + "-" * 50)
        print("Escolha um cenário de morte:")
        for i, cenario in enumerate(cenarios_de_morte.keys(), start=1):
            print(f"{i}. {cenario}")
        
        escolha = int(input("Digite o número do cenário que deseja escolher: ")) - 1
        titulo_cenario = list(cenarios_de_morte.keys())[escolha]

        assassino, vitima_suspeita = sortear_assassino(personagens)
        morto = random.choice([p for p in personagens if p != assassino])
        descricao_cenario = cenarios_de_morte[titulo_cenario][0]
        
        print(f"\n{'-' * 50}")
        print(f"Vítima: {morto}")
        print(f"Local: {titulo_cenario}")
        print(f"Horário: {descricao_cenario.split(', ')[-1]}")
        print(f"{'-' * 50}")
        
        suspeitos = listar_suspeitos(personagens, morto)
        
        dicas, descricao = gerar_dica(assassino, suspeitos, titulo_cenario)
        pontos = 7  

        for i, dica in enumerate(dicas):
            print(f"\nDica {i+1}: {dica}")
            tentativa = input("Deseja adivinhar quem é o assassino(a)? (S/N): ").lower()
            
            if tentativa == 's':
                palpite = input("Quem é o assassino?: ")
                if palpite == assassino:
                    print(f"Você acertou! O assassino é {assassino}.")
                    print(f"Você ganhou {pontos} pontos!")
                    break
                else:
                    print("Palpite incorreto! Tente novamente com mais dicas.")
                    pontos -= 1
            else:
                print(f"Você escolheu continuar. Vamos para a próxima dica.\n")
        
        print(f"\nO jogo terminou. O assassino era {assassino}.")
        print(f"Seu placar final é: {pontos} pontos.")
        pontuacao_total += pontos  

        placar_total_acumulado(pontuacao_total)

        jogar_novamente = input("Deseja jogar novamente? (S/N): ").lower()
        if jogar_novamente != 's':
            print("Obrigado por jogar!")
            break

jogo_detetive()