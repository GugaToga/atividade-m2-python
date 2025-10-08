def validar_data(dia: int, mes: int, ano: int) -> str:
    """
    Verifica se a data informada é válida, considerando dias do mês, mês, ano e ano bissexto.

    Args:
        dia (int): Dia do mês.
        mes (int): Mês do ano.
        ano (int): Ano com quatro dígitos.

    Returns:
        str: "Data válida!" ou mensagem indicando o motivo da invalidez.
    """
    if ano < 0 or ano > 2025:
        return "Data inválida (Ano fora do permitido)."
    
    if mes < 1 or mes > 12:
        return "Data inválida (Mês inexistente)."
    
    dias_por_mes = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    # Verifica ano bissexto
    if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
        dias_por_mes[2] = 29

    if dia < 1 or dia > dias_por_mes[mes]:
        return "Data inválida (Dia inexistente)."

    return "Data válida!"


def exibir_resultado():
    """
    Solicita uma data do usuário e exibe se ela é válida ou inválida.
    """
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))

    resultado = validar_data(dia, mes, ano)
    print(f"\n{resultado}")


if __name__ == "__main__":
    exibir_resultado()
