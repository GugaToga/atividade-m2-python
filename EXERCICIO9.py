def obter_preco() -> float:
    """
    Solicita ao usuário o preço do produto.

    Returns:
        float: Preço do produto.
    """
    while True:
        try:
            preco = float(input("Digite o preço do produto: R$ "))
            if preco < 0:
                print("O preço não pode ser negativo. Tente novamente.")
                continue
            return preco
        except ValueError:
            print("Entrada inválida. Digite um número válido.")


def verificar_vip() -> bool:
    """
    Verifica se o cliente é VIP.

    Returns:
        bool: True se for VIP, False caso contrário.
    """
    while True:
        vip = input("O cliente é VIP? (s/n): ").strip().lower()
        if vip in ('s', 'n'):
            return vip == 's'
        else:
            print("Entrada inválida. Digite 's' para sim ou 'n' para não.")


def calcular_desconto(preco: float, vip: bool) -> int:
    """
    Calcula o percentual de desconto com base no preço e status VIP.

    Args:
        preco (float): Preço original do produto.
        vip (bool): Indica se o cliente é VIP.

    Returns:
        int: Percentual total de desconto.
    """
    if preco >= 100:
        desconto = 20
    elif preco >= 50:
        desconto = 10
    else:
        desconto = 0

    if vip:
        desconto += 5

    return desconto


def calcular_preco_final(preco: float, desconto: int) -> float:
    """
    Calcula o preço final com o desconto aplicado.

    Args:
        preco (float): Preço original.
        desconto (int): Percentual de desconto.

    Returns:
        float: Preço final após desconto.
    """
    return preco - (preco * desconto / 100)


def mostrar_resultado(desconto: int, preco_final: float) -> None:
    """
    Exibe o desconto aplicado e o preço final.

    Args:
        desconto (int): Percentual de desconto aplicado.
        preco_final (float): Preço final com desconto.
    """
    print(f"\nDesconto aplicado: {desconto}%")
    print(f"Preço final: R$ {preco_final:.2f}")


def main() -> None:
    """
    Função principal que executa o processo de cálculo de desconto.
    """
    preco = obter_preco()
    vip = verificar_vip()
    desconto = calcular_desconto(preco, vip)
    preco_final = calcular_preco_final(preco, desconto)
    mostrar_resultado(desconto, preco_final)


if __name__ == "__main__":
    main()
