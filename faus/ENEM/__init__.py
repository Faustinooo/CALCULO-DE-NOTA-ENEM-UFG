def linha(a = 33):
    print(f"\033[{a}m=-" * 20)

def texto(a = ""):
    linha()
    print(f"    {a}")
    linha()
    print("\033[m")
def enem(linguagens = 0,CH = 0,CN = 0,MAT= 0,RED = 0):
  #GRUPOS DO 1 AO 5 LING
  lg12345 = linguagens * 0.2
  #GRUPOS DO 6 7
  lg67 = linguagens * 0.25
  #GRUPOS DO 8
  lg8 = linguagens * 0.3


  #GRUPOS DO 1 a 3 e 5
  ch1235 = CH * 0.1
  #GRUPOS DO 4
  ch4 = CH * 0.15
  #GRUPOS DO 6
  ch6 = CH * 0.3
  #GRUPOS DO 7
  ch7 = CH * 0.2
  #GRUPOS DO 8
  ch8 = CH * 0.25

  #GRUPOS DO 1
  cn1 = CN * 0.25
  #GRUPOS DO 2
  cn2 = CN * 0.15
  #GRUPOS DO 3 6 ao 8
  cn3678 = CN * 0.1
  #GRUPOS DO 4 5
  cn45 = CN * 0.3

  #GRUPOS DO 1
  m1 = MAT * 0.3
  #GRUPOS DO 2 3
  m23 = MAT * 0.4
  #GRUPOS DO 4
  m4 = MAT * 0.15
  #GRUPOS DO 5 7
  m57 = MAT * 0.2
  #GRUPOS DO 6 8
  m68 = MAT * 0.1

  #GRUPOS DO 1 2
  r12 = RED * 0.15
  #GRUPOS DO 345
  r345 = RED * 0.2
  #GRUPOS DO 678
  r678 = RED * 0.25
#SOMA PARA MÉDIA DO GRUPO 1
  gp1 = lg12345 + ch1235 + cn1 + m1 + r12
  # SOMA PARA MÉDIA DO GRUPO 2
  gp2 = lg12345 + ch1235 + cn2 + m23 + r12
  # SOMA PARA MÉDIA DO GRUPO 3
  gp3 = lg12345 + ch1235 + cn3678 + m23 + r345
  # SOMA PARA MÉDIA DO GRUPO 4
  gp4 = lg12345 + ch4 + cn45 + m4 + r345
  # SOMA PARA MÉDIA DO GRUPO 5
  gp5 = lg12345 + ch1235 + cn45 + m57 + r345
  # SOMA PARA MÉDIA DO GRUPO 6
  gp6 = lg67 + ch6 + cn3678 + m68 + r678
  # SOMA PARA MÉDIA DO GRUPO 7
  gp7 = lg67 + ch7 + cn3678 + m57 + r678
  # SOMA PARA MÉDIA DO GRUPO 8
  gp8 = lg8 + ch8 + cn3678 + m68 + r678

  #RETORNA OS DADOS PARA IMPRESSÃO NO CONSOLE
  return f'''GRUPO 1: {gp1:>5.2f}
GRUPO 2: {gp2:>5.2f}
GRUPO 3: {gp3:>5.2f}
GRUPO 4: {gp4:>5.2f}
GRUPO 5: {gp5:>5.2f}
GRUPO 6: {gp6:>5.2f}
GRUPO 7: {gp7:>5.2f}
GRUPO 8: {gp8:>5.2f}'''
