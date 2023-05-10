numeros = [234,546,567,523467,2343,54234]
pares = 0
for n in numeros:
    if n % 2 == 0:
        pares += 1
print(f"numero de pares {pares}")

num1 = [1,2,3,4,5,6,7,8,9,10]
num2 = [11,12,13,14,15,16,17,18,19,20]
for i in range(10):
    print(f"soma: {num1[i] + num2[i]}")

letras = ["a", "b", "c", "d", "i", "o", "h"]
qtd_vogais = 0
for l in letras:
    if l == "a" or l == "e" or l == "i" or l == "o" or l == "u":
        qtd_vogais += 1
print(f"quantidade de vogais: {qtd_vogais}")


profs = ["allan", "israel", "danilo", "yan", "luciano", "ana", "cordeiro"]
for prof in profs:
    if prof == "danilo":
        print("achei o danilo")
    else:
        print(f"droga achei o {prof}")


carros = ["ka", "celta", "golf", "fusca"]
preco = [10,200,5,1000]
preco_carro_mais_caro = 0
indice = 0
for i in range(len(carros)):
    if preco[i] > preco_carro_mais_caro:
        preco_carro_mais_caro = preco[i]
        indice = i

print(f"o carro mais caro eh o {carros[indice]}, com um preço de {preco[indice]}")

lista = ["a", "b", "c", "d", "i", "o", "h", "z"]
incremento = 0
if len(lista) % 2 != 0:
    incremento = 1
for i in range((len(lista)//2) + incremento):
    lista[i],lista[len(lista) - 1 - i] = lista[len(lista) - 1 - i], lista[i]
print(lista)