adm = "Vinícius"
senha = "24102003"

print("Usuário: ")
adm_c = input()
print("Senha: ")
senha_c = input()
#verificacao_senhas

#verdadeiro = True
#print("Verdadeiro =", verdadeiro)
#falso = False
#print("Falso =", falso)
#print(type(falso))
#print(type(verdadeiro))
if adm == adm_c and senha == senha_c:
  print("Acesso autorizado!")
else:
  print("Usuário ou senha incorreta!")


#verificacao_senhas
adm = "Vinícius"
senha = "24102003"
confer = adm == adm_c and senha == senha_c
print(confer)