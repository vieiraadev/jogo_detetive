import ttg

# Definindo a proposição
# P: "{suspeito} está presente"
# ¬P: "{suspeito} não está presente"

tabela_tautologia = ttg.Truths(['P'], ['P or not P'])

print(
    "Tabela Verdade para a tautologia '{suspeito} está presente ou não está presente':"
)
print(tabela_tautologia)

# P: "{suspeito} estava com um relógio"
# ¬P: "{suspeito} não estava com um relógio"

# tabela verdade P and ¬P
tabela_contradicao = ttg.Truths(['P'], ['P and not P'])

print(
    "Tabela Verdade para a contradição '{suspeito} estava com um relógio e {suspeito} não estava com um relógio':"
)
print(tabela_contradicao)

# P: "{suspeito} está em casa"
# Q: "{suspeito} não está em casa"

# tabela verdade P or Q
# P: "{suspeito} está estudando para o exame"
# Q: "{suspeito} está assistindo a um filme"

# Criando a tabela verdade para a contingência P or Q
tabela_contingencia = ttg.Truths(['P', 'Q'], ['P or Q'])

# Exibindo a tabela verdade
print(
    "Tabela Verdade para a contingência '{suspeito} está estudando para o exame ou {suspeito} está assistindo a um filme':"
)
print(tabela_contingencia)

# Definindo as proposições
# P: "{suspeito} está presente"
# R: "{suspeito} estava com um relógio"
# S: "{suspeito} está estudando para o exame"
# T: "{suspeito} está assistindo a um filme"

# Criando a tabela verdade para a proposição combinada
tabela_combinada = ttg.Truths(
    ['P', 'R', 'S', 'T'],  # Variáveis P, R, S e T
    ['P and R and (S and T)']  # Proposição combinada
)

# Exibindo a tabela verdade
print("Tabela Verdade para a proposição combinada:")
print(tabela_combinada)
