import random

number = random.randint(0, 11)

while True:
    answer = input("Number: ")
    if not answer or answer == "exit":
        break

    if not answer.isdigit():
        print("Not a number!")
        continue

    parsed_answer = int(answer)

    if parsed_answer > number:
        print("number is less")
    elif parsed_answer < number:
        print("number is great")
    else:
        print("Good job!")
        break
