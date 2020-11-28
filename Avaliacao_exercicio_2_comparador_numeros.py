valor_1 = int(input("Insira o 1º valor: "))
valor_2 = int(input("Insira o 2º valor: "))
valor_3 = int(input("Insira o 3º valor: "))
valor_4 = int(input("Insira o 4º valor: "))

list1 = [valor_1,valor_2,valor_3,valor_4]
pares, impares, diferentes = 0, 0, 0

for num in list1:
   if num % 2 == 0:
      pares += 1
   else:
      impares += 1

diferentes = []
 
for item in list1: 
    if item not in diferentes: 
        diferentes.append(item)

print("Diferentes = %d, Pares = %d, Impares = %d" % (len(diferentes), pares, impares))