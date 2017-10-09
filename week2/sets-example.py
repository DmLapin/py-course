empty_set = set()
number_set = {1, 2, 3, 3, 4, 5}

print(number_set)
print(2 in number_set)

odd_set = set()
even_set = set()

for number in range(10):
    if number % 2:
        odd_set.add(number)
    else:
        even_set.add(number)

print(odd_set, even_set)

print(odd_set | even_set)
print(odd_set & even_set)
print(odd_set - even_set)

even_set.remove(2)
print(even_set)

