def calcular_imc(peso: float, altura: float) -> tuple[float, str]:
    """
    Calcula o Índice de Massa Corporal (IMC) e retorna a classificação.

    Args:
        peso (float): Peso da pessoa em quilogramas.
        altura (float): Altura da pessoa em metros.

    Returns:
        tuple[float, str]: IMC arredondado e sua respectiva classificação.
    """
    imc = peso / (altura * altura)
    imc_arredondado = round(imc, 2)

    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc < 25:
        classificacao = "Peso normal"
    elif imc < 30:
        classificacao = "Sobrepeso"
    elif imc < 35:
        classificacao = "Obesidade grau I"
    elif imc < 40:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"

    return imc_arredondado, classificacao


def exibir_resultado():
    """
    Solicita peso e altura do usuário, calcula IMC e exibe a classificação.
    """
    peso = float(input("Digite seu peso (kg): "))
    altura = float(input("Digite sua altura (m): "))

    imc, classificacao = calcular_imc(peso, altura)

    print(f"\nSeu IMC é: {imc}")
    print(f"Classificação: {classificacao}")


if __name__ == "__main__":
    exibir_resultado()
