import datetime
import random
import time

verde = "\033[92m"
reset = "\033[0m"

# Lista de personagens
personagens_lista = [
    "Alessandro Rossi",
    "Lucca Romano",
    "Sofia Bellini",
    "Chiara Vitale",
    "Bianca Moretti",
    "Matteo Ferraro",
    "Elena Capello",
]

personagens_descricao = [
    "45 anos - Ambicioso e Carismático",
    "38 anos - Racional e Meticuloso",
    "36 anos - Criativa e Ousada",
    "34 anos - Empática e Carismática",
    "42 anos - Pragmática e Racional",
    "40 anos - Criativo e Amigável",
    "28 anos - Amigável e Atenta",
]


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
        "-------------------------------------------------------------",
    ]

    for linha in planta:
        print(f"{verde}{linha}{reset}")


# Lista de cenários
cenarios_lista = [
    "Crime no Salão",
    "Cozinha da Discórdia",
    "Quarto do Suspeito",
    "Deck da Verdade",
    "Corredor Sombrio",
]


# Funções do jogo
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
    for i, (personagem, descricao) in enumerate(
        zip(personagens_lista, personagens_descricao), start=1
    ):
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
        "-------------------------------------------------------------",
    ]

    for linha in planta:
        print(f"{verde}{linha}{reset}")


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
            "{suspeito} estava com uma arma.",
            "{suspeito} estava no quarto 5.",
            "Se {suspeito} estava na casa, então ele(a) estava na sala de estar.",
            "{assassino} estava fugindo da casa.",
            "{suspeito} estava dormindo.",
            "{suspeito} estava falando com o cozinheiro",
            "{suspeito} estava com uma acompanhante na sala de entretenimento",
            "{suspeito} estava no salão no momento da morte.",
            "{assassino} estava com sangue em suas roupas.",
            "{suspeito} estava tendo um coma alcoólico na suíte master",
        ],
        "Cozinha da Discórdia": [
            "{suspeito} estava na piscina do deck externo.",
            "{suspeito} estava extremamente nervoso na dispensa da cozinha.",
            "{assassino} estava deixando pegadas de sangue.",
            "{suspeito} estava comendo no salão principal.",
            "{suspeito} estava vendo o por do sol fora da casa.",
            "{suspeito} estava no quarto 4.",
            "Se {suspeito} estava na suíte master, então ele estava tomando banho.",
            "{assassino} estava subornando o cozinheiro.",
            "{suspeito} estava com uma faca.",
            "Se {suspeito} estava na casa, então ele(a) estava no corredor dos quartos.",
        ],
        "Quarto do Suspeito": [
		    "{assassino} estava escondido no armário do quarto.",
            "{suspeito} estava em uma reunião online.",
            "Se {suspeito} estava na cozinha, então ele estava conversando com o cozinheiro.",
            "{suspeito} estava deitado no deck externo.",
            "{suspeito} estava com uma tesoura suja de sangue.",
            "{suspeito} estava tomando banho.",
            "{suspeito} estava com um canivete no bolso.",
            "{assassino} estava com uma arma silenciada.",
            "{suspeito} estava na sala de entretenimento jogando videogame.",
            "{suspeito} estava conversando com a faxineira.",
        ],
        "Deck da Verdade": [
		    "{suspeito} estava no quarto 6 arrumando suas roupas.",
            "{suspeito} estava com as mãos ensanguentadas.",
            "{suspeito} estava defecando no quarto 5.",
            "{suspeito} estava em seu carro usando drogas.",
            "{suspeito} estava falando com sua esposa por telefone.",
            "Se {assassino} estava no deck, então deixou pegadas de sangue.",
            "{suspeito} estava na cozinha procurando bebidas.",
            "{suspeito} estava desesperado(a) e muito arrependido de algo.",
            "{suspeito} estava no salão principal.",
            "{assassino} estava fugindo para fora da casa.",
        ],
        "Corredor Sombrio": [
		    "{suspeito} estava fugindo no corredor sombrio.",
            "{assassino} estava com uma faca escondida no casaco.",
            "Se {suspeito} estava no quarto 2, então ele(a) estava vomitando no banheiro.",
            "{suspeito} estava tendo um ataque de ansiedade.",
            "{suspeito} estava fazendo embaixadinhas no deck.",
            "{suspeito} estava brigando com a faxineira.",
            "{assassino} estava fugindo loucamente em seu carro.",
            "{suspeito} estava dormindo no quarto 5.",
            "{suspeito} estava ouvindo musica alta na sala de entretenimento.",
            "{suspeito} estava com uma arma.",
        ],
    }

    return random.sample(dicas_por_cenario[cenario], 7)


def imprimir_linha(texto):
    comprimento_texto = len(texto)
    linha = "-" * comprimento_texto
    print(f"{linha}\n{texto}\n{linha}")


pontuacao_total = 0


def pos_jogo_acerto(assassino):
    global pontuacao_total
    print(f"{verde}" + "-" * 60)
    print(f"{verde}|{'Fim de Jogo!':^58}|")
    print(f"{verde}|{f'O assassino era {assassino}':^58}|" f"{reset}")
    print(f"{verde}|{f'Pontuação acumulada: {pontuacao_total}':^58}|{reset}")
    print(f"{verde}" + "-" * 60)
    print(f"{reset}1. Jogar novamente\n2. Sair")
    escolha_pos_jogo = input("Escolha uma opção: ")

    if escolha_pos_jogo == "1":
        jogo()  # Reiniciar o jogo
    elif escolha_pos_jogo == "2":
        print(f"{verde}" + "-" * 60)
        print(f"{verde}|{'Obrigado por jogar!':^58}|")
        print(f"{verde}" + "-" * 60)
        exit()
    else:
        print("Escolha inválida. Saindo do jogo.")
        exit()


def pos_jogo_errado(assassino):
    global pontuacao_total
    print(f"{verde}" + "-" * 60)
    print(f"{verde}|{'Fim de Jogo!':^58}|")
    print(f"{verde}|{f'Pontuação acumulada: {pontuacao_total}':^58}|{reset}")
    print(f"{verde}" + "-" * 60)
    print(f"{reset}1. Jogar novamente\n2. Sair")
    escolha_pos_jogo = input("Escolha uma opção: ")

    if escolha_pos_jogo == "1":
        jogo()  # Reiniciar o jogo
    elif escolha_pos_jogo == "2":
        print(f"{verde}" + "-" * 60)
        print(f"{verde}|{'Obrigado por jogar!':^58}|")
        print(f"{verde}" + "-" * 60)
        exit()
    else:
        print("Escolha inválida. Saindo do jogo.")
        exit()


def reiniciar_personagens():
    global personagens_lista
    personagens_lista = [
        "Alessandro Rossi",
        "Lucca Romano",
        "Sofia Bellini",
        "Chiara Vitale",
        "Bianca Moretti",
        "Matteo Ferraro",
        "Elena Capello",
    ]


def jogo():
    global pontuacao_total  # Usar a variável global para pontuação
    reiniciar_personagens()  # Reinicia a lista de personagens

    while True:
        bem_vindo()
        descricao()
        exibir_planta()
        personagens()

        # Determinar o assassino aleatoriamente
        assassino = random.choice(personagens_lista)

        cenarios()
        cenario_escolhido = int(input("Escolha um cenário (1-10): ")) - 1
        cenario = cenarios_lista[cenario_escolhido]

        # Determinar a vítima aleatoriamente
        vitima = random.choice(personagens_lista)
        personagens_lista.remove(vitima)  # Remover a vítima da lista de suspeitos

        # Gerar dicas
        dicas = gerar_dicas(cenario, personagens_lista)

        # Exibir a vítima
        print(f"{verde}" + "-" * 60)
        if vitima in [
            "Sofia Bellini",
            "Chiara Vitale",
            "Bianca Moretti",
            "Elena Capello",
        ]:
            print(f"{verde}|{f'{vitima} FOI ASSINADA!':^58}|")
        else:
            print(f"{verde}|{f'{vitima} FOI ASSASSINADO!':^58}|")
        print(f"{verde}" + "-" * 60)

        # Mostrar a lista de suspeitos com índices
        print(f"{verde}" + "-" * 60)
        print(f"{verde}|{'SUSPEITOS':^58}|")
        print(f"{verde}" + "-" * 60)
        for index, personagem in enumerate(personagens_lista):
            print(f"{verde}|{index + 1}. {personagem:<55}|")
        print(f"{verde}" + "-" * 60 + f"{reset}")

        # Lógica do jogo
        pontos = 7  # Pontos máximos para acertar de primeira

        for i, dica in enumerate(dicas):
            imprimir_linha(
                f"\nDica {i + 1}: {dica.format(suspeito=personagens_lista[i % len(personagens_lista)])}"
            )

            while True:  # Loop para garantir a escolha válida
                print(f"{verde}1. Adivinhar\n2. Próxima dica\n3. Sair{reset}")
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    try:
                        palpite_index = (
                            int(input("Digite o número correspondente ao suspeito: "))
                            - 1
                        )
                        if 0 <= palpite_index < len(personagens_lista):
                            palpite = personagens_lista[palpite_index]
                            if palpite == assassino:
                                print(
                                    f"Parabéns! Você acertou e ganhou {pontos} pontos."
                                )
                                pontuacao_total += pontos  # Adiciona à pontuação total
                                pos_jogo_acerto(assassino)
                                return
                            else:
                                print(
                                    f"Você errou! O assassino era {assassino}. Você não pontuou nessa."
                                )
                                pos_jogo_errado(assassino)
                                return  # Finaliza o jogo
                        else:
                            print("Número inválido. Tente novamente.")
                    except ValueError:
                        print("Entrada inválida. Por favor, insira um número.")

                elif escolha == "2":
                    pontos -= 1
                    if pontos == 0:
                        pos_jogo_acerto(assassino)
                        return  # Finaliza o jogo
                    break  # Sai do loop para ir para a próxima dica

                elif escolha == "3":
                    pos_jogo_acerto(assassino)
                    return  # Finaliza o jogo

                else:
                    print("Opção inválida. Tente novamente.")


# Iniciar o jogo
if __name__ == "__main__":
    jogo()