"""
Programa: eq_quad
Descrição: Este programa resolve uma equação quadrática com termos à escolha do usuário
Autor: Filipe Eich
Data: 28/02/2025
Versao: 0.0.1
"""

#Alocaçao de memoria

a=""
x1=""
x2=""
b=""
c=""
y=""
delta=""
aux=""


#Entrada de dados

a = float(input("\nOlá! Vamos achar o valor de X em uma equação quadrática? Considere o formato a.x² + b.x + c = y , Qual valor de a?: "))
b = float(input("\nAgora, me diga o valor para b: "))
c = float(input("\nPor fim, atribua o valor de c: "))
y = float(input("\nAgora, me diga o valor para y: "))


# Processamento de dados

delta=b**2-(4*a*(c-y))

if delta>0:
    x1=(-b + delta**0.5)/(2*a)
    x2=(-b - delta**0.5)/(2*a)
    aux=1
elif delta==0:
    x1= -b / (2*a)
    x2=-x1
    aux=1
else:
    aux=0


#Saida de dados

if aux==1:
    print(f"\nAqui estão as raízes da equação: X1 = {x1}; X2= {x2}")
elif aux==0:
    print(f"\nNão há solução real para o problema!")
