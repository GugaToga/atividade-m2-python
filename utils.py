from EXERCICIO1 import calcular_bonus
from EXERCICIO2 import classificar_triangulo
from EXERCICIO3 import calcular_imc
from EXERCICIO4 import avaliar_aluno
from EXERCICIO5 import validar_data
from EXERCICIO6 import verificar_direito_ao_voto
from EXERCICIO7 import calcular_percentual_divida, classificar_risco
from EXERCICIO8 import calcular_pontuacao
from EXERCICIO9 import calcular_desconto, calcular_preco_final
from EXERCICIO10 import validar_senha

def executar_exercicio_1():
    salario = float(input("Salário: "))
    tempo = int(input("Tempo de empresa (anos): "))
    print(calcular_bonus(salario, tempo))

def executar_exercicio_2():
    lados = [float(input(f"Lado {i+1}: ")) for i in range(3)]
    print(classificar_triangulo(*lados))

def executar_exercicio_3():
    peso = float(input("Peso (kg): "))
    altura = float(input("Altura (m): "))
    print(calcular_imc(peso, altura))

def executar_exercicio_4():
    notas = [float(input(f"Nota {i+1}: ")) for i in range(3)]
    print(avaliar_aluno(*notas))

def executar_exercicio_5():
    dia = int(input("Dia: "))
    mes = int(input("Mês: "))
    ano = int(input("Ano: "))
    print(validar_data(dia, mes, ano))

def executar_exercicio_6():
    idade = int(input("Idade: "))
    nacionalidade = int(input("Nacionalidade (1=Brasileiro, 2=Estrangeiro): "))
    print(verificar_direito_ao_voto(idade, nacionalidade))

def executar_exercicio_7():
    renda = float(input("Renda mensal: "))
    dividas = float(input("Dívidas totais: "))
    percentual = calcular_percentual_divida(dividas, renda)
    print(f"Percentual dívida: {percentual:.2f}% -> {classificar_risco(renda, percentual)}")

def executar_exercicio_8():
    gabarito = ['B', 'C', 'D', 'A']
    respostas = [input(f"Carta {i+1}: ").upper() for i in range(4)]
    print(f"Pontuação: {calcular_pontuacao(respostas, gabarito)}")

def executar_exercicio_9():
    preco = float(input("Preço: "))
    vip = input("Cliente VIP? (s/n): ").lower() == 's'
    desconto = calcular_desconto(preco, vip)
    print(f"Preço final: {calcular_preco_final(preco, desconto):.2f} (Desconto {desconto}%)")

def executar_exercicio_10():
    senha = input("Digite a senha: ")
    print("Senha válida!" if validar_senha(senha) else "Senha inválida!")
