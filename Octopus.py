from chatterbot.trainers import ListTrainer #Permite o uso de lista de strings
from chatterbot import ChatBot #Construtor, para criar o programa

bot = ChatBot(
    'Octopus',
    trainer='chatterbot.trainers.ListTrainer'
)

conversa = ['Oi','Olá','Tudo bem?', #Lista de treinamento do boot
            'Tudo ótimo','Você gosta de programar?',
            'Sim, eu programo em Python','Qual seu nome?',
            'Meu nome é Octopus, eu sou um Polvo',
            'Quantos anos você tem?','Eu tenho oito patinhas']

trainer = ListTrainer(bot)
trainer.train(conversa)

print('OCTOPUS')
print('___')
while True:#Loop enquanto for verdadeiro faça
    pergunta = input('EU: ')#Entrada do usuário
    print('___')
    resposta = bot.get_response(pergunta)#Resposta do bot

    if float(resposta.confidence) > 0.5: #Grau de confiança da resposta
        print('OCTUPUS: ', resposta)#Resposta do bot
        print('___')

    #elif float(resposta.confidence) < 0.5:  #Grau de confiança da resposta


    else:
        print('OCTUPUS: Ainda não sei responder está pergunta')
        conversa.append(str(input('Repita a Pergunta: ')))#Entrada do usuário adicionando na lista
        conversa.append(str(input('Como você Responderia: ')))#Entrada do usuário adicionando na lista
        print(conversa)
        print('Aprendi, Obrigado!')
        print('___')