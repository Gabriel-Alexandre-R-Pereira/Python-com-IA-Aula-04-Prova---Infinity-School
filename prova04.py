def media(num1, num2, num3):
    soma = num1 + num2 + num3
    media_aritimetica = soma / 3

    return media_aritimetica

teste1 = media(8, 9, 10)
print(f"A média aritimética de 8, 9 e 10 é: {teste1}")

numero1 = 80
numero2 = 90
numero3 = 100
teste2 = media(numero1, numero2, numero3)
print(f"A média aritimética de 80, 90 e 100 é: {teste2}")

lista_numeros = []
for numero in range(3):
    numero = float(input("Dgite um número: "))
    lista_numeros.append(numero)
teste3 = media(*lista_numeros)
print(f"A média aritimética de {*lista_numeros,}: {teste3}")