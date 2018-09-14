import emoji
import sys
from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''\033[30mSUAS OPÇÕES
[ 0 ] PEDRA 
[ 1 ] PAPEL
[ 2 ] TESOURA\033[m''')
while True:
    try:
        jogador = int(input('\033[30mQual sua jogada: \033[m'))
        if jogador > 2:
            print(emoji.emojize('\033[31m==JOGADA INVÁLIDA :loudspeaker: ==\033[m', use_aliases=True))
            sys.exit();
        break
    except ValueError:
        print(emoji.emojize('\033[31m==JOGADA INVÁLIDA :loudspeaker: ==\033[m', use_aliases=True))
        sys.exit();
print('\033[35mJO\033[m')
sleep(1)
print('\033[36mKEN\033[m')
sleep(1)
print('\033[31mPÔ\033[m')
print('\033[33m-=' * 11, '\033[m')
print('Computador Jogou {}'.format(itens[computador]))
print('Jogador Jogou {}'.format(itens[jogador]))
print('\033[33m-=' * 11, '\033[m')
if computador == jogador:
        print('\033[35mEMPATE\033[m')
if computador == 0:
    if jogador == 1:
        print('\033[34mVOCÊ VENDEU\033[m')
if computador == 2:
    if jogador == 0:
        print('\033[34mVOCÊ VENCEU\033[m')
if computador == 1:
    if jogador == 0:
        print('\033[31mCOMPUTADOR VENCEU\033[m')
if computador == 0:
    if jogador == 2:
        print('\033[31mCOMPUTADOR VENCEU\033[m')
if computador == 2:
    if jogador == 1:
        print('\033[31mCOMPUTADOR VENCEU\033[m')
if computador == 1:
    if jogador == 2:
        print('\033[34mVOCÊ VENCEU\033[m')