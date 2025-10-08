def obter_idade() -> int:
    """
    Solicita ao usuário que insira a idade e retorna como um inteiro.

    Returns:
        int: Idade inserida pelo usuário.
    """
    return int(input("Idade: "))


def obter_nacionalidade() -> int:
    """
    Solicita ao usuário que escolha a nacionalidade.

    Returns:
        int: 1 para Brasileiro, 2 para Estrangeiro.
    """
    return int(input("Nacionalidade-\n1- Brasileiro\n2- Estrangeiro\n>: "))


def validar_idade(idade: int) -> bool:
    """
    Verifica se a idade está dentro de um intervalo válido (0 a 150).

    Args:
        idade (int): Idade a ser validada.

    Returns:
        bool: True se for válida, False caso contrário.
    """
    return 0 <= idade <= 150


def validar_nacionalidade(nacionalidade: int) -> bool:
    """
    Verifica se a nacionalidade é válida (1 ou 2).

    Args:
        nacionalidade (int): Código da nacionalidade.

    Returns:
        bool: True se for válida, False caso contrário.
    """
    return nacionalidade in (1, 2)


def verificar_direito_ao_voto(idade: int, nacionalidade: int) -> str:
    """
    Determina o direito de voto com base na idade e nacionalidade.

    Args:
        idade (int): Idade da pessoa.
        nacionalidade (int): Código da nacionalidade (1 para Brasileiro, 2 para Estrangeiro).

    Returns:
        str: Mensagem sobre o direito de voto.
    """
    if idade < 16:
        return "Você não pode votar."
    elif idade >= 18:
        if nacionalidade == 1:
            return "Você pode votar!"
        elif nacionalidade == 2:
            return "Você pode votar! (Opcionalmente)"
    elif 16 <= idade < 18:
        return "Você pode votar! (Opcionalmente)"
    return "Erro ao verificar o direito ao voto."


def main() -> None:
    """
    Função principal que coordena a execução do programa.
    """
    idade = obter_idade()
    nacionalidade = obter_nacionalidade()

    if not validar_idade(idade):
        print("Idade inválida.")
    elif not validar_nacionalidade(nacionalidade):
        print("Nacionalidade inválida.")
    else:
        resultado = verificar_direito_ao_voto(idade, nacionalidade)
        print(resultado)


if __name__ == "__main__":
    main()
