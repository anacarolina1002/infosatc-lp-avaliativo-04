#Crie uma função que receba por parâmetro DUAS palavras e verifique se uma é o
#inverso da outra. 
#No if tentei usar esse comando nome[-1] + parametroNome(nome[:-1]):, 
#que usei no primeiro exercício mas não funcionou e eu não sei o porquê.
#Aí achei na internet esse comando[::-1] que é bem mais fácil e eu podia ter usado no 
#primeiro exercício mas não achei antes kkk cada k é uma lágrima.
nome=("Alice") 
nomeInverso=("ecilA")#Aqui pode alterar e botar qualquer valor pra testar o False
def parametroNome(nome,nomeInverso):
    if nomeInverso == nome[::-1]:
        print("O nome",nomeInverso,"é o inverso de",nome)
        return True
    else:
        print("O nome",nomeInverso,"não é o inverso de",nome)
        return False
print(parametroNome(nome,nomeInverso))