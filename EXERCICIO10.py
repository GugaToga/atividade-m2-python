print("Crie uma senha seguindo as regras:")
print("- Mínimo 8 caracteres")
print("- Pelo menos 1 letra maiúscula")
print("- Pelo menos 1 letra minúscula")
print("- Pelo menos 1 número")
print("- Pelo menos 1 dos símbolos: !@#$%")

senha = input("Digite a senha: ")
tem_maiuscula = any(c.isupper() for c in senha)
tem_minuscula = any(c.islower() for c in senha)
tem_numero = any(c.isdigit() for c in senha)
tem_simbolo = any(c in "!@#$%" for c in senha)
tamanho_ok = len(senha) >= 8
if tem_maiuscula and tem_minuscula and tem_numero and tem_simbolo and tamanho_ok:
    print(" Senha válida!")
else:
    print(" Senha inválida! Tente novamente.")
