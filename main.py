####
temperatura = int(input("Escreva sua temperatura"))
mensagem = input('Deseja continuar?')
opções= ("Não")
while mensagem =='Sim':
    temperatura = int(input("Escreva sua temperatura"))
if mensagem == 'Não':
    print('Finalizado:')
if temperatura >=38:
    print('Você está com febre')
elif temperatura <=37:
    print('Você não está com febre')



