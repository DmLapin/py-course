# int
int_num = 13
print(int_num)

int_num = 100_000_000
print(int_num)
print(type(int_num))

# float
float_num = 13.4
print(float_num)
print(type(float_num))

float_num = 1.5e2
print(float_num)

# complex
complex_num = 14 + 1j
print(type(complex_num))
print(complex_num.real)
print(complex_num.imag)

# none
answer = None
print(answer)
print(bool(answer))

# string
string = "hello"
for letter in string:
    print("Буква", letter)

tpl = "Hello, %s"
print(tpl % "username")

multiline = """hello
aaa"""
print(multiline)

byte_str = b"Hello"
print(byte_str)

unicode_str = "Привет"
enc_str = unicode_str.encode(encoding="utf-8")
print(enc_str)
print(enc_str.decode())
print(unicode_str[0:4])
print(unicode_str[::2])
print(unicode_str[::-1])
