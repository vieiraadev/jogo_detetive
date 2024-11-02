import ttg

print("tabelas verdades do cenário 1")
print("--------------------------------------")
#tabela verdade Contingência
print("{suspeito} estava com uma arma ou faca.")
table = ttg.Truths(['p', 'q'], ['p or q'])
print(table)
print("--------------------------------------")
#tabela verdade tautologia
print("{suspeito} estava no quarto 5 ou não estava no quarto 5")
table = ttg.Truths(['p'], ['p or not p'])
print(table)
print("--------------------------------------")
#tabela verdade Contingência
print("Se {suspeito} estava na casa, então ele(a) estava na sala de estar.")
table = ttg.Truths(['p', 'q'], ['not p or q'])
print(table)
print("--------------------------------------")
#tabela verdade Contingência
print("{assassino} estava fugindo da casa e estava correndo muito.")
table = ttg.Truths(['p', 'q'], ['p and q'])
print(table)
print("--------------------------------------")
#tabela verdade Contingência
print("{suspeito} estava dormindo e roncando.")
table = ttg.Truths(['p', 'q'], ['p and q'])
print(table)
print("--------------------------------------")
#tabela verdade Contingência
print(
    "O {suspeito} estava escondido no quarto e ao mesmo tempo não estava escondido em nenhum lugar da casa."
)
table = ttg.Truths(['p', 'q'], ['p and not q'])
print(table)
print("--------------------------------------")
#tabela verdade Contingência
print(
    "{suspeito} estava com uma acompanhante na sala de entretenimento ou na suíte master"
)
table = ttg.Truths(['p', 'q'], ['p or q'])
print(table)
print("--------------------------------------")
#tabela verdade contradição
print(
    "{suspeito} estava sozinho no quarto, mas ao mesmo tempo não estava sozinho no quarto..."
)
table = ttg.Truths(['p'], ['p and not p'])
print(table)
print("--------------------------------------")
#tabela verdade tautologia
print(
    "O {assassino}  estava presente na cena do crime ou não estava presente, mas ainda assim tem alguma conexão com o crime."
)
table = ttg.Truths(['p'], ['p or not p'])
print(table)
print("--------------------------------------")
#tabela verdade tautologia
print(
    "{assassino}  tinha um álibi ou ele não tinha um álibi, mas suas ações chamaram a atenção naquela noite."
)
table = ttg.Truths(['p'], ['p or not p'])
print(table)
