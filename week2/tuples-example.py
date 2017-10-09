empty_tuple = ()
empty_tuple = tuple()

my_tuple = ('hello', 'my', 'friend')
print(my_tuple)

tuple_with_list = ([], [])
print(tuple_with_list)
tuple_with_list[0].append('wow')
print(tuple_with_list)

print(hash(my_tuple))
