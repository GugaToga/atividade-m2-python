def calcular_bonus(salario: float, tempo: int) -> dict:
    """
    Calcula o bônus salarial com base no salário e tempo de empresa.

    Args:
        salario (float): Salário atual do funcionário.
        tempo (int): Tempo de empresa em anos.

    Returns:
        dict: Contém salário, tempo de empresa, bônus e total a receber.
    """
    if salario < 2000 and tempo >= 5:
        bonus = salario * 0.20
    elif salario < 2000 and tempo < 5:
        bonus = salario * 0.10
    elif salario >= 2000 and tempo >= 5:
        bonus = salario * 0.05
    else:
        bonus = 0

    total = salario + bonus

    return {
        "salario": salario,
        "tempo": tempo,
        "bonus": bonus,
        "total": total
    }


def exibir_resultado():
    """
    Função para entrada de dados via usuário e exibição formatada.
    """
    salario = float(input("Digite o salário do funcionário: R$ "))
    tempo = int(input("Digite o tempo de empresa (em anos): "))
    resultado = calcular_bonus(salario, tempo)

    print(f"\nSalário: R$ {resultado['salario']:.2f}")
    print(f"Tempo de empresa: {resultado['tempo']} anos")
    print(f"Bônus: R$ {resultado['bonus']:.2f}")
    print(f"Total a receber: R$ {resultado['total']:.2f}")


if __name__ == "__main__":
    exibir_resultado()


