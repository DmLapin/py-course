f = open('testfile', 'r+', encoding='utf-8')

print(f)
print(f.read())
print(f.write('Appended string'))
f.seek(0)
print(f.read())
f.close()

