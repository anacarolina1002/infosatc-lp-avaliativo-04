#Crie uma função que receba uma palavra por parâmetro e permita inverter a ordem
#dessa palavra. Exemplo: ATOR = ROTA

def parametroNome(nome):
    if (nome==''):  #Declaração de nome como uma string
        return nome #Retorna o nome ao contrário 
    parametroRes = nome[-1] + parametroNome(nome[:-1])
    return parametroRes #Função que decrementa as letras e reescreve ao contrário
print(parametroNome('alan'))#Definição de nome como "Teodoro"