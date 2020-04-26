# Calculadora em Python

# Desenvolva uma calculadora em Python com tudo que você aprendeu nos capítulos 2 e 3. 
# A solução será apresentada no próximo capítulo!
# Assista o vídeo com a execução do programa!

print("\n******************* Python Calculator *******************")

#As opções de calculos serão por meio da Expressão Lambda

soma = lambda x,y: x+y
subtracao = lambda x,y: x-y
multiplicacao = lambda x,y: x*y
divisao = lambda x,y: x/y

'''inicio da execução da calculadora'''

#obtendo a opção digitada pelo usuário
opcao = int(input('1 - Soma \n2 - Subtração\n3 - Multiplicação\n4 - Divisão\nEscolha uma das opções '))

#obtendo os valores por meio das variáveis
valor1 = int(input('Primeiro Valor '))
valor2 = int(input('Segundo Valor '))

'''condicionais dos resultados'''

if opcao == 1:
    print(str(valor1) +" + "+ str(valor2) + " = " + str(soma(valor1,valor2)))
elif opcao == 2:
    print(str(valor1) +" - "+ str(valor2) + " = " + str(subtracao(valor1,valor2)))

elif opcao == 3:
    print(str(valor1) +" * "+ str(valor2) + " = " + str(multiplicacao(valor1,valor2)))

elif opcao == 4:
    print(str(valor1) +" / "+ str(valor2) + " = " + str(divisao(valor1,valor2)))

else:
    print('Opção Inválida')
