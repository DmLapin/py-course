empty_dict = {}
empty_dict = dict()

my_map = {
    'mutable': ['one', 'two', 'three'],
    'immutable': ('no', 'changes'),
}

print(my_map)
print(my_map['immutable'])

my_map['new'] = 'elem'
my_map['mutable'][0] = 'replaced'
print(my_map)

empty_dict.setdefault('key', 'default')
print(empty_dict)

for key in my_map:
    print(key)

for key, value in my_map.items():
    print('{} - {}'.format(key, value))



