from itertools import combinations, permutations, product

data = [1, 2, 3]

print("Исходные данные:", data)

print("\nКомбинации по 2 элемента:")
for c in combinations(data, 2):
    print(c)

print("\nПерестановки:")
for p in permutations(data):
    print(p)

print("\nДекартово произведение:")
for pr in product(data, repeat=2):
    print(pr)