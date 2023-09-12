

print("*********************************")
print("*****Olá, Seja bem vindo(a)!*****")
print("*********************************")
print("Iremos te auxiliar no cálculo no seu planejamento financeiro!")
print('Primeiramente precisamos de alguns dados:')
def calcular():
    while True:
        capital = float(input("Qual seu valor inicial?"))
        taxa = float(input("Qual a taxa de juros da sua aplicação (em %)?"))
        tempo = float(input("Por quantos meses seu capital estará sujeito a esse juros?"))
        juros = taxa / 100

        print('Qual cálculo você deseja realizar?')
        calculo = int(input('[1] Juros Simples [2] Juros Compostos'))
        if (calculo == 1):
            simples = capital * juros * tempo
            print(f'Esse é o seu capital total: {simples}')
        elif (calculo == 2):
            composto = capital * (1 + juros) ** tempo
            print(f'Esse é o seu capital total: {composto}')
        else:
            print('Opção invalida! Tente novamente!')
            calcular()
        break
def nova_consulta():
    repetir = int(input('Deseja realizar uma nova consulta? [1] para SIM ou [2] para NÃO?'))
    if repetir == 1:
        calcular()
    elif repetir == 2:
        print('Até a próxima!')
        exit()
    else:
        print('Opção inválida, tente novamente!')
        nova_consulta()

calcular()
nova_consulta()

