# main.py - menu principal de execução dos exercícios
import os, sys

# Garante que o diretório atual está no sys.path
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
if SCRIPT_DIR not in sys.path:
    sys.path.insert(0, SCRIPT_DIR)

import utils


def main():
    while True:
        print("\n=== MENU PRINCIPAL ===")
        print("1 - Calcular Bônus")
        print("2 - Classificar Triângulo")
        print("3 - Calcular IMC")
        print("4 - Avaliar Aluno")
        print("5 - Validar Data")
        print("6 - Verificar Direito ao Voto")
        print("7 - Avaliar Risco Financeiro")
        print("8 - Jogo das Cartas")
        print("9 - Calcular Desconto")
        print("10 - Verificar Senha")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "0":
            print("Saindo...")
            break

        func = getattr(utils, f"executar_exercicio_{opcao}", None)
        if func:
            try:
                func()
            except Exception as e:
                print(f"Erro ao executar o exercício {opcao}: {e}")
        else:
            print("Opção inválida!")


if __name__ == "__main__":
    main()
