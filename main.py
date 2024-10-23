import datetime
import random

verde = "\033[92m"
reset = "\033[0m"

personagens_lista = [
    'Alessandro Rossi',
    'Lucca Romano',
    'Sofia Bellini',
    'Chiara Vitale',
    'Bianca Moretti',
    'Matteo Ferraro',
    'Elena Capello'
]

personagens_descricao = [
    '45 anos - Ambicioso e Carismático',
    '38 anos - Racional e Meticuloso',
    '36 anos - Criativa e Ousada',
    '34 anos - Empática e Carismática',
    '42 anos - Pragmática e Racional',
    '40 anos - Criativo e Amigável',
    '28 anos - Amigável e Atenta',
]

cenarios_lista = [
    "Crime no Salão",
    "Cozinha da Discórdia",
    "Quarto do Suspeito",
    "Deck da Verdade",
    "Corredor Sombrio",
    "Sala de Entretenimento",
    "Momento da Festa",
    "Conversa Silenciosa",
    "Encontro Noturno",
    "Última Mensagem"
]

def bem_vindo():
    print(f"{verde}" + "-" * 60)
    print(f"{verde}|{'':^58}|")
    print(f"{verde}|{'BEM VINDO AO JOGO!':^58}|")
    print(f"{verde}|{'':^58}|")
    print(f"{verde}|{'Prepare-se para desvendar o mistério':^58}|")
    print(f"{verde}|{'que te aguarda!':^58}|")
    print(f"{verde}|{'':^58}|")
    print(f"{verde}" + "-" * 60 + f"{reset}")

def descricao():
    print(f"{verde}" + "-" * 60)
    print(f"{verde}|{'DESCRIÇÃO DO CASO':^58}|")
    print(f"{verde}" + "-" * 60)
    print(f"{verde}|{'7 milionários se reúnem em uma casa luxuosa':^58}|")
    print(f"{verde}|{'em uma ilha para uma celebração de negócios.':^58}|")
    print(f"{verde}|{'Durante a festa, um dos sócios é encontrado morto.':^58}|")
    print(f"{verde}|{'Agora, todos os presentes têm motivos ocultos e':^58}|")
    print(f"{verde}|{'segredos que podem levar a uma investigação profunda.':^58}|")
    print(f"{verde}|{'Seu dever é investigar, encontrar o assassino e a arma.':^58}|")
    print(f"{verde}|{'Contamos com você para desvendar este mistério!':^58}|")
    print(f"{verde}" + "-" * 60 + f"{reset}")

def personagens():
    print(f"{verde}" + "-" * 60)
    print(f"{verde}|{'PERSONAGENS':^58}|")
    print(f"{verde}" + "-" * 60)
    for i, (personagem, descricao) in enumerate(zip(personagens_lista, personagens_descricao), start=1):
        print(f"{verde}|{f'{i}. {personagem} - {descricao}':<58}|")
    print(f"{verde}" + "-" * 60 + f"{reset}")

def exibir_planta():
    data_atual = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    planta = [
        "  -----------------------------------------------------------",
        f"| PLANTA:                                 {data_atual} |",
        "  -----------------------------------------------------------",
        "                                                            ",
        "                                                            ",
        "                           ENTRADA                          ",
        "--------------------------|       |-------------------------",
        "|                                                           |",
        "|                                                           |",
        "|                                                           |",
        "|                      SALÃO PRINCIPAL                      |",
        "|                                                           |",
        "|                                                           |",
        "|                                                           |",
        "|-------------------------|       |-------------------------|",
        "|                    |                                      |",
        "|   SALA DE ESTAR            CORREDOR CENTRAL               |",
        "|                    |                                      |",
        "|--------------------|-----------------|         |----------|",
        "|                    |                 |         |          |",
        "|  COZINHA GOURMET                     |           QUARTO 1 |",
        "|                    |                 |         |          |",
        "|--------------------|                           |----------|",
        "|                    |                           |          |",
        "|                                      |         | QUARTO 2 |",
        "|  SALA DE           |                 |                    |",
        "|  ENTRETENIMENTO    |                 |         |----------|",
        "|                    |                 |         |          |",
        "|--------------------|-----------------|           QUARTO 3 |",
        "|                    |                 |         |          |",
        "|                    |                           |----------|",
        "|     QUARTO 6                                              |",
        "|                    |                 |         | QUARTO 4 |",
        "|--------------------|-----------------|         |          |",
        "|                    |                           |----------|",
        "|                    |                                      |",
        "|                    |                 |         | QUARTO 5 |",
        "|     SUITE          |                 |         |          |",
        "|     MASTER         |                 |         |----------|",
        "|                    |                 |                    |",
        "|-------    ---------|-----------------|                    |",
        "|                                                           |",
        "|                        DECK EXTERNO                       |",
        "-------------------------------------------------------------"
    ]

    for linha in planta:
        print(f"{verde}{linha}{reset}")

def arma(vitima):
    green = "\033[92m"
    reset = "\033[0m" 
    gun_art = r"""
|-----------------------------------------------------------------------|
|   ____________________________________         ---        __          |
|  |                                    |===--  --    --   --    --     |
|  |       ____________________________ |        ---               --   | 
|  |       |  |                                                         |
|  |     |____|                                                         |  
|  |     |                                                              |
|  |     |                                                              |
|  |     |                       A VÍTIMA FOI: {vitima}                 |
|  |     |                                                              |
|  |     |                                                              |
|  |     |                                                              |
|  |     |                                                              |
|  |_____|                                                              |
|-----------------------------------------------------------------------|
"""
    print(green + gun_art.replace("{vitima}", vitima) + reset)

def cenarios():
    print(f"{verde}" + "-" * 60)
    print(f"{verde}|{'CENÁRIOS DISPONÍVEIS':^58}|")
    print(f"{verde}" + "-" * 60)
    for i, cenario in enumerate(cenarios_lista, start=1):
        print(f"{verde}|{f'{i}. {cenario}':<58}|")
    print(f"{verde}" + "-" * 60 + f"{reset}")

def gerar_dicas(cenario, personagens_lista):
    dicas_por_cenario = {
        "Crime no Salão": [
            "Se {suspeito} estava no salão, então ele é inocente.",
            "Se {suspeito} estava conversando, então ele não pode ser o assassino.",
            "Se {suspeito} viu algo suspeito, ele deve ser interrogado.",
            "Se {suspeito} estava no banheiro, então ele não estava no salão.",
            "Se {suspeito} não tem um motivo, então ele é inocente.",
            "Se {suspeito} estava escondido, então ele pode ser suspeito.",
            "Se {suspeito} não ouviu nada, então ele pode ser culpado."
        ],
        "Cozinha da Discórdia": [
            "Se {suspeito} estava na cozinha, então ele é inocente.",
            "Se {suspeito} estava cozinhando, então ele não pode ser o assassino.",
            "Se {suspeito} viu algo suspeito, ele deve ser interrogado.",
            "Se {suspeito} estava no salão, então ele não estava na cozinha.",
            "Se {suspeito} não tem um motivo, então ele é inocente.",
            "Se {suspeito} estava na despensa, então ele pode ser suspeito.",
            "Se {suspeito} não ouviu nada, então ele pode ser culpado."
        ],
        "Quarto do Suspeito": [
            "Se {suspeito} estava no quarto, então ele é inocente.",
            "Se {suspeito} estava dormindo, então ele não pode ser o assassino.",
            "Se {suspeito} viu algo suspeito, ele deve ser interrogado.",
            "Se {suspeito} estava na sala, então ele não estava no quarto.",
            "Se {suspeito} não tem um motivo, então ele é inocente.",
            "Se {suspeito} estava escondido, então ele pode ser suspeito.",
            "Se {suspeito} não ouviu nada, então ele pode ser culpado."
        ],
        "Deck da Verdade": [
            "Se {suspeito} estava no deck, então ele é inocente.",
            "Se {suspeito} estava olhando para o mar, então ele não pode ser o assassino.",
            "Se {suspeito} viu algo suspeito, ele deve ser interrogado.",
            "Se {suspeito} estava dentro da lancha, então ele não estava no deck.",
            "Se {suspeito} não tem um motivo, então ele é inocente.",
            "Se {suspeito} estava perto da saída, então ele pode ser suspeito.",
            "Se {suspeito} não ouviu nada, então ele pode ser culpado."
        ],
        "Corredor Sombrio": [
            "Se {suspeito} estava no corredor, então ele é inocente.",
            "Se {suspeito} estava passando, então ele não pode ser o assassino.",
            "Se {suspeito} viu algo suspeito, ele deve ser interrogado.",
            "Se {suspeito} estava em outro andar, então ele não estava no corredor.",
            "Se {suspeito} não tem um motivo, então ele é inocente.",
            "Se {suspeito} estava escondido, então ele pode ser suspeito.",
            "Se {suspeito} não ouviu nada, então ele pode ser culpado."
        ],
        "Sala de Entretenimento": [
            "Se {suspeito} estava na sala de entretenimento, então ele é inocente.",
            "Se {suspeito} estava assistindo TV, então ele não pode ser o assassino.",
            "Se {suspeito} viu algo suspeito, ele deve ser interrogado.",
            "Se {suspeito} estava no banheiro, então ele não estava na sala.",
            "Se {suspeito} não tem um motivo, então ele é inocente.",
            "Se {suspeito} estava lá, então ele pode ser suspeito.",
            "Se {suspeito} não ouviu nada, então ele pode ser culpado."
        ],
        "Momento da Festa": [
            "Se {suspeito} estava na festa, então ele é inocente.",
            "Se {suspeito} estava dançando, então ele não pode ser o assassino.",
            "Se {suspeito} viu algo suspeito, ele deve ser interrogado.",
            "Se {suspeito} estava no banheiro, então ele não estava na festa.",
            "Se {suspeito} não tem um motivo, então ele é inocente.",
            "Se {suspeito} estava se divertindo, então ele pode ser inocente.",
            "Se {suspeito} não ouviu nada, então ele pode ser culpado."
        ],
        "Conversa Silenciosa": [
            "Se {suspeito} estava em uma conversa, então ele é inocente.",
            "Se {suspeito} estava ouvindo, então ele não pode ser o assassino.",
            "Se {suspeito} viu algo suspeito, ele deve ser interrogado.",
            "Se {suspeito} estava no banheiro, então ele não estava na conversa.",
            "Se {suspeito} não tem um motivo, então ele é inocente.",
            "Se {suspeito} estava escondido, então ele pode ser suspeito.",
            "Se {suspeito} não ouviu nada, então ele pode ser culpado."
        ],
        "Encontro Noturno": [
            "Se {suspeito} estava no encontro, então ele é inocente.",
            "Se {suspeito} estava se divertindo, então ele não pode ser o assassino.",
            "Se {suspeito} viu algo suspeito, ele deve ser interrogado.",
            "Se {suspeito} estava no banheiro, então ele não estava no encontro.",
            "Se {suspeito} não tem um motivo, então ele é inocente.",
            "Se {suspeito} estava escondido, então ele pode ser suspeito.",
            "Se {suspeito} não ouviu nada, então ele pode ser culpado."
        ],
        "Última Mensagem": [
            "Se {suspeito} recebeu uma mensagem, então ele é inocente.",
            "Se {suspeito} estava respondendo, então ele não pode ser o assassino.",
            "Se {suspeito} viu algo suspeito, ele deve ser interrogado.",
            "Se {suspeito} estava no banheiro, então ele não estava enviando a mensagem.",
            "Se {suspeito} não tem um motivo, então ele é inocente.",
            "Se {suspeito} estava no quarto, então ele pode ser suspeito.",
            "Se {suspeito} não ouviu nada, então ele pode ser culpado."
        ],
    }

    return random.sample(dicas_por_cenario[cenario], 7)

def jogo():
    bem_vindo()
    descricao()
    personagens()

    cenarios()
    cenario_escolhido = int(input("Escolha um cenário (1-10): ")) - 1
    cenario = cenarios_lista[cenario_escolhido]

    vitima = random.choice(personagens_lista)
    personagens_lista.remove(vitima) 

    dicas = gerar_dicas(cenario, personagens_lista)
    arma(vitima)
    print(f"{verde}" + "-" * 60)
    print(f"{verde}|{'SUSPEITOS':^58}|")
    print(f"{verde}" + "-" * 60)
    for personagem in personagens_lista:
        print(f"{verde}|{personagem:<58}|")
    print(f"{verde}" + "-" * 60 + f"{reset}")

    pontos = 7
    for i, dica in enumerate(dicas):
        print(f"\nDica {i + 1}: {dica.format(suspeito=personagens_lista[0])}")
        print(f"{verde}1. Adivinhar\n2. Próxima dica\n3. Sair{reset}")

        escolha = input("Escolha uma opção: ")
        
        if escolha == "1":
            palpite = input("Quem você acha que é o assassino? ")
            if palpite.lower() == vitima.lower():
                print("Você acertou! O assassino é:", vitima)
                return
            else:
                print("Você errou! O assassino não é:", palpite)
                pontos -= 1
        
        elif escolha == "2":
            pontos -= 1
        
        elif escolha == "3":
            print("Saindo do jogo...")
            return
        
        print(f"Pontos restantes: {pontos}")
    
    print("Fim do jogo! A vítima foi:", vitima)

jogo()