from typing import List


def obter_respostas_usuario(tamanho: int = 4) -> List[str]:
    """
    Solicita ao usuário que insira uma sequência de cartas.

    Args:
        tamanho (int): Número de cartas na sequência. Padrão é 4.

    Returns:
        List[str]: Lista com as cartas escolhidas pelo usuário (em letras maiúsculas).
    """
    print("Escolha a sequência de 4 cartas (A, B, C ou D):")
    respostas = []
    for i in range(tamanho):
        carta = input(f"Carta {i + 1}: ").strip().upper()
        while carta not in ('A', 'B', 'C', 'D'):
            print("Entrada inválida. Digite apenas A, B, C ou D.")
            carta = input(f"Carta {i + 1}: ").strip().upper()
        respostas.append(carta)
    return respostas


def calcular_pontuacao(respostas: List[str], gabarito: List[str]) -> int:
    """
    Calcula a pontuação com base nas respostas do usuário e no gabarito.

    Regras:
    - +10 pontos por carta correta na posição correta.
    - +5 pontos por cada ocorrência de 'A'.
    - +5 pontos se 'C' for seguido por 'D' em qualquer posição.
    - Pontuação máxima é 50.

    Args:
        respostas (List[str]): Respostas do usuário.
        gabarito (List[str]): Sequência correta de cartas.

    Returns:
        int: Pontuação final (máximo 50).
    """
    pontos = 0

    # +10 por acerto na posição correta
    for i in range(len(gabarito)):
        if respostas[i] == gabarito[i]:
            pontos += 10

    # +5 por cada 'A'
    pontos += respostas.count('A') * 5

    # +5 se 'C' for seguido por 'D'
    for i in range(len(respostas) - 1):
        if respostas[i] == 'C' and respostas[i + 1] == 'D':
            pontos += 5
            break  # só uma vez

    # Pontuação máxima de 50
    return min(pontos, 50)


def mostrar_resultado(respostas: List[str], gabarito: List[str], pontuacao: int) -> None:
    """
    Exibe a sequência correta, a do usuário e a pontuação final.

    Args:
        respostas (List[str]): Respostas do usuário.
        gabarito (List[str]): Gabarito correto.
        pontuacao (int): Pontuação final.
    """
    print("\nSequência correta:", gabarito)
    print("Sua sequência:", respostas)
    print("Pontuação final:", pontuacao)


def main() -> None:
    """
    Função principal que executa o jogo de cartas e pontuação.
    """
    gabarito = ['B', 'C', 'D', 'A']
    respostas = obter_respostas_usuario()
    pontuacao = calcular_pontuacao(respostas, gabarito)
    mostrar_resultado(respostas, gabarito, pontuacao)


if __name__ == "__main__":
    main()
