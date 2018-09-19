import emoji
import sys
import playsound
print('\033[34mFILA\033[m')
print('\033[36m|\033[m')
ListaMembros = []
finish = ' ';
i = 1
while finish != True: # Se finish for diferente de vazio
    membro = input('Jogador N° '+str(i)+ ': ').upper().strip().lstrip().rstrip()
    i = i+1
    if membro == ' '.strip(): # Se nome for vazio == ERRO
        print(emoji.emojize('\033[31m==NOME INVÁLIDO :no_entry: ==\033[m', use_aliases=True))
        playsound.playsound('signos.mp3')  # Som Erro
        sys.exit();
    for letter in membro: # laço para verificar se o nome possui numeros
        if letter.isdigit():
            print(emoji.emojize('\033[31m==NOME INVÁLIDO :no_entry: ==\033[m', use_aliases=True))
            playsound.playsound('signos.mp3')  # Som Erro
            sys.exit();
    if len(ListaMembros) >= 1:
        lista = ('SIM', 'NÃO')
        print('\033[33m=' * 20, '\033[m')
        print('''\033[30mMAIS ALGUM JOGADOR
        [ 1 ] SIM
        [ 2 ] NÃO\033[m''')
        try:
            proximo = int(input('\033[30m? \033[m'))
        except ValueError:
            print(emoji.emojize('\033[31m==OPÇÃO INVÁLIDA :loudspeaker:\033[m', use_aliases=True))
            playsound.playsound('signos.mp3') # Som Erro
            sys.exit();
            print('\033[33m=' * 20, '\033[m')
            print('''\033[30mMAIS ALGUM JOGADOR
            [ 1 ] SIM
            [ 2 ] NÃO\033[m''')
            try:
                proximo = int(input('\033[30m? \033[m'))
            except ValueError:
                print(emoji.emojize('\033[31m==OPÇÃO INVÁLIDA== :loudspeaker:\033[m', use_aliases=True))
                playsound.playsound('signos.mp3')  # Som Erro
                sys.exit();
        if proximo > 2:
            print(emoji.emojize('\033[31m==OPÇÃO INVÁLIDA== :loudspeaker: \033[m', use_aliases=True))
            playsound.playsound('signos.mp3')  # Som Erro
            sys.exit();
            print('\033[33m=' * 20, '\033[m')
            print('''\033[30mMAIS ALGUM JOGADOR
            [ 1 ] SIM
            [ 2 ] NÃO\033[m''')
            try:
                proximo = int(input('\033[30m? \033[m'))
            except ValueError:
                print(emoji.emojize('\033[31m==OPÇÃO INVÁLIDA== :loudspeaker:\033[m', use_aliases=True))
                playsound.playsound('signos.mp3')  # Som Erro
                sys.exit();
                print('\033[33m=' * 20, '\033[m')
                print('''\033[30mMAIS ALGUM JOGADOR
                [ 1 ] SIM
                [ 2 ] NÃO\033[m''')
                proximo = int(input('\033[30m? \033[m'))
                if proximo > 2:
                    print(emoji.emojize('\033[31m==OPÇÃO INVÁLIDA== :loudspeaker:\033[m', use_aliases=True))
                    playsound.playsound('signos.mp3')  # Som Erro
                    sys.exit();
        if proximo == 2:
            finish = True
    ListaMembros.append(membro) # metodo para inserir depois
def runGame(data): # Chamada da função
    players = [];
    players.append(data[0])
    players.append(data[1])
    i = 1
    venc = []
    for player in players: # Para cada jogador, imprima o jogador
        print(player+' \033[36mé o Jogador Número:  \033[m' + str(i))
        i = i + 1;
        venc.append(player) # Acrescentar Jogador
    print('\033[33m=' * 20, '\033[m')
    print('''\033[30m[ 1 ] {}\n[ 2 ] {}\033[m'''.format(venc[0], venc[1]))
    try:
        result = int(input('\033[34mQUEM VENCEU ? \033[34m'))
    except ValueError:
        print(emoji.emojize('\033[31m==OPÇÃO INVÁLIDA :loudspeaker:\033[m', use_aliases=True))
        playsound.playsound('signos.mp3')  # Som Erro
        sys.exit();
    if result == 1:
        result = 2
    elif result == 2:
        result = 1
    result = result - 1;
    print('\033[33m=' * 20, '\033[m')
    print('''\033[30mENTROU MAIS ALGUEM?\n[ 1 ] SIM\n[ 2 ] NÃO\033[m''')
    more = int(input('\033[35mINSIRA À OPÇÃO: \033[m'))
    if more == 1:
        addedPlayer = str(input('\033[36mINSIRA O NOME DO JOGADOR: \033[m')).upper().strip().lstrip().rstrip()
        ListaMembros.append(addedPlayer)
        finishAdding = ' '
        while finishAdding != True:
            print('''\033[30mMAIS ALGUEM?\n[ 1 ] SIM\n[ 2 ] NÃO\033[m''')
            continueToAdd = int(input('\033[35mINSIRA À OPÇÃO: \033[m'))
            if continueToAdd == 1:
                more1 = str(input('\033[36mINSIRA O NOME DO JOGADOR: \033[m')).upper().strip().lstrip().rstrip()
                ListaMembros.append(more1)
            elif continueToAdd == 2:
                finishAdding = True
            elif continueToAdd > 2:
                print('\033[31m==VOCÊ É BOBO?==\033[m')
                sys.exit()
    loser = players[result]
    print('\033[33m=' * 20, '\033[m')
    print(emoji.emojize(loser + '\033[31m--PERDEU-- :loudspeaker:\033[m', use_aliases=True))
    if len(data) > 2:
        print('\033[36m|\033[m')
        print(data[2]+' \033[35m--ENTRA AGORA--\033[m')
        print('\033[33m=' * 20, '\033[m')
        print('\033[36mLISTA DE PRÓXIMOS: \033[m')
        if len(data) > 3:
            print(' - '+data[3])
        if len(data) > 4:
            print(' - '+data[4])
        if len(data) > 5:
            print(' - '+data[5])
    print('\033[35m=' * 20, '\033[m')
    i = 0;
    if len(ListaMembros) > 2:
        for membro in ListaMembros:
            if membro == loser:
                del ListaMembros[i];
                ListaMembros.append(loser)
                break
            else:
                i = i+1;
# runAgain = ' '
# while runAgain != True:
while True:
    runGame(ListaMembros)
    sleep(3)
    # print('''\033[30
    # [ 1 ] SIM
    # [ 2 ] NÃO\033[m''')
    # try:
    #     again = int(input('Jogar Novamente?:'))
    # except ValueError:
    #     print(emoji.emojize('\033[31m==OPÇÃO INVÁLIDA :loudspeaker: ==\033[m', use_aliases=True))
    #     playsound.playsound('signos.mp3')  # Som Erro
    #     sys.exit();
    # if again == 2:
    #     runAgain = True