# a = int(input('Primeiro Valor: '))
# b = int(input('Segundo Valor: '))
# c = int(input('Terceiro Valor: '))
# if a > b and a > c:
#     print('O maior número é {}'.format(a))
# elif b > a and b > c:
#     print('O maior número é {}'.format(b))
# else:
#     print('O maior número é: {}'.format(c))
# print('Final do Programa')
#------------------------------------------------------------
# a = int(input('Entre com o primeiro Valor: '))
# b = int(input('Entre com o segundo Valor: '))
# resto1 = a % 2
# resto2 = b % 2
# if resto1 == 0 or not resto2 > 0:
#     print('Foi digitado um número par')
# else:
#     print('Nenhum número par foi digitado')
#------------------------------------------------------------------
a = int(input('Primeiro Bimestre: '))
if a > 10:
    a = int(input('Você digitou errado. Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
if b > 10:
    b = int(input('Você digitou errado. Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
if c > 10:
    c = int(input('Você digitou errado. Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
if d > 10:
    d = int(input('Você digitou errado. Quarto Bimestre: '))
media = (a + b + c + d) / 4
if a <= 10 and b <= 10 and c <= 10 and d <= 10:
    print('Media: {}'.format(media))
else:
    print('Foi informado alguma nota errada')