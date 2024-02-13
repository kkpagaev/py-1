# Гра "Нумо вгадай". Розробіть просту гру, де користувач має вгадати випадкове
# число від 1 дe 100. Для генерації випадкового числа використовуйте функцію
# random.randint(a, b) (тут a та b включно). Для отримання числа з консолі
# використовуйте функцію input(), результат якої обовʼязково явно приведіть до
# типу int.
import random

def cmp(a, b):
    if a > b:
        return 1
    elif a < b:
        return -1
    else:
        return 0

messages = {
    1: "Too low",
    0: "You win",
    -1: "Too high"
}


def play(start, input, count):
    n = int(input("Enter number: "))
    g = cmp(start, n)
    print(messages[g])
    if g == 0:
        print("You guessed in %d tries" % count)
        return
    play(start, input, count + 1)


def main():
    start = random.randint(1, 100)
    play(start, input, 1)

# main()

# def foo(n):


d = {
    "it": 3,
    "Harry Potter": 13,
    "Bible": 11,
}

for key, value in d.items():
    d[key] = value + 5

print(d)









