def avaliar_aluno(nota1: float, nota2: float, nota3: float) -> str:
    """
    Avalia o desempenho de um aluno com base em três notas.

    Se alguma nota for zero, o aluno é reprovado automaticamente.
    Caso contrário, a média é calculada e a classificação é feita.

    Args:
        nota1 (float): Primeira nota.
        nota2 (float): Segunda nota.
        nota3 (float): Terceira nota.

    Returns:
        str: Resultado da avaliação ("Reprovado automaticamente",
             "Aprovado", "Recuperação" ou "Reprovado").
    """
    if nota1 == 0 or nota2 == 0 or nota3 == 0:
        return "Reprovado automaticamente. (Zerado)"
    
    media = (nota1 + nota2 + nota3) / 3
    print(f"Média: {media:.2f}")

    if media >= 7:
        return "Aprovado"
    elif media >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


def exibir_resultado():
    """
    Solicita as três notas do aluno, avalia o desempenho e exibe o resultado.
    """
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))

    resultado = avaliar_aluno(nota1, nota2, nota3)
    print(f"Resultado: {resultado}")


if __name__ == "__main__":
    exibir_resultado()
