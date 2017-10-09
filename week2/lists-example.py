empty_list = []
empty_list = list()

none_list = [None] * 10
print(none_list)

collection = ['one', 'two', 'three']
print(collection)

user_data = [
    ['Elena', 5],
    ['Andrew', 8]
]
print(user_data)

print(len(collection))
print(collection[0])
print(collection[-1])
collection[2] = 'something'
print(collection)
print('two' in collection)
print(collection[1:3])

for idx, item in enumerate(collection):
    print('#{} {}'.format(idx, item))

collection.append('appended')
print(collection)
del collection[0]
print(collection)
print(', '.join(collection))
print(sorted(collection))


