#verificacao_senhas
adm = "Vinícius"
senha = "24102003"
adm_confere = "Vinícius"
senha_confere = "24102003"

if adm == adm_confere and senha == senha_confere:
  print("Acesso autorizado!")
else:
  print("Usuário ou senha incorreta!")

confer = adm == adm_confere and senha == senha_confere
print(confer)