def classificar_triangulo(lado1: float, lado2: float, lado3: float) -> str:
    """
    Classifica um triângulo com base nos três lados fornecidos.

    Args:
        lado1 (float): Comprimento do primeiro lado.
        lado2 (float): Comprimento do segundo lado.
        lado3 (float): Comprimento do terceiro lado.

    Returns:
        str: Tipo de triângulo ("equilátero", "isósceles", "escaleno") ou
             mensagem de erro caso não forme um triângulo.
    """
    if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
        if lado1 == lado2 == lado3:
            return "Triângulo equilátero"
        elif lado1 == lado2 or lado1 == lado3 or lado2 == lado3:
            return "Triângulo isósceles"
        else:
            return "Triângulo escaleno"
    else:
        return "Os lados informados não formam um triângulo"


def exibir_resultado():
    """
    Solicita os lados do triângulo ao usuário, classifica e exibe o resultado.
    """
    lado1 = float(input("Digite o primeiro lado: "))
    lado2 = float(input("Digite o segundo lado: "))
    lado3 = float(input("Digite o terceiro lado: "))

    resultado = classificar_triangulo(lado1, lado2, lado3)
    print(f"\nResultado: {resultado}")


if __name__ == "__main__":
    exibir_resultado()
1