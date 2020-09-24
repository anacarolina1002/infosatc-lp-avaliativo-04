#Crie uma função que receba uma palavra por parâmetro e permita inverter a ordem
#dessa palavra. Exemplo: ATOR = ROTA
#Só nessa atividade tem vários commits pq usei ela pra me ajudar no próximo exercício
#pra ver como ficavam as palavras ao contrário pra usar lá
#e tbm pq uma hora commitei tudo junto e fiz bagunça
def parametroNome(nome):
    if (nome==''):  #Declaração de nome como uma string
        return nome #Retorna o nome ao contrário 
    parametroRes = nome[-1] + parametroNome(nome[:-1])
    return parametroRes #Função que decrementa as letras e reescreve ao contrário
print(parametroNome('Alice'))#Definição de nome como "Alice"