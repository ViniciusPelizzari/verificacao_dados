#verificacao_senhas
adm = "Vinícius"
senha = "24102003"
adm_confere = "Vinícius"
senha_confere = "24102003"
#verdadeiro = True
#print("Verdadeiro =", verdadeiro)
#falso = False
#print("Falso =", falso)
#print(type(falso))
#print(type(verdadeiro))
if adm == adm_confere and senha == senha_confere:
  print("Acesso autorizado!")
else:
  print("Usuário ou senha incorreta!")


#verificacao_senhas
adm = "Vinícius"
senha = "24102003"
adm_confere = "Vinícius"
senha_confere = "24102003"
confer = adm == adm_confere and senha == senha_confere
print(confer)