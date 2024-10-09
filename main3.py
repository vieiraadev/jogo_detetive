import datetime
import random

verde = "\033[92m"
reset = "\033[0m"

personagens_lista = [
    'Alessandro Rossi - 45 anos - Ambicioso e Carismático',
    'Lucca Romano - 38 anos - Racional e Meticuloso',
    'Sofia Bellini - 36 anos - Criativa e Ousada',
    'Chiara Vitale - 34 anos - Empática e Carismática',
    'Bianca Moretti - 42 anos - Pragmática e Racional',
    'Matteo Ferraro - Criativo e Amigável',
    'Elena Capello - Amigável e Atenta'
]
cenarios_lista = [
    "1. Crime no Salão",
    "2. Cozinha da Discórdia",
    "3. Quarto do Suspeito",
    "4. Deck da Verdade",
    "5. Corredor Sombrio",
    "6. Sala de Entretenimento",
    "7. Momento da Festa",
    "8. Conversa Silenciosa",
    "9. Encontro Noturno",
    "10. Última Mensagem"
]

def bem_vindo():
    print(f"{verde}" + "-"*60)
    print(f"{verde}|{'':^58}|")
    print(f"{verde}|{'BEM VINDO AO JOGO!':^58}|")
    print(f"{verde}|{'':^58}|")
    print(f"{verde}|{'Prepare-se para desvendar o mistério':^58}|")
    print(f"{verde}|{'que te aguarda!':^58}|")
    print(f"{verde}|{'':^58}|")
    print(f"{verde}" + "-"*60 + f"{reset}")

def descricao():
    print(f"{verde}" + "-"*60)
    print(f"{verde}|{'DESCRIÇÃO DO CASO':^58}|")
    print(f"{verde}" + "-"*60)
    print(f"{verde}|{'7 milionários se reúnem em uma casa luxuosa':^58}|")
    print(f"{verde}|{'em uma ilha para uma celebração de negócios.':^58}|")
    print(f"{verde}|{'Durante a festa, um dos sócios é encontrado morto.':^58}|")
    print(f"{verde}|{'Agora, todos os presentes têm motivos ocultos e':^58}|")
    print(f"{verde}|{'segredos que podem levar a uma investigação profunda.':^58}|")
    print(f"{verde}|{'Seu dever é investigar, encontrar o assassino e a arma.':^58}|")
    print(f"{verde}|{'Contamos com você para desvendar este mistério!':^58}|")
    print(f"{verde}" + "-"*60 + f"{reset}")

def personagens():
    print(f"{verde}" + "-"*60)
    print(f"{verde}|{'PERSONAGENS':^58}|")
    print(f"{verde}" + "-"*60)
    for i, personagem in enumerate(personagens_lista, start=1):
        print(f"{verde}|{f'{i}. {personagem}':<58}|")
    print(f"{verde}" + "-"*60 + f"{reset}")

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

def cenarios():
    print(f"{verde}" + "-"*60)
    print(f"{verde}|{'CENÁRIOS DISPONÍVEIS':^58}|")
    print(f"{verde}" + "-"*60)
    for cenario in cenarios_lista:
        print(f"{verde}|{cenario:<58}|")
    print(f"{verde}" + "-"*60 + f"{reset}")

def escolher_cenario():
    while True:
        try:
            escolha = int(input(f"{verde}Escolha um cenário (1-10): "))
            if 1 <= escolha <= 10:
                print(f"{verde}Você escolheu: {cenarios_lista[escolha - 1]}")
                personagem_morto = random.choice(personagens_lista)
                print(f"{verde}" + "-"*60)
                print(f"{verde}|{'ATENÇÃO!':^58}|")
                print(f"{verde}|{f'{personagem_morto.split(" - ")[0]} foi encontrado morto!':^58}|")
                print(f"{verde}" + "-"*60)
                break
            else:
                print("Por favor, escolha um número entre 1 e 10.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

bem_vindo()
print("\n" * 2)

descricao()
print("\n" * 2)

personagens()
print("\n" * 2)

exibir_planta()
print("\n" * 2)

cenarios()
print("\n" * 2)

escolher_cenario()
