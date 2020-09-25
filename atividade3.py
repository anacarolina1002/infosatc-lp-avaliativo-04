#No eaercício da última semana, de desenvolver um sistema para verificar se a
#pessoa está apta para doação de sangue, você criou todo o sistema sem utilizar
#funções. Nessa nova versão mantenha os recursos e verificações que foram
#propostas, porém, separe em funções as validações e recursos. Eaemplo: função
#para fazer a validação se a pessoa está apta: def validaRequisitos(): onde dentro do
#escopo da função, você deve colocar o processo de validação e retornar true ou
#false para mostrar ao usuário se ele está apto ou não.

nome=[]
cpf=[]
senha=[]
aptidao=[]

def printFinal():
    print("Nome:   ",nome," \nCPF:    ",cpf," \nSenha:  ",senha," \nAptidão:",aptidao)
def cadastroDados():
    nome.append(input("Insira seu nome:"))
    cpf.append(input("Insira seu cpf:"))
    senha.append(input("Insira sua senha:"))
    aptidao.append(input("Insira aqui se você está apto para doação de sangue:"))
    printFinal()

idadecont = 0
pesocont = 0
horascont =0
pessoaCadastrada=0

idade=(int(input("Insira a sua idade: ")))
peso=(float(input("Insira o seu peso: ")))
horas=(int(input("Insira quantas horas dormiu na noite passada: ")))

if idade>=16 and idade<=69:
    idadecont+=1
else:
    print("Idade fora dos requisitos!")
if peso>50:
    pesocont+=1
else:
    print("Peso fora dos requisitos!")
if horas>=6:
    horascont+=1
else:
    print("Horas de sono fora dos requisitos!")
if idadecont == 1 and pesocont == 1 and horascont == 1:
    print("Você pode ser um doador!")
    cadastro = (input("Parabéns! Você pode ser um doador, deseja se cadastrar? Digite S-Sim ou N-Não:"))
    if cadastro=="S":
        pessoaCadastrada = pessoaCadastrada+1
        cadastroDados()#volta pra def cadastroDados() e executa a linha de comandos que eu induzi
    else:
        print("Cadastro negado.")
else:
    print("Você não pode ser um doador.")
    cadastro = (input("Você não pode doar no momento, mas deseja se cadastrar? Digite S-Sim ou N-Não:"))
    if cadastro=="S":
        pessoaCadastrada = pessoaCadastrada+1
        cadastroDados()#volta pra def cadastroDados() e executa a linha de comandos que eu induzi
    else:
        print("Cadastro negado.")

