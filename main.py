from enum import Enum

nome = "Cleiton"
idade = 20
sexo = "m"
peso = 70.5
ativo = True

# val1, val2, adicao, subtracao, multiplicacao, divisao, modulo
# idadeTernario
# idadeIF
# dia
a = 0
b = 0
c = 0
m = 0
n = 0

# Constante
PI = 3.14159265

# Comentário de uma linha

""" Comentário
  de varias linhas
"""

# ESCREVER NA TELA
print("### ESCREVER NA TELA ###\n")
print("Olá Mundo")
print("\n")

# VARIÁVEIS
print("### VARIÁVEIS E TIPOS BÁSICOS ###\n")
print("Nome: ", nome, "\n")
print("Idade: ", idade, "\n")
print("Sexo: ", sexo, "\n")
print("Peso: ", peso, "\n")
print("Ativo: ", ativo)
print("\n")

# CONSTANTE
print("### CONSTANTE ###\n")
print("PI: ", PI)
print("\n")

# OPERACOES
print("#### OPERACOES #### \n")
val1 = int(input("Informe o valor 1: "))
val2 = int(input("Informe o valor 2: "))

adicao = val1 + val2 # Pode usar: (+, -, *, /, %)
subtracao = val1 - val2
multiplicacao = val1 * val2
divisao = val1 / val2
modulo = val1 % val2
print("Soma: ", adicao, "\n")
print("Subtracao: ", subtracao, "\n")
print("Multiplicacao: ", multiplicacao, "\n")
print("Divisao: ", divisao, "\n")
print("Modulo: ", modulo)
print("\n")

# TERNARIO
print("### TERNARIO \n")
idadeTernario = int(input("Digite um número: "))
print ("Maior de idade\n" if idadeTernario >= 18 else "Menor de idade\n")
print("\n")

# IF ELSE IF ELSE
print("### IF ELSE IF ELSE \n")
idadeIF = int(input("Informe a idade: "))
if (idadeIF < 12):
  print("CRIANCA \n")
elif ((idadeIF >= 12) and (idadeIF < 18)):
  print("ADOLESCENTE \n")
else:
  print("ADULTO \n")
print("\n")

#  CASE
print("### SWITCH CASE \n")
dia = int(input("Informe um numero 1 - 7 para semana: "))
match (dia):
  case 1:
    print("Domingo")

  case 2:
    print("Segunda")

  case 3:
    print("Terça")

  case 4:
    print("Quarta")

  case 5:
    print("Quinta")

  case 6:
    print("Sexta")

  case 7:
    print("Sabado")
    
  case _:
    print("Valor nao existente")
print("\n")

# REPEAT
print("### REPEAT ### \n")
print("Não tem REPEAT \n")
print("\n")

# DO WHILE
"""
print("### DO WHILE ### \n");
do:
  print("\n", a)
  a = a + 1
while (a < 10)
print("\n")
"""

# WHILE
print("### WHILE ###")
while (b < 10):
  print(b)
  b = b + 1
print("\n")

# FOR
print("### FOR ### \n")
for c in range(0, 10, 1):
  print(c)
print("\n")

# ARRAY
print("### ARRAY ###")
numbers = [10, 20, 30, 40]

for number in numbers:
    print(number)
print()

# MATRIZ
print("### MATRIZ ###")
matriz = [[0] * 3 for _ in range(3)]  # Declaração de uma matriz 3x3 de inteiros

# Inicialização da matriz
for i in range(3):
    for j in range(3):
        matriz[i][j] = i * 3 + j + 1

# Acesso aos elementos da matriz
print("Elementos da matriz:")
for row in matriz:
    print(' '.join(map(str, row)))
print()

# FUNÇÃO
print("### FUNCAO ### \n");
m = int(input("Digite o valor 1: "))
n = int(input("Digite o valor 2: "))

def funcao_soma(m,n):
    return m + n

print("Soma ", funcao_soma(m,n));

print("\n");

# PROCEDURE
print("### PROCEDURE ###");
print("Não tem PROCEDURE");
print("");

# PONTEIRO
print("### PONTEIRO ###\n");
print("Não tem PONTEIRO \n");
print(" Não é necessário liberar memória manualmente, como em C ou C++. A variável será automaticamente coletada pelo coletor de lixo quando não estiver mais em uso. \n");
print("\n");


# TRY
print("### TRY ###\n");
try:
    numero1 = int(input('Digite o valor 1 para o dividendo: '))
    numero2 = int(input('Digite o valor 2 para o divisor: '))
    
    if numero2 == 0:
        raise Exception('Divisão por zero não é permitida!')
    
    res = numero1 / numero2
    print(f'Resultado da divisão: {res}')
except ValueError:
    print('Entrada inválida!')
except Exception as e:
    print(f'Ocorreu uma exceção: {e}')

print("\n");

# ENUM
print("### ENUM ###\n");
class Cor(Enum):
    Vermelho = 1
    Verde = 2
    Azul = 3
    Amarelo = 4
    Laranja = 5

minha_cor = Cor.Azul

if minha_cor == Cor.Vermelho:
    print("Minha cor favorita é vermelho.")
elif minha_cor == Cor.Verde:
    print("Minha cor favorita é verde.")
elif minha_cor == Cor.Azul:
    print("Minha cor favorita é azul.")
elif minha_cor == Cor.Amarelo:
    print("Minha cor favorita é amarelo.")
elif minha_cor == Cor.Laranja:
    print("Minha cor favorita é laranja.")
else:
    print("Eu não tenho uma cor favorita.")

print("\n");
