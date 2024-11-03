import datetime
import random

vermelho = "\033[91m"
reset = "\033[0m"

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

cenarios_lista = [
    "Crime no Salão",
    "Cozinha da Discórdia",
    "Quarto do Suspeito",
]

assassinos_por_cenario = {
    "Crime no Salão": "Chiara Vitale",
    "Cozinha da Discórdia": "Lucca Romano",
    "Quarto do Suspeito": "Elena Capello",
}


def bem_vindo():
    print(f"{vermelho}" + "-" * 60)
    print(f"{vermelho}|{'':^58}|")
    print(f"{vermelho}|{'BEM VINDO AO JOGO!':^58}|")
    print(f"{vermelho}|{'':^58}|")
    print(f"{vermelho}|{'Prepare-se para desvendar o mistério':^58}|")
    print(f"{vermelho}|{'que te aguarda!':^58}|")
    print(f"{vermelho}|{'':^58}|")
    print(f"{vermelho}" + "-" * 60 + f"{reset}")


def descricao():
    print(f"{vermelho}" + "-" * 60)
    print(f"{vermelho}|{'DESCRIÇÃO DO CASO':^58}|")
    print(f"{vermelho}" + "-" * 60)
    print(f"{vermelho}|{'7 milionários se reúnem em uma casa luxuosa':^58}|")
    print(f"{vermelho}|{'em uma ilha para uma celebração de negócios.':^58}|")
    print(f"{vermelho}|{'Durante a festa, um dos sócios é encontrado morto.':^58}|")
    print(f"{vermelho}|{'Agora, todos os presentes têm motivos ocultos e':^58}|")
    print(f"{vermelho}|{'segredos que podem levar a uma investigação profunda.':^58}|")
    print(
        f"{vermelho}|{'Seu dever é investigar, encontrar o assassino e a arma.':^58}|"
    )
    print(f"{vermelho}|{'Contamos com você para desvendar este mistério!':^58}|")
    print(f"{vermelho}" + "-" * 60 + f"{reset}")


def personagens():
    print(f"{vermelho}" + "-" * 60)
    print(f"{vermelho}|{'PERSONAGENS':^58}|")
    print(f"{vermelho}" + "-" * 60)
    for i, (personagem, descricao) in enumerate(
        zip(personagens_lista, personagens_descricao), start=1
    ):
        print(f"{vermelho}|{f'{i}. {personagem} - {descricao}':<58}|")
    print(f"{vermelho}" + "-" * 60 + f"{reset}")


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
        print(f"{vermelho}{linha}{reset}")


def cenarios():
    print(f"{vermelho}" + "-" * 60)
    print(f"{vermelho}|{'CENÁRIOS DISPONÍVEIS':^58}|")
    print(f"{vermelho}" + "-" * 60)
    for i, cenario in enumerate(cenarios_lista, start=1):
        print(f"{vermelho}|{f'{i}. {cenario}':<58}|")
    print(f"{vermelho}" + "-" * 60 + f"{reset}")


def gerar_dicas(cenario, assassino):
    dicas_por_cenario = {
        "Crime no Salão": [
            "Elena estava na cozinha ou Elena não estava na cozinha.",
            "Se Sofia estava na sala de entretenimento, então Chiara não matou a vítima.",
            "Se Chiara matou a vítima, então Lucca estava com uma faca.",
            "Se Alessandro estava no salão, então Matteo tinha um motivo para matar a vítima.",
            "Se Sofia não estava na sala de entretenimento, então Elena não estava na cozinha.",
            "Bianca estava sozinha no corredor e Bianca não estava sozinha no corredor.",
            "Se Matteo tinha um motivo, então Chiara matou a vítima.",
            "Se Alessandro não estava no salão, então Chiara matou a vítima.",
            "Se Sofia estava na sala de entretenimento, então Elena estava na cozinha.",
            "Se Elena estava na cozinha, então Alessandro não estava no salão.",
        ],
        "Cozinha da Discórdia": [
            "Chiara estava no salão no momento do crime ou Chiara não estava no salão no momento do crime.",
            "Se Sofia estava na sala de entretenimento, então Lucca não matou a vítima.",
            "Se Lucca matou a vítima, então Lucca estava com uma faca.",
            "Se Alessandro estava no salão, então Matteo tinha um motivo para matar a vítima.",
            "Se Sofia não estava na sala de entretenimento, então Chiara não estava na cozinha.",
            "Se Bianca estava sozinha no corredor, então Bianca não está sozinha no corredor.",
            "Se Matteo tinha um motivo, então Lucca matou a vítima.",
            "Se Alessandro não estava no salão, então Lucca matou a vítima.",
            "Se Sofia estava na sala de entretenimento, então Chiara estava na cozinha.",
            "Se Chiara estava na cozinha, então Alessandro não estava no salão.",
        ],
        "Quarto do Suspeito": [
            "Alessandro ou Sofia estavam no salão no momento do crime.",
            "Se Chiara estava na sala de entretenimento, então Elena não matou a vítima.",
            "Se Elena matou a vítima, então Lucca estava com uma faca.",
            "Se Alessandro estava no salão, então Matteo tinha um motivo para matar a vítima.",
            "Se Chiara não estava na sala de entretenimento, então Sofia não estava na cozinha.",
            "Se Bianca estava sozinha no corredor, então Alessandro estava no salão.",
            "Se Matteo tinha um motivo, então Elena matou a vítima.",
            "Se Alessandro não estava no salão, então Elena matou a vítima.",
            "Se Chiara estava na sala de entretenimento, então Sofia estava na cozinha.",
            "Se Sofia estava na cozinha, então Alessandro não estava no salão.",
        ],
    }

    dicas = dicas_por_cenario[cenario]
    dicas_formatadas = [
        dica.format(
            suspeito=random.choice([p for p in personagens_lista if p != assassino]),
            assassino=assassino,
        )
        for dica in dicas
    ]
    return dicas_formatadas


def imprimir_linha(texto):
    comprimento_texto = len(texto)
    linha = "-" * comprimento_texto
    print(f"{linha}\n{texto}\n{linha}")


pontuacao_total = 0


def pos_jogo_acerto(assassino):
    global pontuacao_total
    print(f"{vermelho}" + "-" * 60)
    print(f"{vermelho}|{'Fim de Jogo!':^58}|")
    print(f"{vermelho}|{f'O assassino era {assassino}':^58}|" f"{reset}")
    print(f"{vermelho}|{f'Pontuação acumulada: {pontuacao_total}':^58}|{reset}")
    print(f"{vermelho}" + "-" * 60)
    print(f"{reset}1. Jogar novamente\n2. Sair")
    escolha_pos_jogo = input("Escolha uma opção: ")

    if escolha_pos_jogo == "1":
        jogo()
    elif escolha_pos_jogo == "2":
        print(f"{vermelho}" + "-" * 60)
        print(f"{vermelho}|{'Obrigado por jogar!':^58}|")
        print(f"{vermelho}" + "-" * 60)
        exit()
    else:
        print("Escolha inválida. Saindo do jogo.")
        exit()


def pos_jogo_errado(s):
    global pontuacao_total
    print(f"{vermelho}" + "-" * 60)
    print(f"{vermelho}|{'Fim de Jogo!':^58}|")
    print(f"{vermelho}|{f'Pontuação acumulada: {pontuacao_total}':^58}|{reset}")
    print(f"{vermelho}" + "-" * 60)
    print(f"{reset}1. Jogar novamente\n2. Sair")
    escolha_pos_jogo = input("Escolha uma opção: ")

    if escolha_pos_jogo == "1":
        jogo()
    elif escolha_pos_jogo == "2":
        print(f"{vermelho}" + "-" * 60)
        print(f"{vermelho}|{'Obrigado por jogar!':^58}|")
        print(f"{vermelho}" + "-" * 60)
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
    global pontuacao_total
    reiniciar_personagens()

    while True:
        bem_vindo()
        descricao()
        exibir_planta()
        personagens()

        cenarios()
        cenario_escolhido = int(input("Escolha um cenário (1-3): ")) - 1
        cenario = cenarios_lista[cenario_escolhido]
        assassino = assassinos_por_cenario[cenario]
        
        vitima = random.choice([p for p in personagens_lista if p != assassino])
        personagens_lista.remove(vitima)

        dicas = gerar_dicas(cenario, assassino)

        print(f"{vermelho}" + "-" * 60)
        if vitima in [
            "Sofia Bellini",
            "Chiara Vitale",
            "Bianca Moretti",
            "Elena Capello",
        ]:
            print(f"{vermelho}|{f'{vitima} FOI ASSASSINADA!':^58}|")
        else:
            print(f"{vermelho}|{f'{vitima} FOI ASSASSINADO!':^58}|")
        print(f"{vermelho}" + "-" * 60)

        print(f"{vermelho}" + "-" * 60)
        print(f"{vermelho}|{'SUSPEITOS':^58}|")
        print(f"{vermelho}" + "-" * 60)

        for index, personagem in enumerate(personagens_lista):
            print(f"{vermelho}|{index + 1}. {personagem:<55}|")
        print(f"{vermelho}" + "-" * 60 + f"{reset}")

        pontos = 10

        for i, dica in enumerate(dicas):
            imprimir_linha(
                f"\nDica {i + 1}: {dica.format(suspeito=personagens_lista[i % len(personagens_lista)], assassino=assassino)}"
            )

            while True:
                print(f"{vermelho}1. Adivinhar\n2. Próxima dica\n3. Sair{reset}")
                escolha = input("Escolha uma opção: ")

                if escolha == "1":
                    try:
                        palpite_index = (
                            int(input("Digite o número correspondente ao suspeito: "))
                            - 1
                        )
                        if 0 <= palpite_index < len(personagens_lista):
                            palpite = personagens_lista[palpite_index]
    
                            if palpite.strip() == assassino.strip():
                                print(
                                    f"Parabéns! Você acertou e ganhou {pontos} pontos."
                                )
                                pontuacao_total += pontos
                                pos_jogo_acerto(assassino)
                                return
                            else:
                                print(
                                    f"Você errou! O assassino era {assassino}. Você não pontuou nessa."
                                )
                                pos_jogo_errado(palpite)
                                return
                        else:
                            print("Número inválido. Tente novamente.")
                    except ValueError:
                        print("Entrada inválida. Por favor, insira um número.")

                elif escolha == "2":
                    pontos -= 1
                    if pontos <= 0:
                        print("Você não tem mais pontos para continuar. Fim de jogo.")
                        pos_jogo_acerto(assassino)
                        return
                    break

                elif escolha == "3":
                    pos_jogo_acerto(assassino)
                    return

                else:
                    print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    jogo()
