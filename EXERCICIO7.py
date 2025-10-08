def obter_idade() -> int:
    """
    Solicita ao usuário que insira sua idade.

    Returns:
        int: Idade inserida pelo usuário.
    """
    return int(input("Idade: "))


def obter_renda() -> float:
    """
    Solicita ao usuário que insira sua renda mensal.

    Returns:
        float: Renda mensal inserida pelo usuário.
    """
    return float(input("Renda mensal (R$): "))


def obter_dividas() -> float:
    """
    Solicita ao usuário que insira o total de dívidas.

    Returns:
        float: Valor total de dívidas inserido pelo usuário.
    """
    return float(input("Total de dívidas (R$): "))


def calcular_percentual_divida(dividas: float, renda: float) -> float:
    """
    Calcula o percentual de dívidas em relação à renda.

    Args:
        dividas (float): Valor total das dívidas.
        renda (float): Renda mensal.

    Returns:
        float: Percentual da dívida em relação à renda.
    """
    if renda == 0:
        return 100.0  # Considera risco total se não há renda
    return (dividas / renda) * 100


def classificar_risco(renda: float, percentual_divida: float) -> str:
    """
    Classifica o risco financeiro do usuário com base na renda e percentual de dívida.

    Args:
        renda (float): Renda mensal.
        percentual_divida (float): Percentual da dívida em relação à renda.

    Returns:
        str: Classificação de risco ("ALTA", "MEDIA", "BAIXA", "MEDIA/BAIXA").
    """
    if renda < 2000 and percentual_divida > 50:
        return "ALTA"
    elif 2000 <= renda <= 5000 or 30 <= percentual_divida <= 50:
        return "MEDIA"
    elif renda > 5000 and percentual_divida < 30:
        return "BAIXA"
    else:
        return "MEDIA/BAIXA"


def main() -> None:
    """
    Função principal que executa a classificação de risco.
    """
    idade = obter_idade()
    renda = obter_renda()
    dividas = obter_dividas()

    percentual = calcular_percentual_divida(dividas, renda)
    risco = classificar_risco(renda, percentual)

    print(f"Sua classificação de risco é: {risco}")


if __name__ == "__main__":
    main()
