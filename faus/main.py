# importa do módulo ENEM todas as funções contidas
from ENEM import *

# exibe um texto para informar que se trata da calculadora de nota do ENEM
texto("CALCULADORA DE NOTA ENEM (UFG)")

# solicita a nota obtida na prova de Linguagens, repetindo a solicitação caso a nota seja inválida
while True:
    linguagens = str(input("Nota na Prova De Linguagens: ")).replace(",", ".")
    if linguagens == "" or linguagens.isalpha():
        print(f"\033[31mHOUVE UM ERRO, INFORME NOVAMENTE A NOTA.\033[m")
        continue
    break

# solicita a nota obtida na prova de Ciências Humanas, repetindo a solicitação caso a nota seja inválida
while True:
    CH = str(input("Nota na Prova De Ciências Humanas: ")).replace(",", ".")
    if CH == "" or CH.isalpha():
        print(f"\033[31mHOUVE UM ERRO, INFORME NOVAMENTE A NOTA.\033[m")
        continue
    break

# solicita a nota obtida na prova de Ciências da Natureza, repetindo a solicitação caso a nota seja inválida
while True:
    CN = str(input("Nota na Prova De Ciências Da Natureza: ")).replace(",", ".")
    if CN == "" or CN.isalpha():
        print(f"\033[31mHOUVE UM ERRO, INFORME NOVAMENTE A NOTA.\033[m")
        continue
    break

# solicita a nota obtida na prova de Matemática, repetindo a solicitação caso a nota seja inválida
while True:
    MAT = str(input("Nota na Prova De Matemática: ")).replace(",", ".")
    if MAT == "" or MAT.isalpha():
        print(f"\033[31mHOUVE UM ERRO, INFORME NOVAMENTE A NOTA.\033[m")
        continue
    break

# solicita a nota obtida na redação, repetindo a solicitação caso a nota seja inválida
while True:
    RED = str(input("Nota na Prova De Redação: ")).replace(",", ".")
    if RED.isdigit() or RED != ",":
        pass
    else:
        print(f"\033[31mHOUVE UM ERRO, INFORME NOVAMENTE A NOTA.\033[m")
        continue
    print("")
    break


# chama a função enem do módulo ENEM, passando as notas como parâmetros
f = enem(float(linguagens), float(CH), float(CN), float(MAT), float(RED))

# exibe as médias das notas no console, separadas por uma linha
linha(36)
print("NOTAS:\n")
print(f)
linha(36)
print("\033[m")