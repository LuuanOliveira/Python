import playsound
import sys
print('\033[32m--DESCUBRA SEU SIGNO--\033[m')
print('\033[36m|\033[m')
nome = str(input('\033[30mQual seu nome ? \033[m')).upper()
if nome == ' '.strip():
    print('\033[31m=' * 30, '\033[m')
    print('\033[31mNOME INVÁLIDO\033[m')
    playsound.playsound('signos.mp3') # Som Erro
    sys.exit();
for letter in nome:
    if letter.isdigit():
        print('\033[31m=' * 30, '\033[m')
        print('\033[31mNOME INVÁLIDO\033[m')
        playsound.playsound('signos.mp3') # Som Erro
        sys.exit();
while True:
    try:
        dia = int(input('\033[30mDigite o DIA do seu nascimento: \033[m'))
        if dia > 31:
            print('\033[31m=' * 30, '\033[m')
            print('\033[31mDIA DE NASCIMENTO INVÁLIDO\033[m')
            playsound.playsound('signos.mp3') # Som Erro
            sys.exit();
        mes = int(input('\033[30mDigite o MÊS do seu nascimento: \033[m'))
        if mes > 12:
            print('\033[31m=' * 30, '\033[m')
            print('\033[31mMÊS DE NASCIMENTO INVÁLIDO\033[m')
            playsound.playsound('signos.mp3') # Som Erro
            sys.exit();
        if mes == 1:
            mes = 'JANEIRO'
        if mes == 2:
            mes = 'FEVEREIRO'
        if mes == 3:
            mes = 'MARÇO'
        if mes == 4:
            mes = 'ABRIL'
        if mes == 5:
            mes = 'MAIO'
        if mes == 6:
            mes = 'JUNHO'
        if mes == 7:
            mes = 'JULHO'
        if mes == 8:
            mes = 'AGOSTO'
        if mes == 9:
            mes = 'SETEMBRO'
        if mes == 10:
            mes = 'OUTUBRO'
        if mes == 11:
            mes = 'NOVEMBRO'
        if mes == 12:
            mes = 'DEZEMBRO'
        ano = int(input('\033[30mDigite o ANO do seu nascimento: \033[m'))
        print('\033[36m|\033[m')
        if ano < 1900:  # Usuário pode ter no máximo 118 anos
            print('\033[31m=' * 30, '\033[m')
            playsound.playsound('signos.mp3') # Som Erro
            print('\033[31mANO DE NASCIMENTO INVÁLIDO\033[m')
            sys.exit();
        break
    except ValueError:
        print('\033[31m=' * 30, '\033[m')
        print('\033[31mFORMATO INVÁLIDO DD/MM/AAA\033[m')
        playsound.playsound('signos.mp3') # Som Erro
        sys.exit();
result = 2018 - ano  # Calculo da idade do usuário
print('\033[35m{} você nasceu no Dia {} De {} De {},\033[35m'.format(nome, dia, mes, ano))
print('\033[36m|\033[m')
print('\033[32m=' * 30, '\033[m')
if result <= 1:
    print('\033[34mVocê tem {} Ano\033[m'.format(result))
else:
    print('\033[34mVocê tem {} Anos\033[m'.format(result))
if result: # Print quando obter o resuldado
    if mes == 'JANEIRO' and dia > 20 or mes == 'FEVEREIRO' and dia < 21:
        print('Seu Signo é AQUÁRIO: ')
    if mes == 'FEVEREIRO' and dia > 20 or mes == 'MARÇO' and dia < 21:
        print('Seu Signo é PEIXES: ')
    if mes == 'MARÇO' and dia > 20 or mes == 'ABRIL' and dia < 21:
        print('Seu Signo é ÁRIES: ')
    if mes == 'ABRIL' and dia > 20 or mes == 'MAIO' and dia < 21:
        print('Seu Signo é TOURO: ')
    if mes == 'MAIO' and dia > 20 or mes == 'JUNHO' and dia < 21:
        print('Seu Signo é GÊMEOS: ')
    if mes == 'JUNHO' and dia > 20 or mes == 'JULHO' and dia < 21:
        print('Seu Signo é CÂNCER: ')
    if mes == 'JULHO' and dia > 20 or mes == 'AGOSTO' and dia < 21:
        print('Seu Signo é LEÃO: ')
    if mes == 'AGOSTO' and dia > 20 or mes == 'SETEMBRO' and dia < 21:
        print('\033[32m=' * 30, '\033[m')
        print('\033[30mSeu Signo é VIRGEM: \n\nVirgem é um signo do elemento Terra, são marcados pela lentidão e por \nprecisarem de segurança.'
              'Todos os signos do zodíaco ligado ao elemento possuem uma ótima relação com a comida. \n'
              'Assim como a terra, são firmes, estáveis e sólidos. Até mesmo nos momentos em que as pessoas mais se deixam \nlevar pelas emoções, '
              'Esse signo prefere apostar na sua estabilidade. Não somente em virgem mas também os outros signos do horóscopo \nque são regidos pelo elemento terra,'
              'São muito cuidadosos e excessivamente críticos em suas relações interpessoais, ainda mais quando se trata de amor e sexo.\033[m')
    if mes == 'SETEMBRO' and dia > 20 or mes == 'OUTUBRO' and dia < 21:
        print('Seu Signo é LIBRA: ')
    if mes == 'OUTUBRO' and dia > 20 or mes == 'NOVEMBRO' and dia < 21:
        print('Seu Signo é ESCORPIÃO: ')
    if mes == 'NOVEMBRO' and dia > 20 or mes == 'DEZEMBRO' and dia < 21:
        print('Seu Signo é SAGITÁRIO: ')
    if mes == 'DEZEMBRO' and dia > 20 or mes == 'JANEIRO' and dia < 21:
        print('Seu Signo é CAPRICÓRNIO: ')