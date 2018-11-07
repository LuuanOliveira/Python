from chatterbot.trainers import ListTrainer #Permite o uso de lista de strings
from chatterbot import ChatBot #Construtor, para criar o programa


bot = ChatBot(
    'Octopus Chat Bot',
    trainer='chatterbot.trainers.ListTrainer'
)

conversa = ['Oi','Olá','Tudo bem?','Tudo ótimo','Você gosta de programar?','Sim, eu programo em Python','Qual seu nome?','Meu nome é Octopus, eu sou um Polvo','Quantos anos você tem?','Eu tenho oito patinhas']

bot.set_trainer(ListTrainer)
bot.train(conversa)

print('\033[35mOCTOPUS CHATBOT\033[m')
print('\033[31m ___\033[m')
while True: #Loop

    pergunta = input('\033[32mUsuário: \033[m')#Entrada do usuário
    print('\033[34m--- \033[m')
    resposta = bot.get_response(pergunta)#Resposta do bot

    if float(resposta.confidence) > 0.5: #Grau de confiança da resposta
        print('\033[36mOctopus: \033[m', resposta)
        print('\033[31m ___\033[m')
    else:
        print('\033[36mOctopus: \033[m','\033[31mAinda não sei responder está pergunta\033[m')