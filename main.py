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
    "Deck da Verdade",
    "Corredor Sombrio",
]


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
            "{suspeito} estava com uma arma ou faca.",
            "{suspeito} estava no quarto 5 ou quarto 6.",
            "Se {suspeito} estava na casa, então ele(a) estava na sala de estar.",
            "{assassino} estava fugindo da casa e estava correndo muito.",
            "{suspeito} estava dormindo e roncando.",
            "{suspeito} estava falando com o cozinheiro ou com a faxineira.",
            "{suspeito} estava com uma acompanhante na sala de entretenimento ou na suíte master",
            "{suspeito} estava no salão e muito nervoso no momento da morte.",
            "{assassino} estava com sangue em suas roupas se e somente se estivesse com uma faca no bolso.",
            "{suspeito} estava tendo um coma alcoólico no deck externo ou no corredor.",
        ],
        "Cozinha da Discórdia": [
            "{suspeito} estava na piscina do deck externo ou no quarto 5.",
            "{suspeito} estava extremamente nervoso e aflito na dispensa da cozinha.",
            "{assassino} estava deixando pegadas de sangue e estava correndo.",
            "{suspeito} estava comendo no salão principal ou no deck externo.",
            "{suspeito} estava vendo o por do sol fora da casa se e somente se o por do sol estivesse bonito.",
            "{suspeito} estava no quarto 4 ou no quarto 2.",
            "Se {suspeito} estava na suíte master, então ele estava tomando banho.",
            "{assassino} estava subornando ou ameaçando o cozinheiro.",
            "{suspeito} estava com uma faca e estava nervoso.",
            "Se {suspeito} estava na casa, então ele(a) estava no corredor dos quartos.",
        ],
        "Quarto do Suspeito": [
            "{assassino} estava escondido no armário do quarto e tinha sangue em suas roupas.",
            "{suspeito} estava em uma reunião online ou em chamada de vídeo com a amante.",
            "Se {suspeito} estava na cozinha, então ele estava conversando com o cozinheiro.",
            "{suspeito} estava deitado no deck externo e estava admirando a vista.",
            "{suspeito} estava com uma tesoura suja de sangue e estava em choque.",
            "{suspeito} estava tomando banho se e somente se estivesse sujo.",
            "{suspeito} estava com um canivete ou uma faca no bolso.",
            "{assassino} estava com uma arma silenciada e com carregadores para a arma.",
            "{suspeito} estava na sala de entretenimento jogando videogame ou assistindo um filme.",
            "{suspeito} estava conversando com a faxineira ou falando sozinho.",
        ],
        "Deck da Verdade": [
            "{suspeito} estava no quarto 6 arrumando suas roupas e o quarto.",
            "{suspeito} estava com as mãos e a camiseta ensanguentadas.",
            "{suspeito} estava defecando ou urinando no quarto 5.",
            "{suspeito} estava em seu carro usando drogas ou bebidas alcoólicas.",
            "{suspeito} estava falando com sua esposa ou filhos por telefone.",
            "Se {assassino} estava no deck, então deixou pegadas de sangue.",
            "{suspeito} estava na cozinha procurando bebidas e petiscos.",
            "{suspeito} estava desesperado(a) e muito arrependido(a) de algo.",
            "{suspeito} estava no salão principal se e somente se tivesse comida.",
            "{assassino} estava fugindo para fora da casa ou se escondendo.",
        ],
        "Corredor Sombrio": [
            "{suspeito} estava fugindo e correndo no corredor sombrio.",
            "{assassino} estava com uma faca escondida no casaco ou na calça.",
            "Se {suspeito} estava no quarto 2, então ele(a) estava vomitando no banheiro.",
            "{suspeito} estava tendo um ataque de ansiedade e panico.",
            "{suspeito} estava fazendo embaixadinhas ou estava na piscina do deck.",
            "{suspeito} estava brigando com a faxineira e com o cozinheiro.",
            "{assassino} estava fugindo e acelerando muito seu carro.",
            "{suspeito} estava dormindo no quarto 5 ou no quarto 6.",
            "{suspeito} estava ouvindo musica alta se e somente se estivesse na suíte master.",
            "{suspeito} estava com uma arma e uma faca.",
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
    return random.sample(dicas_formatadas, 10)


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

        assassino = random.choice(personagens_lista)
        vitima = random.choice(personagens_lista)

        while vitima == assassino:
            vitima = random.choice(personagens_lista)

        personagens_lista.remove(vitima)

        cenarios()
        cenario_escolhido = int(input("Escolha um cenário (1-5): ")) - 1
        cenario = cenarios_lista[cenario_escolhido]

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

                            # Comparar com o assassino sem removê-lo antes do término
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