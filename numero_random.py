import random

numero_random = random.randint(1, 101)
print(numero_random)

# lista de 101 números random entre el 1 y el 101
list_numeros_random = [random.randint(1, 101) for i in range(102)]
print(list_numeros_random)

#print(len(list_numeros_random))

randomer_number = random.choice(list_numeros_random)
print(randomer_number)

numbers_b = random.sample(range(1000), 12)
print(numbers_b)
