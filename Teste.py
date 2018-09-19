import sys
nome = str(input('Qual seu nome? '))
lista = ('PROGRAMADOR', 'MÉDICO', 'ADVOGADO')
print('''[ 1 ] PROGRAMADOR
[ 2 ] MÉDICO
[ 3 ] ADVOGADO''')
profissional = int(input('QUAL SUA FUTURA PROFISÃO?'))
if profissional == 1:
    profissional = 'PROGRAMADOR'
if profissional == 2:
    profissional = 'MÉDICO'
if profissional == 3:
    profissional = 'ADVOGADO'
if profissional != 1 or 2 and 3:
    print('\033[31mOPÇÃO INVÁLIDA\033[m')
    sys.exit();
print('{} você será com certeza um ótimo {}'.format(nome, profissional))
