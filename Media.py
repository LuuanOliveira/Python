import sys
print('\033[32m=== UNIVERSIDADE ===\033[m')
nome = str(input('\033[30mNome do Aluno: \033[m')).upper()
if nome == ' '.strip():  # Verificação caso o campo nome esteja vazio
    print('\033[31m=' * 20, '\033[m')
    print('\033[31mNOME INVÁLIDO\033[m')
    sys.exit();
for letter in nome:  # Verificação caso o campo nome receba um valor int
    if letter.isdigit():
        print('\033[31m=' * 20, '\033[m')
        print('\033[31mNOME INVÁLIDO\033[m')
        sys.exit();
while True:
    try:
        ra = int(input('\033[30mR.A do Aluno: \033[m'))
        if ra == ' '.strip():  # Verificação caso o campo RA esteja vazio
            print('\033[31m=' * 20, '\033[m')
            print('\033[31mR.A INVÁLIDO\033[m')
            sys.exit();
        break
    except ValueError:
        print('\033[31m=' * 20, '\033[m')
        print('\033[31mR.A INVÁLIDO\033[m')
        sys.exit();
print('\033[32m======================\033[m')
nota1 = float(input('\033[30m1º Nota: \033[m'))
if nota1 > 10:
    print('\033[31m=' * 30, '\033[m')
    print('\033[31mNOTA INVÁLIDA, VALOR MAXÍMO 10\033[m')
    sys.exit();
nota2 = float(input('\033[30m2° Nota: \033[m'))
if nota2 > 10:
    print('\033[31m=' * 30, '\033[m')
    print('\033[31mNOTA INVÁLIDA, VALOR MAXÍMO 10\033[m')
    sys.exit();
result = (nota1 + nota2) / 2
print('\033[32m======================\033[m')
if result >= 7:
    print('{} RA: {}'.format(nome, ra))
    print('\033[36m|\033[m')
    print('Sua média foi {} você está \033[34mAPROVADO\033[m'.format(result))
elif result < 4:
    print('{} RA: {}'.format(nome, ra))
    print('\033[36m|\033[m')
    print('Sua média foi {} você está \033[31mREPROVADO\033[m'.format(result))
elif result == 4 or 5 and 6:
    print('{} RA: {}'.format(nome, ra))
    print('\033[36m|\033[m')
    print('Sua média foi {} você está de \033[35mEXAME\033[m'.format(result))