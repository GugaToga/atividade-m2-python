def validar_senha(senha: str) -> bool:
    """
    Verifica se a senha atende aos seguintes critérios:
    - Mínimo de 8 caracteres
    - Pelo menos 1 letra maiúscula
    - Pelo menos 1 letra minúscula
    - Pelo menos 1 número
    - Pelo menos 1 símbolo especial (!@#$%)

    Args:
        senha (str): A senha a ser verificada.

    Returns:
        bool: True se a senha for válida, False caso contrário.
    """
    tem_maiuscula: bool = any(c.isupper() for c in senha)
    tem_minuscula: bool = any(c.islower() for c in senha)
    tem_numero: bool = any(c.isdigit() for c in senha)
    tem_simbolo: bool = any(c in "!@#$%" for c in senha)
    tamanho_ok: bool = len(senha) >= 8

    return tem_maiuscula and tem_minuscula and tem_numero and tem_simbolo and tamanho_ok


def exibir_regras() -> None:
    """
    Exibe as regras de criação de senha para o usuário.
    """
    print("Crie uma senha seguindo as regras:")
    print("- Mínimo 8 caracteres")
    print("- Pelo menos 1 letra maiúscula")
    print("- Pelo menos 1 letra minúscula")
    print("- Pelo menos 1 número")
    print("- Pelo menos 1 dos símbolos: !@#$%")


def main() -> None:
    """
    Função principal que executa o programa de validação de senha.
    """
    exibir_regras()
    senha: str = input("Digite a senha: ")

    if validar_senha(senha):
        print("Senha válida!")
    else:
        print("Senha inválida! Tente novamente.")


if __name__ == "__main__":
    main()

