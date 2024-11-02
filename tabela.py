import ttg

print("tabelas verdades do cenário 1")
print("--------------------------------------")
#tabela verdade tautologia
print("v  v ~v : Elena estava na cozinha ou Elena não estava na cozinha")
table = ttg.Truths(['v'], ['v or not v'])
print(table)
print("--------------------------------------")
#tabela verdade Contingência
print("r→¬s: Se Sofia estava na sala de entretenimento, então Chiara não matou a vítima.") 
tabela_verdade = ttg.Truths(['r', 's'], ['r implies not s'])
print(tabela_verdade)
print("--------------------------------------")
#tabela verdade Contingência
print("s→q: Se Chiara matou a vítima, então Lucca estava com uma faca. ") 
tabela_verdade = ttg.Truths(['s', 'q'], ['s implies q'])
print(tabela_verdade)
print("--------------------------------------")
#tabela verdade Contingência
print("P->t: Se Alessandro estava no salão, então Matteo tinha um motivo para matar a vítima. ") 
tabela_verdade = ttg.Truths(['P', 'T'], ['P implies T'])
print(tabela_verdade)
print("--------------------------------------")
#tabela verdade Contingência
print("¬r→¬v: Se Sofia não estava na sala de entretenimento, então Elena não estava na cozinha.  ") 
tabela_verdade = ttg.Truths(['r', 'v'], ['not r implies not v'])
print(tabela_verdade)
print("--------------------------------------")
#tabela verdade contradição
print(" U ^ ~U : Bianca estava sozinha no corredor e Bianca não estava sozinha no corredor. (falsa não ajuda em nada)  ") 
tabela_verdade = ttg.Truths(['U'], ['U and not U'])
print(tabela_verdade)
print("--------------------------------------")
#tabela verdade Contingência
print(" t→s : Se Matteo tinha um motivo, então Chiara matou a vítima.  ") 
tabela_verdade = ttg.Truths(['T', 'S'], ['T implies S'])
print(tabela_verdade)
print("--------------------------------------")
#tabela verdade Contingência
print(" ¬p→s : Se Alessandro não estava no salão, então Chiara matou a vítima.  ") 
tabela_verdade = ttg.Truths(['P', 'S'], ['not P implies S'])
print(tabela_verdade)
print("--------------------------------------")
#tabela verdade Contingência
print("r→v: Se Sofia estava na sala de entretenimento, então Elena estava na cozinha. ")
tabela_verdade = ttg.Truths(['r', 'v'], ['r implies v'])
print(tabela_verdade)
print("--------------------------------------")
#tabela verdade Contingência
print("v→ ~p: Se Elena estava na cozinha, então Alessandro não estava no salão. ")
tabela_verdade = ttg.Truths(['v', 'p'], ['v implies not p'])
print(tabela_verdade)

